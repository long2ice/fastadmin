import os

import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise
from fastadmin import app as admin_app


def create_app():
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
    register_tortoise(app, config={
        "connections": {"default": os.getenv("DATABASE_URL") or 'mysql://root:123456@127.0.0.1:3306/fastadmin'},
        "apps": {"models": {"models": ["examples.models"], "default_connection": "default"}},
    }, generate_schemas=True)
    return app


app_ = create_app()

if __name__ == '__main__':
    uvicorn.run('main:app_', debug=True, reload=True)
