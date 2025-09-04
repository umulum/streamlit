import streamlit as st

# 앱 전체 페이지 타이틀, 레이아웃 설정
st.set_page_config(page_title="제조 결함 대시보드", layout="wide")

# 페이지 리스트 정의
pages = [
    st.Page("dashboard_page.py", title="대시보드", icon="📊", default=True),
    st.Page("prediction_page.py", title="예측 및 EDA", icon="🤖"),
]

# 페이지 네비게이션 생성
pg = st.navigation(pages)

# 사용자가 선택한 페이지 실행
pg.run()
