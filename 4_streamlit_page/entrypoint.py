import streamlit as st

# 1. 여러 페이지 정보를 등록합니다.
pages = [
    st.Page("home.py", title="홈 화면", icon="🏠", default=True),
    st.Page("production.py", title="생산 데이터", icon="🏭"),
    st.Page("quality.py", title="품질 관리", icon="🔍"),
    st.Page("maintenance.py", title="예지 보전", icon="🛠️"),
]

# 2. 사용자가 선택한 페이지를 받아옵니다.
selected_page = st.navigation(pages)

# 3. 선택된 페이지를 실행(run)합니다.
selected_page.run()

