import streamlit as st
import pandas as pd
import numpy as np
import urllib.request
import re
import os 
import pickle
from konlpy.tag import Komoran
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

if "JAVA_HOME" not in os.environ:
    os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-17-openjdk-amd64"
    
# 앱 전체 페이지 타이틀, 레이아웃 설정
st.set_page_config(page_title="Steam 감성 분석", layout="wide")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# --- 캐싱: 모델, 토크나이저, 데이터셋 로드 (최초 1회만 실행) ---
@st.cache_resource
def load_assets():
    """모델, 토크나이저, 데이터셋을 로드하고 캐싱합니다."""
    try:
        model_path = os.path.join(BASE_DIR, "sentiment_model.h5")
        tokenizer_path = os.path.join(BASE_DIR, "tokenizer.pickle")

        model = load_model(model_path)
        with open(tokenizer_path, "rb") as handle:
            tokenizer = pickle.load(handle)

        # Steam 리뷰 데이터 다운로드 및 로드
        try:
            file_path = os.path.join(BASE_DIR, "steam.txt")

            urllib.request.urlretrieve(
                "https://raw.githubusercontent.com/bab2min/corpus/master/sentiment/steam.txt",
                filename=file_path,
            )
            data = pd.read_table(file_path, names=["label", "reviews"])
            data.drop_duplicates(subset=["reviews"], inplace=True)
            data["reviews"].replace("", np.nan, inplace=True)
            data = data.dropna(how="any")
            data["label_text"] = data["label"].apply(
                lambda x: "긍정 (Positive)" if x == 1 else "부정 (Negative)"
            )
        except Exception as e:
            st.error(f"데이터 로드 중 오류 발생: {e}")
            data = pd.DataFrame({"label": [], "reviews": [], "label_text": []})

        return model, tokenizer, data
    except FileNotFoundError:
        st.error(
            "모델 파일(sentiment_model.h5) 또는 토크나이저 파일(tokenizer.pickle)을 찾을 수 없습니다. 모델 학습 코드를 먼저 실행하고 파일을 업로드해주세요."
        )
        st.stop()
    except Exception as e:
        st.error(f"자산 로드 중 예상치 못한 오류 발생: {e}")
        st.stop()

# --- 전역 변수 및 예측 함수 설정 ---
model, tokenizer, steam_data = load_assets()
komoran = Komoran()
stopwords = [
    "도", "는", "다", "의", "가", "이", "은", "한", "에", "하", "고", "을", "를",
    "인", "듯", "과", "와", "네", "들", "듯", "지", "임", "게", "만", "게임", "겜",
    "되", "음", "면",
]
max_len = 60

def clean_text(text):
    text = re.sub(r"[^ㄱ-ㅎㅏ-ㅣ가-힣 ]", "", text)
    return text

def sentiment_predict(new_sentence: str):
    """새로운 문장의 감성을 예측하고 확률을 반환하는 함수"""
    cleaned_sentence = clean_text(new_sentence)
    tokenized_sentence = komoran.morphs(cleaned_sentence)
    tokenized_sentence = [word for word in tokenized_sentence if word not in stopwords]
    if not tokenized_sentence:
        return 0.5, "중립 (Neutral)"

    encoded = tokenizer.texts_to_sequences([tokenized_sentence])
    pad_new = pad_sequences(encoded, maxlen=max_len)
    score = float(model.predict(pad_new)[0][0])
    sentiment = "긍정 (Positive)" if score > 0.5 else "부정 (Negative)"
    return score, sentiment

# --- 감성 물결 배너 애니메이션 CSS/HTML 함수 ---
def sentiment_wave_banner(score):
    """
    분석 결과에 따라 물결 배너 애니메이션 효과를 추가합니다.
    """
    sentiment_type = "긍정 (Positive)" if score > 0.5 else "부정 (Negative)"

    if sentiment_type == "긍정 (Positive)":
        color1 = "#4CAF50" # 밝은 녹색
        color2 = "#81C784" # 연한 녹색
        text_color = "white"
        title = f"긍정 (Positive) {score*100:.2f}%"
        icon = "😊"
    else: # 부정 (Negative)
        color1 = "#E57373" # 연한 빨간색
        color2 = "#F44336" # 밝은 빨간색
        text_color = "white"
        title = f"부정 (Negative) {(1-score)*100:.2f}%"
        icon = "😞"

    wave_path1 = "M0,70 C150,120 350,-20 500,70 C650,160 850,20 1000,70 L1000,100 L0,100 Z"
    wave_path2 = "M0,50 C150,100 350,0 500,50 C650,100 850,0 1000,50 L1000,100 L0,100 Z"
    wave_path3 = "M0,60 C150,110 350,30 500,80 C650,130 850,50 1000,90 L1000,100 L0,100 Z"

    st.markdown(
        f"""
        <style>
            @keyframes wave-1 {{
                0% {{ transform: translateX(0); }}
                100% {{ transform: translateX(-50%); }}
            }}
            @keyframes wave-2 {{
                0% {{ transform: translateX(-50%); }}
                100% {{ transform: translateX(0); }}
            }}
            @keyframes wave-3 {{
                0% {{ transform: translateX(-25%); }}
                100% {{ transform: translateX(-75%); }}
            }}
            .wave-banner {{
                position: relative;
                width: 100%;
                height: 150px;
                border-radius: 10px;
                overflow: hidden;
                box-shadow: 0 4px 12px rgba(0,0,0,0.1);
                margin-bottom: 20px;
                display: flex;
                justify-content: center;
                align-items: center;
                text-align: center;
                background: linear-gradient(to right, {color1}, {color2});
            }}
            .wave-container {{
                position: absolute;
                width: 100%;
                height: 100%;
                bottom: 0;
                left: 0;
                opacity: 0.8;
                overflow: hidden;
            }}
            .wave {{
                position: absolute;
                width: 200%;
                height: 100%;
                bottom: -20px;
                background-repeat: repeat-x;
                opacity: 0.8;
            }}
            .wave-1 {{
                background-image: url('data:image/svg+xml;utf8,<svg viewBox="0 0 1000 100" xmlns="http://www.w3.org/2000/svg"><path fill="rgba(255,255,255,0.2)" d="{wave_path1}" /></svg>');
                animation: wave-1 10s linear infinite;
                z-index: 3;
            }}
            .wave-2 {{
                background-image: url('data:image/svg+xml;utf8,<svg viewBox="0 0 1000 100" xmlns="http://www.w3.org/2000/svg"><path fill="rgba(255,255,255,0.3)" d="{wave_path2}" /></svg>');
                animation: wave-2 15s linear infinite;
                z-index: 2;
            }}
            .wave-3 {{
                background-image: url('data:image/svg+xml;utf8,<svg viewBox="0 0 1000 100" xmlns="http://www.w3.org/2000/svg"><path fill="rgba(255,255,255,0.4)" d="{wave_path3}" /></svg>');
                animation: wave-3 20s linear infinite;
                z-index: 1;
            }}
            .banner-content {{
                position: relative;
                z-index: 10;
                color: {text_color};
                font-size: 2.5rem;
                font-weight: bold;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
            }}
        </style>
        <div class="wave-banner">
            <div class="wave-container">
                <div class="wave wave-1"></div>
                <div class="wave wave-2"></div>
                <div class="wave wave-3"></div>
            </div>
            <div class="banner-content">
                {title} {icon}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# 페이지 리스트 정의
pages = [
    st.Page("page1.py", title="대시보드", icon="📊", default=True),
    st.Page("page2.py", title="감성분석 테스트", icon="🤖"),
]

# 페이지 네비게이션 생성 및 실행
pg = st.navigation(pages)
pg.run()
