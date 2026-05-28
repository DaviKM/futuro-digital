import uvicorn
from fastapi import FastAPI
from maonamassa3 import router

app = FastAPI()
app.include_router(router)

if __name__ == '__main__':
    uvicorn.run('main:app', port=20000, reload=True)