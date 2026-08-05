# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

# # path parameters
# @app.get("/items/{item_id}")
# async def read_item(item_id):
#     return {"item_id": item_id}


# # path parameters with type
# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}

# #----------------------------------------------------------
# # Create enum class
# #----------------------------------------------------------
# from enum import Enum

# from fastapi import FastAPI


# class ModelName(str, Enum):
#     alexnet = "alexnet"
#     resnet = "resnet"
#     lenet = "lenet"


# app = FastAPI()


# @app.get("/models/{model_name}")
# async def get_model(model_name: ModelName):
#     if model_name is ModelName.alexnet:
#         return {"model_name": model_name, "message": "Deep Learning FTW!"}

#     if model_name.value == "lenet":
#         return {"model_name": model_name, "message": "LeCNN all the images"}

#     return {"model_name": model_name, "message": "Have some residuals"}

# #-------------------------------------------------------------------
# #Path Converter
# #-------------------------------------------------------------------
# # from fastapi import FastAPI

# # app = FastAPI()

# @app.get("/files/{file_path:path}")
# async def read_file(file_path: str):
#     return {"file_path": file_path}

#------------------------------------------------------------------
#Stage 1: Your first real endpoint
#------------------------------------------------------------------
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return{
        "name": "Task API",
        "version": "1.0",
        "endpoints": ["/tasks"]
    }

@app.get("/health")
def health():
    return{
        "status": "ok"
    }

@app.get("/about")
def about():
    return{
        "author": "Danelle",
        "course": "CRUD API"
    }

#-----------------------------------------------------------------
#Stage 2: Read: list and a single task
#-----------------------------------------------------------------

from fastapi import FastAPI, HTTPException

app = FastAPI()

tasks = [
    {
        "id": 1,
        "title": "Learn FastAPI",
        "done": False
    },
    {
        "id": 2,
        "title": "Buy groceries",
        "done": True
    },
    {
        "id": 3,
        "title": "Build CRUD API",
        "done": False
    }
]

@app.get("/")
def read_root():
    return {"message: Hello World"}

@app.get("/tasks")
def get_tasks():
    return tasks

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
        
    raise HTTPException(
        status_code = 404,
        detail = f"Task {task_id} not found"
    )