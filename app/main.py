from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Optional

app=FastAPI()

@app.get('/')
def home():
    return 'hello world'

class Post(BaseModel):
    id: int
    title: str
    content: str


posts = [
    {
        'id':1,
        'title':'post1',
        'content':'text1'
    },
    {
        'id':2,
        'title':'post2',
        'content':'text2'
    },
    {
        'id':3,
        'title':'post3',
        'content':'text3'
    }
]


@app.get('/items')
def get_posts() -> list:
    return posts
    

@app.get('/items/{id}')
def get_posts(id: int) -> dict:
    for post in posts:
        if post['id'] == id:
            return post
    raise HTTPException(status_code=404, detail='Post not found')

@app.get('/search')
def search(post_id: Optional[int] = None) -> Dict[str, Optional[Post]]:
    if post_id:
        for post in posts:
            if post['id'] == post_id:
                return {'data': Post(**post)}
        raise HTTPException(status_code=404, detail='Post not found')
    else:
        return {'data': None}