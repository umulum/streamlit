import streamlit as st

st.markdown("### 버튼 클릭 횟수 (session_state 미사용)")

count = 0  # 항상 0으로 시작

if st.button("버튼을 눌러보세요!"):
    count += 1

st.write(f"버튼 클릭 횟수: {count}")

st.markdown("-------")
st.markdown("### 버튼 클릭 횟수 (session_state 사용)")

# session_state에 count 키가 없으면 0으로 초기화
if "count" not in st.session_state:
    st.session_state.count = 0

if st.button("버튼"):
    st.session_state.count += 1

st.write(f"버튼 클릭 횟수: {st.session_state.count}")
