import streamlit as st

# 페이지의 타이틀을 설정합니다.
st.title('Streamlit 실슴')

# st.header("이것은 헤더입니다.")
# st.subheader("이것은 서브헤더입니다.")
st.markdown("제목 함수 `title` ")
st.markdown("헤더 함수 `header` ")
st.markdown("서브헤더 함수 `subheader` ")

st.markdown("--------")
st.markdown("### 마크다운 함수 `markdown` ")

st.markdown("**굵게** 혹은 *기울임* 할 수도 있어요.")

st.markdown("[Streamlit 공식 사이트](https://streamlit.io/)로 이동하기")

st.markdown("""
- :red[**빨간색 텍스트**]와 :blue[**파란색** 텍스트]  
- 이모지 💞도 넣어보자! 
""")

st.markdown("""
| 이름     | 직업     | 나이 |
|----------|----------|------|
| 홍길동   | 도적     | 25   |
| 김철수   | 개발자   | 30   |
| 이영희   | 디자이너 | 28   |
""")

st.markdown("--------")
st.markdown("### 텍스트 계열 함수")

st.caption("`caption` 이미지나 그래프의 주석을 달 때 유용합니다.")
st.text("`text` 간단히 텍스트만 표시합니다.")
st.write("`write` 변수를 출력에 사용합니다.")
st.write({"key": "value"})


st.markdown("--------")
st.markdown("### 코드 및 수식 표현")

st.markdown("#### **`code`** 코드 블록")
code_example = """
def hello_world():
    print("Hello World")
"""
st.code(code_example, language="python")

st.markdown("#### **`latex`** 수식 편집기")
st.latex(r"\frac{n!}{k!(n-k)!}")

st.markdown("--------")
st.markdown("### 텍스트 입력")

st.markdown("#### **`text_input`** 짧은 텍스트 입력 ")
user_name = st.text_input("이름을 입력하세요", placeholder="홍길동")
st.write(f"안녕하세요, {user_name} 님!")

st.markdown("#### **`text_area`** 긴 텍스트 입력 ")
user_memo = st.text_area("메모를 남겨주세요", height=100)
st.write("메모 내용:", user_memo)
st.markdown(f"메모 내용: *{user_memo}*")

st.markdown("--------")
st.markdown("### 수치/날짜 입력")

st.markdown("#### **`number_input`** 숫자 입력 ")
age = st.number_input("나이를 입력하세요", min_value=1, max_value=120, value=20)
st.write(f"당신의 나이는 {age}입니다.")

st.markdown("#### **`date_input`** 날짜 입력 ")
selected_date = st.date_input("날짜 선택")
st.write("선택한 날짜:", selected_date)

st.markdown("--------")
st.markdown("### 선택형 위젯")

st.markdown("#### **`selectbox`** 단일 선택 ")
fruit = st.selectbox("어떤 과일을 좋아하세요?", ["사과", "바나나", "딸기"])
st.write(f"선택한 과일은 {fruit}입니다.")

st.markdown("#### **`multiselect`** 복수 선택 ")
colors = st.multiselect("좋아하는 색을 골라보세요", ["빨강", "파랑", "초록", "노랑"], ["빨강"])
st.write("선택한 색상:", colors)

st.markdown("#### **`radio`** 라디오 버튼 ")
choice = st.radio(
    "어떤 동물을 좋아하세요?",
    ("고양이", "강아지", "코끼리")
)

st.write("당신이 선택한 동물은:", choice)
if choice == "고양이":
    st.write("🐱 야옹~")
elif choice == "강아지":
    st.write("🐶 멍멍!")
else:
    st.write("🐘 뿌우~")

st.markdown("--------")
st.markdown("### 파일 업로드 `file_uploader` ")

uploaded_file = st.file_uploader("CSV 파일을 업로드 해주세요", type=["csv"])
if uploaded_file is not None:
    st.write("업로드한 파일 이름:", uploaded_file.name)


#############################
st.markdown("--------")
st.markdown("### 버튼/슬라이더")

st.markdown("#### **`button`** 버튼 ")
if st.button("클릭"):
    st.write("버튼이 클릭되었습니다!")
import random

st.markdown("##### 🔮 오늘의 운세 뽑기")

if st.button("운세 뽑기"):
    fortunes = [
        "대박! 오늘은 황금 같은 기회가 온다!",
        "조심조심~ 길을 가다가 복이 굴러들어올 수도?!",
        "평탄한 하루! 큰 일은 없으나 작은 행복이 있을 예정!",
        "약간의 우울함이 스칠 수 있지만, 친구와 수다로 극복 가능!",
        "캠프 끝나고 여자친구가 생겨요!"
    ]
    result = random.choice(fortunes)
    st.markdown(f"**당신의 운세: {result}**")
else:
    st.markdown("💡 버튼을 눌러 당신의 오늘 운세를 확인해보세요!")

import random

st.markdown("##### 📝 닉네임 랜덤 생성기")

adj = ["멋진", "우아한", "화끈한", "엉뚱한", "귀여운"]
noun = ["고양이", "강아지", "코알라", "원숭이", "도마뱀"]

if st.button("닉네임 생성"):
    nickname = random.choice(adj) + " " + random.choice(noun)
    st.write(f"**당신의 새로운 닉네임은: {nickname}**")

st.markdown("#### **`slider`** 슬라이더 ")
val = st.slider("값을 선택하세요", 0, 100, 50)
st.write("현재 값:", val)

#############################
import pandas as pd
st.markdown("--------")
st.markdown("### 데이터 로딩 & 간단 전처리 예제")

# ❶ 파일 업로드 위젯 (csv, xlsx 등 허용)
uploaded_file = st.file_uploader(
    "분석할 CSV 또는 Excel 파일을 업로드하세요", 
    type=["csv", "xlsx"]
)

df = None

if uploaded_file is not None:
    # 파일 확장자에 따라 다른 함수로 읽습니다.
    if uploaded_file.name.endswith(".csv"):
        try:
            df = pd.read_csv(uploaded_file)
        except UnicodeDecodeError:
            df = pd.read_csv(uploaded_file, encoding="cp949")
            st.warning("UTF-8로 읽기 실패 → CP949로 읽었습니다.")
    elif uploaded_file.name.endswith(".xlsx"):
        df = pd.read_excel(uploaded_file)

    st.write("**원본 데이터 미리보기**")
    st.dataframe(df.head(), use_container_width=True)