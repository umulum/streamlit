import pandas as pd
import numpy as np
import streamlit as st

st.title("차트 시각화 실습")

# 예시 데이터 생성
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"]
)

st.line_chart(chart_data)   # 라인 차트
st.bar_chart(chart_data)    # 바 차트
st.area_chart(chart_data)   # 영역 차트


st.markdown("-------")

import matplotlib.pyplot as plt
import koreanize_matplotlib

# 임의 데이터 생성
x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y, color="blue", label="sin(x)")
ax.set_title("Matplotlib Sin Graph")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.legend()

st.pyplot(fig) 

import seaborn as sns

# 샘플 데이터셋: tips
tips = sns.load_dataset("tips")

fig, ax = plt.subplots()
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time", ax=ax)
ax.set_title("Seaborn Scatter Plot (Tips Data)")

st.pyplot(fig)

# 이제 matplotlib 그래프에 한국어를 바로 사용할 수 있음
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [10, 30, 20])
ax.set_title("한글 제목")
ax.set_xlabel("가로축")
ax.set_ylabel("세로축")

st.pyplot(fig)


st.markdown("--------")
import plotly.express as px

# 예시로 iris 데이터셋 사용
df_iris = px.data.iris()

fig = px.scatter(
    df_iris,
    x="sepal_width",
    y="sepal_length",
    color="species",
    size="petal_length",
    title="Plotly - Interactive Scatter Plot"
)

st.plotly_chart(fig)  # st.plotly_chart()를 사용

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")
st.plotly_chart(fig)