import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import pickle

@st.cache_data(show_spinner=False)
def load_data(csv_path="modified_manufacturing_dataset.csv"):
    df = pd.read_csv(csv_path)
    return df

@st.cache_data(show_spinner=False)
def load_model(model_path="rf_top4_model.pkl"):
    """
    pickle 형태로 저장된 학습 모델을 불러와 캐싱합니다.
    """
    with open(model_path, "rb") as f:
        model = pickle.load(f)
    return model

### Main 공간 ###
st.title("머신러닝 예측 및 EDA")

df = load_data()
model = load_model()

# 각 컬럼별 기본 통계값(최소, 최대, 중앙값) 추출 함수
def get_range_info(dataframe, col):
    return {
        "min": float(dataframe[col].min()),
        "max": float(dataframe[col].max()),
        "median": float(dataframe[col].median()),
    }

stockout_info = get_range_info(df, "StockoutRate")
cost_info = get_range_info(df, "ProductionCost")
process_time_info = get_range_info(df, "AdditiveProcessTime")
volume_info = get_range_info(df, "ProductionVolume")

# 예측에 필요한 입력 받기
st.header("모델 기반 결함 예측")
with st.form("prediction_form"):
    st.write("예측에 필요한 입력 데이터를 작성하세요.")

    stockout_rate = st.number_input(
        "재고 품절률 (StockoutRate, %)",
        min_value=round(stockout_info["min"], 2),
        max_value=round(stockout_info["max"], 2),
        value=round(stockout_info["median"], 2),
        step=0.1,
    )

    production_cost = st.slider(
        "제조 비용 (ProductionCost, $)",
        min_value=round(cost_info["min"], 2),
        max_value=round(cost_info["max"], 2),
        value=round(cost_info["median"], 2),
        step=1.0,
    )

    additive_process_time = st.slider(
        "적층 공정 시간 (AdditiveProcessTime, hours)",
        min_value=round(process_time_info["min"], 2),
        max_value=round(process_time_info["max"], 2),
        value=round(process_time_info["median"], 2),
        step=0.5,
    )

    production_volume = st.slider(
        "생산량 (ProductionVolume)",
        min_value=int(volume_info["min"]),
        max_value=int(volume_info["max"]),
        value=int(volume_info["median"]),
        step=50,
    )

    submitted = st.form_submit_button("예측 실행")

# 예측 결과
if submitted:
    # 입력값
    input_data = {
        "StockoutRate": [stockout_rate],
        "ProductionCost": [production_cost],
        "AdditiveProcessTime": [additive_process_time],
        "ProductionVolume": [production_volume],
    }
    features_df = pd.DataFrame(input_data)

    # 모델 예측 (0: 낮은 결함, 1: 높은 결함)
    prediction = model.predict(features_df)[0]
    probability = model.predict_proba(features_df)[0][prediction]

    if prediction == 0:
        st.success(f"예측 결과: 낮은 결함 발생 (확률: {probability:.2f})")
    else:
        st.error(f"예측 결과: 높은 결함 발생 (확률: {probability:.2f})")

    # 입력값 분포 시각화
    st.header("입력값 분포 확인")
    for col, val_list in input_data.items():
        user_val = val_list[0]
        if col in df.columns:
            fig = px.histogram(df, x=col, nbins=20, title=f"{col} 분포")
            fig.add_vline(x=user_val, line_width=3, line_dash="dash", line_color="red")
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning(f"데이터셋에 '{col}' 컬럼이 없어 시각화를 표시할 수 없습니다.")