from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

#the app instance is the main component of our fastapi application .it is used to configure the application
#/ping is the path of the endpoint

#the @app.get() decorator is used to define an endpoint

class Custom(BaseModel):
    name:str
    age:int

@app.get("/ping")
async def root():
    return {"message":"hello world !!"}

@app.get("/")
async def root():
    return {"message":"welcome !!"}

@app.get("/blog/comments")
async def read_blog_comments():
    return {"comments":"no comments yet !!"}

@app.post("/blog/{blog_id}")
async def read_blog(blog_id: int, request_body: Custom, q: str= None, name: str= ''):
    print(request_body)
    print(q,name)
    return {"blog_id": blog_id}


