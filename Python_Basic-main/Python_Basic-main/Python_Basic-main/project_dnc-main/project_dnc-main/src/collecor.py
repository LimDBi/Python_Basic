# DAUM NEWS COLLECTOR ver 1.0
# - 작성일자: 2023년 11월 8일
# - 작성자: LimDBi
# - 내용: 사용자가 수집하고 싶은 뉴스 카테고리를 입력하면 해당 카테고리의 실시간 뉴스 기사와 제목을 수집하는 프로그램
# - 라이브러리: requests, beautifulsoup4, pymongo

# - 프로세스
#   1) 사용자로부터 뉴스 카테로리를 입력
#   2) 해당 카테고리의 실시간 다음뉴스를 수집(제목, 본문)
#   3) 수집 한 기사를 데이터베이스(MongoDB)에 저장

import requests     # 전체 소스코드 가져오기
from bs4 import BeautifulSoup   # 원하는 정보 SELECT
from src.service_news import get_news

# 뉴스 수집(Python) -> Pandas의 데이터프레임 -> Excel 저장


def news_collector(category, page=1, count=1):
    collect_list = []   # 향후 데이터프레임 변환용!


    while True:
        url = f"https://news.daum.net/breakingnews/{dict_news[category]}?page={page}"
        result = requests.get(url)

        if result.status_code == 200:
            print(result, "접속 성공 → 데이터를 수집합니다.")
            doc = BeautifulSoup(result.text, "html.parser")
            url_list = doc.select("ul.list_news2 a.link_txt")

            if len(url_list) == 0:
                break;
            for url in url_list:
                count += 1
                print(f"{count}번", "=" * 100)

                data = get_news(url["href"], category)
                collect_list.append(data)

        else:
            print("URL경로가 잘못되었습니다.")

        page += 1
    # 뉴스 수집 완료
    #   - collect_list -> dataframe
    col_name = ["category", "title", "content", "date"]
    df_review = pd.DataFrame(collect_list, columns = col_name)

    return df_review, count     # tuple type 괄호 생략된 형태 -> (df_review, count)







