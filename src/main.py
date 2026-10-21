from fastapi import FastAPI
from dotenv import load_dotenv 
from routes import base,data
from motor.motor_asyncio import AsyncIOMotorClient
from stores.llm.LLMProviderFactory import LLMProviderFactory
from stores.vectordb.VectorDBProviderFactory import VectorDBProviderFactory

from helpers.config import get_settings

# app initionalize

app=FastAPI()

async def startup_span():
    settings=get_settings()
    app.mongo_conn=AsyncIOMotorClient(settings.MONGODB_URL)
    app.db_client=app.mongo_conn[settings.MONGODB_DATABASE]
    
    llm_provider_factory=LLMProviderFactory(settings)
    vectordb_provider_factory=VectorDBProviderFactory(settings)
    
    
    app.generation_client=llm_provider_factory.create(provider=settings.GENERATION_BACKEND)
    app.generation_client.set_generation_model(settings.GENERATION_MODEL_ID)
    
    app.embedding_client=llm_provider_factory.create(provider=settings.EMBEDDING_BACKEND)
    app.embedding_client.set_embedding_model(model_id=settings.EMBEDDING_MODEL_ID,
                                             embedding_size=settings.EMBEDDING_MODEL_SIZE
                                             )
    
    
    app.vectordb_client=vectordb_provider_factory.create(provider=settings.VECTOR_DB_BACKEND)
    app.vectordb_client.connect()
    
    
        
    
async def shutdown_span():
    app.mongo_conn.close()
    app.vectordb_client.disconnect()



app.on_event('startup')(startup_span)
app.on_event('shutdown')(shutdown_span)

#Base app API
app.include_router(base.base_router)

# Data app API
app.include_router(data.data_router)



