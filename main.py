import uvicorn

from apscheduler.schedulers.background import BackgroundScheduler

from datetime import datetime, timedelta

from fastapi import FastAPI

from pydantic import BaseModel

from typing import Optional

app = FastAPI()

@app.get("/")
async def read_root() :
    return {"message" : "root"}

@app.get("/schedule/{user_id}/{start}/{interval}/")
async def read_schedule(user_id: int, start: int, interval: int):
    start_time = datetime.now()+timedelta(seconds=start)

    def scheduler():
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"user_id : {user_id}, start_time : {start_time:%Y-%m-%d %H:%M:%S}, current_time : {current_time}")

    schedule = BackgroundScheduler(timezone='Asia/Seoul')
    schedule.start() 

    schedule.add_job(
        scheduler,
        'interval',
        seconds    = interval,
        start_date = start_time,
        id         = "scheduler" + str(user_id)
        )

    result = dict()
    result.update(
        user_id  = user_id,
        now      = datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        start    = start_time.strftime("%Y-%m-%d %H:%M:%S"),
        interval = interval
        )
    return result

# @app.get("/schedule/{user_id}/{start}/{interval}/")
# async def read_schedule(user_id: int, start: int, interval: int):
#     start_time = datetime.now() + timedelta(seconds=start)
    
#     def scheduler():
#         print(f"user_id : {user_id}, time : {datetime.now()}")

#     sched = BackgroundScheduler(timezone='Asia/Seoul')
#     sched.start() 

#     sched.add_job(
#         scheduler,
#         'interval',
#         seconds=interval,
#         start_date = start_time,
#         id="scheduler"
#         )

#     result = dict()
#     result.update(
#         user_id  = user_id,
#         now      = datetime.now(),
#         start    = start_time,
#         interval = interval
#         )
#     return result

if __name__ == '__main__':
    uvicorn.run(app="main:app", host="0.0.0.0", port=8000, reload=True)