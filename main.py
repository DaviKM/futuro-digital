import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')

app = FastAPI()

@app.get('/')
def index():
    return {"Hello":"World"}

@app.get('/adicionar-cliente')
def 