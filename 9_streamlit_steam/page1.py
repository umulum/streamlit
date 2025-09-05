import streamlit as st
import plotly.express as px
from app import sentiment_wave_banner, steam_data # app.py에서 함수와 데이터를 불러옵니다.

def show_dashboard():
    st.title("Steam 게임 리뷰 감성 분석 대시보드 🎮")
    st.write("---")
    st.markdown("""이 대시보드는 Streamlit을 활용하여 Steam 게임 리뷰 데이터의 **감성 분포**를 시각화합니다.""")

    st.subheader("데이터 요약")
    col1, col2 = st.columns(2)
    total_reviews = len(steam_data)
    positive_count = steam_data["label"].sum()
    negative_count = total_reviews - positive_count
    with col1:
        st.metric("총 리뷰 수", f"{total_reviews:,} 개")
    with col2:
        st.metric(
            "긍정 리뷰",
            f"{positive_count:,} 개",
            delta=f"부정 리뷰 대비 {positive_count / negative_count:.2f}배",
        )

    st.subheader("리뷰 감성 분포")
    label_counts = steam_data["label_text"].value_counts().reset_index()
    label_counts.columns = ["label_text", "count"]

    # 긍정/부정에 따른 색상 매핑
    color_map = {"긍정 (Positive)": "#81C784", "부정 (Negative)": "#E57373"}

    fig_pie = px.pie(
        label_counts,
        names="label_text",
        values="count",
        title="Steam 리뷰 감성 분포",
        color="label_text",
        color_discrete_map=color_map,
    )
    st.plotly_chart(fig_pie, use_container_width=True)

    st.subheader("리뷰 길이 분포")
    steam_data["review_length"] = steam_data["reviews"].apply(lambda x: len(x.split()))
    fig_hist = px.histogram(
        steam_data,
        x="review_length",
        color="label_text",
        title="리뷰 길이 분포 (단어 수 기준)",
        barmode="overlay",
        nbins=50,
        color_discrete_map=color_map, # 히스토그램에도 색상 매핑 적용
    )
    st.plotly_chart(fig_hist, use_container_width=True)

    st.subheader("긍정/부정 리뷰 샘플")
    col_pos, col_neg = st.columns(2)
    with col_pos:
        st.markdown("### 긍정 리뷰 😃")
        positive_samples = steam_data[steam_data["label"] == 1].sample(5, random_state=42)
        for review in positive_samples["reviews"]:
            st.markdown(f"> **_'{review}'_**")
    with col_neg:
        st.markdown("### 부정 리뷰 😡")
        negative_samples = steam_data[steam_data["label"] == 0].sample(5, random_state=42)
        for review in negative_samples["reviews"]:
            st.markdown(f"> **_'{review}'_**")

if __name__ == "__main__":
    show_dashboard()