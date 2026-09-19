from fastapi import FastAPI
from dotenv import load_dotenv 
from routes import base,data
load_dotenv(override=True)

# app initionalize

app=FastAPI()


#Base app API
app.include_router(base.base_router)

# Data app API
app.include_router(data.data_router)



