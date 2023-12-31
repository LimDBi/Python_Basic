# Streamlit 라이브러리
#   - Python으로 손쉽게 웹사이트를 생성할 수 있는 라이브러리
#   - 기존에는 HTML, CSS, JS 등과 같은 기술을 공부해야 웹사이트 구현 가능
#   - Streamlit을 사용하면 위의 기술을 모르더라도 블럭 쌓듯이 손쉽게 구현 가능
#   - 단, 우리가 원하는 디테일한 작업은 불가능

# pip install streamlit

import streamlit as st

news_catecory = {
    "society": "사회",
    "politics": "정치",
    "economic": "경제",
    "foreign": "국제",
    "culture": "문화",
    "entertain": "연예",
    "sports": "스포츠",
    "digital": "IT"
}

st.set_page_config(
    page_title="뉴스 수집기",
    page_icon="./images/favicon_01.png"
)

st.title(":orange[NEWS COLLECTOR]")
st.text("DAUM 뉴스를 수집합니다.")

# 터미널에 명령어 입력: streamlit run ./app.py
# 사이트 열어서 설정 -> run on save 체크 (코드 바뀔 때마다 자동으로 반영되도록)

with st.form(key="form"):
    category = st.text_input("카테고리 입력").strip()
    submitted = st.form_submit_button("Submit")

    if submitted:
        st.write(category)