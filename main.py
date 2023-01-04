import math, uvicorn, time
from datetime import datetime, timedelta

from fastapi import FastAPI
from fastapi import requests

from pydantic import BaseModel

from typing import Optional

from scheduler import job

from apscheduler.schedulers.background import BackgroundScheduler

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
async def read_schedule(user_id: int, start: int, interval: float):
    today = datetime.now().date()
    start_time = datetime(today.year, today.month, today.day, hour=start)
    cnt = math.ceil(24/interval)
    result = dict()
    result_time = list()

    def job2():
        print(f"user_id : {user_id}, time : {datetime.now()}")





    sched = BackgroundScheduler(timezone='Asia/Seoul') #백그라운드로 실행하기 위해 선언
    sched.start() 

    sched.add_job(
        job2,
        'interval',
        seconds=1,
        id="scheduler") # 수행할 함수를 job에 등록
    #1초 마다 한번씩 함수를 수행한다.







    for i in range(cnt):
        added_time = start_time + timedelta(hours=interval*i)
        result_time.append(added_time.strftime("%Y-%m-%d-%H-%M-%S"))
    result['user_id'] = 3
    result['schedule'] = result_time
    return result


if __name__ == '__main__':
    uvicorn.run(app="main:app", host="0.0.0.0", port=8000, reload=True)