import uvicorn

from apscheduler.schedulers.background import BackgroundScheduler

from datetime import datetime, timedelta

from fastapi import FastAPI

app = FastAPI()

schedule = BackgroundScheduler(timezone='Asia/Seoul')
schedule.start()

@app.get("/")
async def read_root() :
    return {"message" : "root"}

@app.get("/schedule/{user_id}/{start}/{interval}/")
async def read_schedule(user_id: int, start: int, interval: int):
    def scheduler():
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"user_id : {user_id}, start_time : {start_time:%Y-%m-%d %H:%M:%S}, current_time : {current_time}")
    
    start_time = datetime.now()+timedelta(seconds=start)
    schedule_id = str(user_id)
    
    if schedule.get_job(schedule_id):
        schedule.remove_job(schedule_id)
    
    schedule.add_job(scheduler, 'interval', seconds=interval, start_date=start_time, id=schedule_id)

    result = dict()
    result.update(
        user_id  = user_id,
        now      = datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        start    = start_time.strftime("%Y-%m-%d %H:%M:%S"),
        interval = interval
        )
    return result

# class CallSched(BaseModel):
#     start_time   : str
#     writing_cycle: int
#     account      : str
#     uid          : int


# def job(shed_id, uid):
#     print("start_schedule")

# def scheduling_job(interval, start_time, id, uid):
#     sched.add_job(lambda: job(id, uid), 'interval', seconds=interval, start_date=start_time, id=id)
    

# @app.get("/")
# async def root():
#     return {"message": "tripod-scheduler"}


# @app.post("/sched/")
# async def scheduler(callSched: CallSched):
#     scheduling_job(callSched.writing_cycle, callSched.start_time, callSched.account, callSched.uid)
#     return callSched


# @app.post("/sched_change/")
# async def modify(callSched: CallSched):
#     sched.remove_job(callSched.account)
#     scheduling_job(callSched.writing_cycle, callSched.start_time, callSched.account, callSched.uid)
#     return callSched

if __name__ == '__main__':
    uvicorn.run(app="main:app", host="0.0.0.0", port=8000, reload=True)
