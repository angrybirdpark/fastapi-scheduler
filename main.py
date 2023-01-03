from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root() :
    return {"message" : "success"}

@app.get("/{user_id}/{start_time}/{interval_time}")
def read_item(user_id : int, start_time : int, interval_time = int) :
    return {"user_id" : user_id, "start_time" : start_time, "interval_time" : interval_time}    