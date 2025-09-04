import streamlit as st

st.markdown("### Column 예시")
col1, col2, col3 = st.columns([2, 1, 1])

with col1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg")

st.markdown("--------")
st.markdown("### Expander 예시")

with st.expander("📺 요즘 OTT 플랫폼에서 뜨는 작품들"):
    st.write("""
    - **더 글로리**: 화제의 드라마, 역대급 복수극!
    - **피지컬: 100**: 서바이벌 예능 열풍!
    - **오징어 게임**: 전 세계를 휩쓴 한국형 데스게임!
    """)
    st.write("더 자세한 줄거리는 스포일러 방지를 위해 생략!")

with st.expander("⏰ 오늘의 소셜 미디어 소식"):
    st.write("""
    - 틱톡에서 난리 난 '#쿠쿠다스챌린지'
    - 인스타그램 릴스, 짧은 영상 편집 팁 공유하기
    - 재테크/절약 관련 '챌린지'도 인기 상승 중!
    """)

st.markdown("--------")
st.markdown("### Tab 예시")
tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)


with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )