from pydantic import BaseModel

class Post(BaseModel):
    id: int
    title: str
    content: str