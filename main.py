from fastapi import FastAPI

app=FastAPI()

# @app.get('/welcome')

@app.get('/welcome')
def welcome():
    return {"message":"Welcome to mini RAG App 0.1"}
