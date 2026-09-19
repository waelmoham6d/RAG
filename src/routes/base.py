from fastapi import APIRouter ,FastAPI,Depends
from helpers import Settings,get_settings
base_router=APIRouter(
    prefix='/api/v1',
    tags=['api_v1']
)

@base_router.get('/')
async def welcome(app_settings:Settings = Depends(get_settings)):
    app_name=app_settings.APP_NAME
    app_version=app_settings.APP_NAME
    
    return {
        'App Name:':app_name
        ,'App version:':app_version
            }
    
    

