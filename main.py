from fastapi import FastAPI
from database import engine
import models
import uvicorn
from routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='Backstract Generated APIs - fast-api-coll-d76c593cf1db40f392182f05c1b7d72b',debug=False,docs_url='/frosty-wilson-ec8ac27ebeba11efb2290242ac12000522/docs',openapi_url='/frosty-wilson-ec8ac27ebeba11efb2290242ac12000522/openapi.json')

app.include_router(router, prefix='/frosty-wilson-ec8ac27ebeba11efb2290242ac12000522/api', tags=['APIs v1'])

def main():
    uvicorn.run('main:app', host='127.0.0.1', port=8008, reload=True)

if __name__ == '__main__':
    main()