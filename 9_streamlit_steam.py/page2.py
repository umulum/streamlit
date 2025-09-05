import streamlit as st
from app import sentiment_wave_banner, sentiment_predict # app.py에서 함수를 불러옵니다.

def show_sentiment_app():
    st.title("감성분석 테스트 💡")
    st.write("---")
    st.markdown("""아래에 **스팀 게임 리뷰**와 유사한 문장을 입력하고, 해당 리뷰의 **감성(긍정/부정)**을 예측해보세요.""")

    # 세션 상태 초기화 및 관리
    if 'user_input' not in st.session_state:
        st.session_state.user_input = "이 게임 정말 재밌어요! 시간 가는 줄 모르겠네요."
    if 'sentiment_result' not in st.session_state:
        st.session_state.sentiment_result = None
    if 'score' not in st.session_state:
        st.session_state.score = 0.0

    # 버튼 클릭 시 실행될 함수
    def on_button_click():
        """버튼 클릭 시 분석을 수행하고 결과를 세션 상태에 저장하는 함수"""
        if st.session_state.user_input:
            with st.spinner("분석 중..."):
                score, sentiment = sentiment_predict(st.session_state.user_input)
            st.session_state.score = score
            st.session_state.sentiment_result = sentiment
        else:
            st.session_state.sentiment_result = None

    # 사용자 입력 텍스트 영역
    st.text_area(
        "리뷰를 입력하세요:",
        value=st.session_state.user_input,
        height=150,
        key='user_input'
    )

    # 분석 버튼
    # 문제 해결: on_click 인자에 이름을 명시적으로 붙여줍니다.
    st.button("감성 분석 실행", on_click=on_button_click, key="sentiment_button")

    # 세션 상태에 결과가 있을 때만 물결 배너와 결과 출력
    if st.session_state.sentiment_result:
        sentiment_wave_banner(st.session_state.score)
        st.write("---")
        st.markdown("#### 분석 결과 상세")

        # 예측 감성에 따라 다른 색상의 박스를 사용합니다.
        if st.session_state.sentiment_result == "부정 (Negative)":
            st.error(f"입력 문장: **{st.session_state.user_input}**")
            st.error(f"예측 감성: **{st.session_state.sentiment_result}**")
            st.error(f"예측 확률: **긍정 {st.session_state.score*100:.2f}% / 부정 {(1 - st.session_state.score)*100:.2f}%**")
        else:
            st.info(f"입력 문장: **{st.session_state.user_input}**")
            st.info(f"예측 감성: **{st.session_state.sentiment_result}**")
            st.info(f"예측 확률: **긍정 {st.session_state.score*100:.2f}% / 부정 {(1 - st.session_state.score)*100:.2f}%**")

if __name__ == "__main__":
    show_sentiment_app()