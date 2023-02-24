# print("Hello, Python")
from fastapi import FastAPI
from models import Programmer, Languages
from typing import List
print("hello world")
#this is a comment
name = "Karla"
#this is how you declare a variable
age=28
has_pets= True
print(name , age , has_pets)
#lets write a function we use def keyword for it
def hello():
 print("Hello , Python")
hello()
def add(x,y):
 print(x+y)
add(1,4)
#az inja bakhshe api shooroo mishe
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
    #http://127.0.0.1:8000
    #http://127.0.0.1:8000/docs

db: List[Programmer] = [
    Programmer(id= 1, name="Dennis Ritchie", languages=[Languages.b, Languages.c]),
    Programmer(id= 2, name="Brian Wilson Kernighan", languages=[Languages.c]),
    Programmer(id= 3, name="James Gosling", languages=[Languages.java]),
    Programmer(id= 4, name="Guido van Rossum", languages=[Languages.python]),
    Programmer(id= 4, name="Brendan Eich", languages=[Languages.javascript])
]

@app.get("/programmers")
async def get_programmers():
    return db