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

if __name__ == '__main__':
    uvicorn.run(app="main:app", host="0.0.0.0", port=8000, reload=True)