from fastapi import UploadFile,Depends,APIRouter,status,Request
from helpers.config import get_settings,Settings
from fastapi.responses import JSONResponse
from models import ResponseSignal
from controllers import DataController,ProcessController
from .schemes.data import ProcessRequest
import aiofiles
import logging
from models.ProjectModel import ProjectModel 
from models.ChunkModel import ChunkModel 
from models.db_schemes import DataChunk
logger=logging.getLogger('uvicorn.error')

data_router=APIRouter(
    prefix='/api/v1/data'
    ,tags=['data']
)

@data_router.post('/upload/{project_id}')
async def upload_data(request:Request,file:UploadFile,project_id:str,app_settings:Settings = Depends(get_settings)):
    
    project_model=ProjectModel(
        db_client=request.app.db_client
    )
    
    project=await project_model.get_project_or_create_one(
        project_id=project_id
        )
    
    
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
async def process_endpoint(project_id:str,process_request:ProcessRequest,request:Request):
    chunk_size=process_request.chunk_size
    file_id=process_request.file_id
    overlap_size=process_request.overlap_size
    do_reset=process_request.do_reset
    
    project_model=ProjectModel(
        db_client=request.app.db_client
    )
    
    project=await project_model.get_project_or_create_one(
        project_id=project_id
    )
    
    controller=ProcessController(project_id=project_id)
    
    file_chunks=controller.process_file_content(file_id=file_id,chunk_size=chunk_size,overlap_size=overlap_size)
    
    if file_chunks is None or len(file_chunks)==0:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                'signal':ResponseSignal.PROCESSING_FAILED.value
            }
        )
    

    file_chunks_records=[
        DataChunk(
            chunk_text=chunk.text,
                chunk_metadata=chunk.metadatas,
                chunk_order=i+1,
                chunk_project_id=project.id
    
        )
        for i,chunk in enumerate(file_chunks)
        ]
    
    chunk_model=ChunkModel(
        db_client=request.app.db_client
    )
    
    if do_reset==1 : 
        _= await chunk_model.delete_chunks_by_project_id(
            project_id=project.id
        )
        
    
    records_no = await chunk_model.insert_many_chunks(
        chunks=file_chunks_records
    )    
    
    return JSONResponse(
        content={
            'signal':ResponseSignal.PROCESSING_SUCCESS.value,
            'inserted_chunks':records_no
        }
    )
    
    
