from fastapi import APIRouter
import os

base_router=APIRouter(
    prefix='/api/v1',tags=['api_v1'])

@base_router.get('/first',) # اللي جوا الجت بيتضاف بعد ال /api/v1
async def welcome():
    app_name=os.getenv('APP_NAME')
    app_version=os.getenv('APP_VESROIN')
    
    return {
        'app name':app_name,
        'app version':app_version
    }

@base_router.get('/second')
async def calculate():
    
    return '10+5=15'


advanced_router=APIRouter(
    prefix='/api/v1/adv'
)


@advanced_router.get('/third',tags=['adv'])
async def make_prompt():
    return 'prompt'