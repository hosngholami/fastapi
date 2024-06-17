from fastapi import FastAPI
from core.services import  add_number

app = FastAPI()


@app.get("/")
def hello():
    return "hello word"


@app.get('/blog/')
def get_blog(title):

    return {'product title' : f'{title}' } 


app.include_router(add_number.router)
 