import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# CSV 데이터 로드
@st.cache_data(show_spinner=False) # 캐싱
def load_data(csv_path="modified_manufacturing_dataset.csv"):
    df = pd.read_csv(csv_path, parse_dates=["Date"])
    return df

# ======================
### Main 
# ======================

st.image("main.png") # 메인 배너 
df = load_data()

# 월별 평균 계산
df["MonthStart"] = df["Date"].dt.to_period("M").dt.to_timestamp()
monthly_avg = (
    df.groupby("MonthStart")
    .agg(
        {
            "ProductionVolume": "mean",
            "QualityScore": "mean",
            "WorkerProductivity": "mean",
        }
    )
    .reset_index()
)


# 사이드바: 기간(연월) 선택 
df["YearMonth"] = (df["Date"].dt.year.astype(str) + "년 " + df["Date"].dt.month.astype(str) + "월")
available_yearmonths = df.sort_values("Date")["YearMonth"].unique()

with st.sidebar:
    selected_yearmonth = st.selectbox("기간 선택", available_yearmonths)

# 선택한 연/월 > 숫자로 변환 
parts = selected_yearmonth.split("년 ")
selected_year = int(parts[0])
selected_month = int(parts[1].replace("월", ""))
selected_month_start = pd.Timestamp(year=selected_year, month=selected_month, day=1)

# df_selected: 현재 기간 데이터
df_selected = df[df["YearMonth"] == selected_yearmonth].copy()
df_selected["DayOfWeek"] = df_selected["Date"].dt.day_name()

# df_prev: 이전 기간 데이터(전월) 가져오기
selected_index = list(available_yearmonths).index(selected_yearmonth)
if selected_index > 0:
    previous_yearmonth = list(available_yearmonths)[selected_index - 1]
    df_prev = df[df["YearMonth"] == previous_yearmonth]
else:
    previous_yearmonth = None
    df_prev = None

# =============================================================================
# KPI 1: 결함률 (DefectStatus)
# =============================================================================
with st.expander("결함률", expanded=True):
    st.header(f"결함률 ({selected_yearmonth})")

    # 현재 달 결함률 vs 전체 평균 vs 이전 달
    current_defect_rate = df_selected["DefectStatus"].mean() * 100
    overall_defect_rate = df["DefectStatus"].mean() * 100

    if df_prev is not None:
        previous_defect_rate = df_prev["DefectStatus"].mean() * 100 # 저번 달 평균 결함률
        delta_defect = current_defect_rate - previous_defect_rate # 결함률 변화량 
    else:
        delta_defect = 0

    col_defect1, col_defect2 = st.columns(2)
    with col_defect1:
        # st.metric: 숫자 + 증감 표시
        st.metric(
            label="",
            value=f"{current_defect_rate:.1f}%",
            delta=f"{delta_defect:+.1f}%",
        )
    with col_defect2:
        # 전체 평균 대비
        if current_defect_rate <= overall_defect_rate:
            st.info("결함률이 전체 평균 이하로 양호한 상태입니다.")
        else:
            st.error("결함률이 전체 평균 이상입니다. 개선이 필요합니다.")

col1, col2, col3 = st.columns(3)
# =============================================================================
# KPI 2: 생산량 (ProductionVolume)
# =============================================================================
with col1:
    with st.expander("", expanded=True):
        st.subheader(f"{selected_yearmonth} 생산량 KPI")

        # 전체 평균(목표치), 현재 평균, 이전 평균
        overall_target_pv = df["ProductionVolume"].mean()
        current_avg_pv = df_selected["ProductionVolume"].mean()
        if df_prev is not None:
            previous_avg_pv = df_prev["ProductionVolume"].mean()
        else:
            previous_avg_pv = None

        # 생산량 게이지 차트
        gauge_fig_pv = go.Figure(
            go.Indicator(
                mode="gauge+number+delta",
                value=current_avg_pv,
                delta=(
                    {"reference": previous_avg_pv}
                    if previous_avg_pv is not None
                    else {}
                ),
                gauge={
                    "axis": {"range": [0, overall_target_pv * 2]},
                    "bar": {"color": "blue"},
                    "steps": [
                        {"range": [0, overall_target_pv], "color": "lightgray"},
                        {
                            "range": [overall_target_pv, overall_target_pv * 2],
                            "color": "gray",
                        },
                    ],
                    "threshold": {
                        "line": {"color": "red", "width": 4},
                        "thickness": 0.75,
                        "value": overall_target_pv,
                    },
                },
                title={"text": f"목표: {overall_target_pv:.1f} units"},
            )
        )
        st.plotly_chart(gauge_fig_pv, use_container_width=True)

        # 이전 기간 대비 증감(metric)
        if previous_avg_pv is not None:
            delta_value_pv = current_avg_pv - previous_avg_pv
            arrow = "⬆️" if delta_value_pv >= 0 else "⬇️"
            st.metric(
                "전 기간 대비 변화",
                f"{current_avg_pv:.2f} units",
                f"{arrow} {delta_value_pv:+.2f} units",
            )
        else:
            st.write("이전 기간 데이터가 없습니다.")

        # (A) 월별 생산량 평균 라인 차트
        fig_line_pv = px.line(
            monthly_avg,
            x="MonthStart",
            y="ProductionVolume",
            title="월별 생산량 평균",
        )
        fig_line_pv.add_vline(
            x=selected_month_start, line_dash="dash", line_color="red"
        )
        st.plotly_chart(fig_line_pv, use_container_width=True)

        # (B) 생산량 분포 히스토그램
        hist_fig_pv = px.histogram(
            df_selected,
            x="ProductionVolume",
            nbins=20,
            title=f"{selected_yearmonth} 생산량 분포",
        )
        st.plotly_chart(hist_fig_pv, use_container_width=True)

        # (C) 생산량 vs 작업자 생산성 산점도
        scatter_fig_pv = px.scatter(
            df_selected,
            x="ProductionVolume",
            y="WorkerProductivity",
            color="QualityScore",
            title=f"{selected_yearmonth} 생산량 vs 작업자 생산성",
        )
        st.plotly_chart(scatter_fig_pv, use_container_width=True)

        # (D) 요일별 생산량 분포 박스 플롯
        box_fig_pv = px.box(
            df_selected,
            x="DayOfWeek",
            y="ProductionVolume",
            category_orders={
                "DayOfWeek": [
                    "Monday",
                    "Tuesday",
                    "Wednesday",
                    "Thursday",
                    "Friday",
                    "Saturday",
                    "Sunday",
                ]
            },
            title=f"{selected_yearmonth} 요일별 생산량 분포",
        )
        st.plotly_chart(box_fig_pv, use_container_width=True)

# =============================================================================
# KPI 3: 품질 검수
# =============================================================================
with col2:
    with st.expander("", expanded=True):
        st.subheader(f"{selected_yearmonth} 품질 점수 KPI")

        # 전체 평균(목표치), 현재 평균, 이전 평균
        overall_target_qs = df["QualityScore"].mean()
        current_avg_qs = df_selected["QualityScore"].mean()
        if df_prev is not None:
            previous_avg_qs = df_prev["QualityScore"].mean()
        else:
            previous_avg_qs = None

        # 품질 점수 게이지 차트
        gauge_fig_qs = go.Figure(
            go.Indicator(
                mode="gauge+number+delta",
                value=current_avg_qs,
                delta=(
                    {"reference": previous_avg_qs}
                    if previous_avg_qs is not None
                    else {}
                ),
                gauge={
                    "axis": {"range": [0, overall_target_qs * 1.5]},
                    "bar": {"color": "green"},
                    "steps": [
                        {"range": [0, overall_target_qs], "color": "lightgray"},
                        {
                            "range": [overall_target_qs, overall_target_qs * 1.5],
                            "color": "gray",
                        },
                    ],
                    "threshold": {
                        "line": {"color": "red", "width": 4},
                        "thickness": 0.75,
                        "value": overall_target_qs,
                    },
                },
                title={"text": f"목표: {overall_target_qs:.1f}%"},
            )
        )
        st.plotly_chart(gauge_fig_qs, use_container_width=True)

        # 이전 기간 대비 증감
        if previous_avg_qs is not None:
            delta_value_qs = current_avg_qs - previous_avg_qs
            arrow = "⬆️" if delta_value_qs >= 0 else "⬇️"
            st.metric(
                "전 기간 대비 변화",
                f"{current_avg_qs:.1f}%",
                f"{arrow} {delta_value_qs:+.2f}%",
            )
        else:
            st.write("이전 기간 데이터가 없습니다.")

        # (A) 월별 품질 점수 평균 라인 차트
        fig_line_qs = px.line(
            monthly_avg,
            x="MonthStart",
            y="QualityScore",
            title="월별 품질 점수 평균",
        )
        fig_line_qs.add_vline(
            x=selected_month_start, line_dash="dash", line_color="red"
        )
        st.plotly_chart(fig_line_qs, use_container_width=True)

        # (B) 품질 점수 분포 히스토그램
        hist_fig_qs = px.histogram(
            df_selected,
            x="QualityScore",
            nbins=20,
            title=f"{selected_yearmonth} 품질 점수 분포",
        )
        st.plotly_chart(hist_fig_qs, use_container_width=True)

        # (C) 품질 점수 vs 생산량 산점도
        scatter_fig_qs = px.scatter(
            df_selected,
            x="QualityScore",
            y="ProductionVolume",
            color="WorkerProductivity",
            title=f"{selected_yearmonth} 품질 점수 vs 생산량",
        )
        st.plotly_chart(scatter_fig_qs, use_container_width=True)

        # (D) 요일별 품질 점수 분포 박스 플롯
        box_fig_qs = px.box(
            df_selected,
            x="DayOfWeek",
            y="QualityScore",
            category_orders={
                "DayOfWeek": [
                    "Monday",
                    "Tuesday",
                    "Wednesday",
                    "Thursday",
                    "Friday",
                    "Saturday",
                    "Sunday",
                ]
            },
            title=f"{selected_yearmonth} 요일별 품질 점수 분포",
        )
        st.plotly_chart(box_fig_qs, use_container_width=True)

# =============================================================================
# KPI 4: 작업자 생산성 (WorkerProductivity)
# =============================================================================
with col3:
    with st.expander("", expanded=True):
        st.subheader(f"{selected_yearmonth} 작업자 생산성 KPI")

        # 전체 평균(목표치), 현재 평균, 이전 평균
        overall_target_wp = df["WorkerProductivity"].mean()
        current_avg_wp = df_selected["WorkerProductivity"].mean()
        if df_prev is not None:
            previous_avg_wp = df_prev["WorkerProductivity"].mean()
        else:
            previous_avg_wp = None

        # 작업자 생산성 게이지 차트
        gauge_fig_wp = go.Figure(
            go.Indicator(
                mode="gauge+number+delta",
                value=current_avg_wp,
                delta=(
                    {"reference": previous_avg_wp}
                    if previous_avg_wp is not None
                    else {}
                ),
                gauge={
                    "axis": {"range": [0, overall_target_wp * 1.5]},
                    "bar": {"color": "orange"},
                    "steps": [
                        {"range": [0, overall_target_wp], "color": "lightgray"},
                        {
                            "range": [overall_target_wp, overall_target_wp * 1.5],
                            "color": "gray",
                        },
                    ],
                    "threshold": {
                        "line": {"color": "red", "width": 4},
                        "thickness": 0.75,
                        "value": overall_target_wp,
                    },
                },
                title={"text": f"목표: {overall_target_wp:.1f}%"},
            )
        )
        st.plotly_chart(gauge_fig_wp, use_container_width=True)

        # 이전 기간 대비 증감
        if previous_avg_wp is not None:
            delta_value_wp = current_avg_wp - previous_avg_wp
            arrow = "⬆️" if delta_value_wp >= 0 else "⬇️"
            st.metric(
                "전 기간 대비 변화",
                f"{current_avg_wp:.1f}%",
                f"{arrow} {delta_value_wp:+.2f}%",
            )
        else:
            st.write("이전 기간 데이터가 없습니다.")

        # (A) 월별 작업자 생산성 평균 라인 차트
        fig_line_wp = px.line(
            monthly_avg,
            x="MonthStart",
            y="WorkerProductivity",
            title="월별 작업자 생산성 평균",
        )
        fig_line_wp.add_vline(
            x=selected_month_start, line_dash="dash", line_color="red"
        )
        st.plotly_chart(fig_line_wp, use_container_width=True)

        # (B) 작업자 생산성 분포 히스토그램
        hist_fig_wp = px.histogram(
            df_selected,
            x="WorkerProductivity",
            nbins=20,
            title=f"{selected_yearmonth} 작업자 생산성 분포",
        )
        st.plotly_chart(hist_fig_wp, use_container_width=True)

        # (C) 작업자 생산성 vs 품질 점수 산점도
        scatter_fig_wp = px.scatter(
            df_selected,
            x="WorkerProductivity",
            y="QualityScore",
            color="ProductionVolume",
            title=f"{selected_yearmonth} 작업자 생산성 vs 품질 점수",
        )
        st.plotly_chart(scatter_fig_wp, use_container_width=True)

        # (D) 요일별 작업자 생산성 분포 박스 플롯
        box_fig_wp = px.box(
            df_selected,
            x="DayOfWeek",
            y="WorkerProductivity",
            category_orders={
                "DayOfWeek": [
                    "Monday",
                    "Tuesday",
                    "Wednesday",
                    "Thursday",
                    "Friday",
                    "Saturday",
                    "Sunday",
                ]
            },
            title=f"{selected_yearmonth} 요일별 작업자 생산성 분포",
        )
        st.plotly_chart(box_fig_wp, use_container_width=True)

