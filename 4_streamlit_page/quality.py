import streamlit as st
import matplotlib.pyplot as plt
import koreanize_matplotlib
import random


st.title("품질 관리")
st.write("불량률, 불량 유형, 품질 지표 등을 확인합니다.")

# 간단히 불량률 히스토그램 예시 (평균 2%, 표준편차 1% 가정)
data = [random.gauss(0.02, 0.01) for _ in range(100)]

fig, ax = plt.subplots()
ax.hist(data, bins=20, color="orange")
ax.set_title("불량률 분포 (예시)")
ax.set_xlabel("불량률 (%)")
ax.set_ylabel("빈도")

st.pyplot(fig)

