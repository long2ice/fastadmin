import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from fastadmin import app as admin_app

app = FastAPI()
app.mount('/admin', admin_app)
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

if __name__ == '__main__':
    uvicorn.run('main:app', debug=True, reload=True)
