# pip install apscheduler 
# fileName : test.py

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.base import JobLookupError
import time
from datetime import datetime


def job(): # 수행할 일
    print(datetime.now()) 

# sched = BackgroundScheduler(timezone='Asia/Seoul') #백그라운드로 실행하기 위해 선언
# sched.start() 

# sched.add_job(job, 'interval', seconds=1, id="hello") # 수행할 함수를 job에 등록
# #1초 마다 한번씩 함수를 수행한다.

# count = 0
# while True:
#     time.sleep(3)
#     print("count :",count)
#     count += 1
#     if count > 10:
#         sched.shutdown()
#         break