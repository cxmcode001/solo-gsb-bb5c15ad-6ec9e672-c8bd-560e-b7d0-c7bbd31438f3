from fastapi import FastAPI
from pydantic import BaseModel

# 假设请求体长这样
class Item(BaseModel):
    pass

app = FastAPI()

# 定义根路由
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
