# 스케줄러(Scheduler)
#   - 정해진 일정에 맞춰서 프로그램을 동작!
#   예) 12시간에 맞춰
#       5분마다
#       특정일에만(크리스마스)

# 스케줄러 + 프로그램 -> 완성 -> 서버(동작)

# apscheduler
#   1. blocking
#    - 스케줄러 + 프로그램만 동작
#   2. background
#    - 동작은 하되 뒤에서 조용히

# 파이썬 터미널에서 설치 pip install apscheduler
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime


def print_today():
    print(datetime.now()) #현재시간 출력

# 1. 스케줄러 생성
scheduler = BlockingScheduler()

scheduler.add_job(print_today(), "interval", seconds=5)     #5초에 한번씩 현재시간을 출력
scheduler.start()