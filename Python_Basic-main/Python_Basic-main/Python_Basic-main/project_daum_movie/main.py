# TO DO: 1. 스케줄링
#        2. 리뷰 수집 시 중복체크(중복인 경우 수집 X)
#        3. 데이터베이스에 수집된 데이터 -> Excel로 저장
#        4. 데이터베이스에 수집된 데이터 -> 간다한 텍스트 분석
#        5. 데이터베이스에 수집된 데이터 -> WordCloud 시각화
# TIP: 이모티콘 -> 텍스트 변환시 형태 확인 후 정규식 이용하여 제거

from collect.collect_daum_movie_review import review_collector
from apscheduler.schedulers.blocking import BlockingScheduler


def main():
    print("=" * 100)
    print("== 영화 리뷰 수집기 ver1.0 ==")
    print("=" * 100)
    movie_code = input("== 영화코드: ")  # 169328 (나폴레옹)
    print('==MSG: "매일 낮 12시마다 한번씩 수집됩니다."')
    scheduler = BlockingScheduler()
    scheduler.add_job(review_collector,    # Job
                      trigger="cron",      # "Cron" 표기법 사용
                      args=[movie_code],   # Job의 매개변수
                      hour="12",           # 시간
                      minute="0")          # 분
    review_collector(movie_code)


if __name__ == "__main__":
    main()


