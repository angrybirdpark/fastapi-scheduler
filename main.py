import math
from datetime import datetime, timedelta

from fastapi import FastAPI
from fastapi import requests

from pydantic import BaseModel

from typing import Optional

app = FastAPI()

class User(BaseModel):
    id : int

class Schedule(BaseModel):
    id : int
    start_time : int
    interval_time : int
    user : User

@app.get("/")
async def read_root() :
    return {"message" : "success"}

# @app.post("/schedules/", response_model=Schedule)
# async def create_item(schedule: Schedule):
#     data = requests.post(data)
#     start_time = data[start_time]
#     return start_time

@app.get("/schedule/{user_id}/{start}/{interval}/")
async def read_schedule(user_id: int, start: int, interval: int):
    today = datetime.now().date()
    start_time = datetime(today.year, today.month, today.day, hour=start)
    cnt = math.ceil(24 / interval)
    result = dict()
    result_time = list()
    
    for i in range(cnt):
        added_time = start_time + timedelta(hours=interval*i)
        result_time.append(added_time.strftime("%Y-%m-%d-%H-%M-%S"))
    result['user_id'] = user_id
    result['schedule'] = result_time
    return result