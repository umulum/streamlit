import streamlit as st
import pandas as pd


st.title("생산 데이터")
st.write("생산량, 가동시간, 공정별 데이터 분석을 해보세요.")

# 예시 데이터: 실제로는 CSV나 DB에서 불러올 수 있음
data = {
    "라인": ["A", "B", "C"],
    "생산량": [1000, 800, 1200],
    "가동시간": [22, 19, 24],
}
df = pd.DataFrame(data)

st.subheader("생산 데이터 테이블")
st.dataframe(df)

st.subheader("라인별 생산량 차트")
st.bar_chart(df.set_index("라인")["생산량"])
