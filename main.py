from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI() #create an instance of fastAPI
#the app instance is the main component of our FastAPI application, it is used to configure the application

class Custom(BaseModel):
    name: str
    age: int

# the @app.get() decorator is used to define the endpoint
# /ping is the path of the endpoint
@app.get("/ping")
async def root():
    return {"message": "Hello World..."} #when somebody hits the /ping endpoint this is the part we need to return

@app.get("/")
async def root():
    return {"Welcome.."}

# This is a classic "Path Ordering" concept in web development. In FastAPI (and most web frameworks), the order in which you write your code determines how the server interprets a user's request.
@app.get("/blogs/comments")
async def read_blog_comments():
    return {"comments": "No Comments yet!"}

@app.get("/blogs/{blog_id}")
async def read_blog(blog_id:int, request_body: Custom, q: str = None):
    print(request_body)
    print(q)
    return {"blog_id": blog_id} 