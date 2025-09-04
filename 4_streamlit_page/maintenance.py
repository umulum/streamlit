import streamlit as st


st.title("예지 보전 (Predictive Maintenance)")
st.write(
    """
    설비 센서(진동, 온도, 압력 등) 데이터를 토대로
    고장 징후를 사전에 파악하는 모델 예시를 구현할 수 있습니다.
"""
)

st.subheader("예시: 간단 설명")
st.write(
    """
    - 일정 주기마다 장비 상태 데이터를 수집
    - 특정 임계값(Threshold)을 초과하는 경우, 유지보수 알림
    - 예지 보전 모델로 고장 발생 가능 시점 예측
"""
)


