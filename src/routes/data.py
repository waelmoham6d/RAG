from fastapi import UploadFile,Depends,APIRouter,status
from helpers.config import get_settings,Settings
from fastapi.responses import JSONResponse
from models import ResponseSignal
from controllers import DataController,ProcessController
from schemes.data import ProcessRequest
import aiofiles
import logging

logger=logging.getLogger('unicorn.error')

data_router=APIRouter(
    prefix='/api/v1/data'
    ,tags=['data']
)

@data_router.post('/upload/{project_id}')
async def upload_data(file:UploadFile,project_id,app_settings:Settings = Depends(get_settings)):

    controller=DataController()
    
    is_valid,result_signals=controller.validate_uploaded_file(file,project_id)
    
    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                'signal':result_signals
            }
        )
        
    
    file_path,file_id=controller.generate_unique_file_path(project_id,
                                                           orig_file_name=file.filename)
    
    
    try :
        async with aiofiles.open(file_path,mode='wb') as f:
            while True:
                chunk = await file.read(app_settings.FILE_DEFAULT_CHUNK_SIZE)
                if not chunk:
                    break
                await f.write(chunk)
                
    except Exception as e:
        
        logger.error(f'Error while uploading file: {e}')
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                'signal':ResponseSignal.FILE_UPLOAD_FAILED.value
            }
        )
    
    return JSONResponse(
        content=
        {
            'signal':ResponseSignal.FILE_UPLOAD_SUCCESS.value,
            'file_id':file_id
        }
    )
            




@data_router.post("/process/{project_id}")
async def process_endpoint(file_id:str,process_request:ProcessRequest):
    chunk_size=process_request.chunk_size
    file_id=process_request.file_id
    overlab_size=process_request.overlab_size
    
    controller=ProcessController()
    
    chunks=controller.process_file_content(file_id=file_id,chunk_size=chunk_size,overlab_size=overlab_size)
    
    if chunks is None or len(chunks)==0:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                'signal':ResponseSignal.PROCESSING_FAILED.value
            }
        )
    
    
    
    return chunks
