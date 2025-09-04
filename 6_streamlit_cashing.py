import streamlit as st
import time

st.markdown("### 캐싱 미사용 예제")

def expensive_computation1(n):
    # 실제로는 더 복잡한 연산이라고 가정
    time.sleep(3)  # 3초 대기 (연산 비용 시뮬레이션)
    return sum(i*i for i in range(n))

options = [1000, 3000, 5000]  # 예시로 3개만
n = st.selectbox("숫자를 선택하세요", options)

if st.button("Compute", key="btn_no_cache"):
    start = time.time()
    result = expensive_computation1(n)
    elapsed = time.time() - start
    st.write(f"결과: {result}")
    st.write(f"소요 시간: {elapsed:.2f} 초")

st.write("같은 n 값이라도, Compute 누를 때마다 3초씩 기다립니다.")

st.markdown("-------")
st.markdown("### 캐싱 사용 예제")

@st.cache_data
def expensive_computation2(n):
    st.write(f"실제 계산 수행... (n={n})")
    time.sleep(3)  # 3초 대기 (연산 비용 시뮬레이션)
    return sum(i*i for i in range(n))

options = [1000, 3000, 5000]
n = st.selectbox("숫자를 선택하세요", options, key="1")

if st.button("Compute", key="btn_cache"):
    start = time.time()
    result = expensive_computation2(n)
    elapsed = time.time() - start
    st.write(f"결과: {result}")
    st.write(f"소요 시간: {elapsed:.2f} 초")

st.info("같은 n을 다시 선택해 Compute를 누르면, 이미 계산한 결과를 캐시에서 즉시 반환합니다!")