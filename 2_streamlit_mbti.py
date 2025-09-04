import streamlit as st
import random

questions = [
    ("오랜만의 휴가! 오늘 하루는...", [("'이불 밖은 위험해!' 뒹굴거리며 방콕 즐기기! 🏡", "I"), ("'놀자! 오늘을 즐겨야 해!' 친구들 만나러 외출! 🎉", "E")]),
    ("새로운 사람들과 함께하는 파티에 간다면...", [("새로운 사람들이 너무 많다... 아는 사람 옆에 붙어 조용히 이야기 나눠요 🤫", "I"), ("오늘 처음 봤지만 우리는 모두 친구! 먼저 다가가 인사해요 🙋", "E")]),
    ("새로운 재미있는 프로젝트 주제에 관심이 생겼을 때, 나는...", [("사공이 많으면 배가 산으로 간다! 일단은 혼자서 시작 😎", "I"), ("'우리 같이 프로젝트 할래?' 팀원부터 구하며 시작! 🗣️", "E")]),
    ("다음 주말 계획을 세울 때...", [("'이번에는 맛집 도장 깨기다!' 구체적인 장소, 후기 다 찾아본다! 🔍", "S"), ("'어디든 가보자!' 장소 정했으니 다 정한 거지~ 🖼️", "N")]),
    ("어려운 문제가 생겼을 때, 나는...", [("'예전에 이렇게 했었지?' 과거의 경험을 되짚어보며 차근차근 해결! 👣", "S"), ("'이 방법은 어떨까?' 번뜩이는 아이디어로 새로운 해결법 시도! ✨", "N")]),
    ("아직 아무도 모르는 새로운 게임을 배울 때, 나는...", [("'설명서부터 꼼꼼히 읽어봐야지!' 매뉴얼을 정독하며 기본부터 익히는 편! 📚", "S"), ("'일단 해보자!' 이것저것 눌러보면서 감으로 배우는 편! 🕹️", "N")]),
    ("친구가 고민을 털어놓을 때, 내 반응은...", [("'이건 이렇게 하는 게 효율적이야!' 해결 방법을 냉정하게 분석해서 조언해줘요! 🧐", "T"), ("'힘들었겠다, 괜찮아?' 친구의 기분에 공감하며 먼저 안아주는 편! 🤗", "F")]),
    ("중요한 결정을 내려야 할 때, 내 우선순위는...", [("'어떤 선택이 가장 합리적일까?' 논리적으로 따져보고 결과를 생각해요! 🧠", "T"), ("이걸 선택하면 모두가 행복할까?' 사람들의 마음과 관계를 먼저 생각해요! ❤️", "F")]),
    ("팀원들과 의견 충돌이 생겼을 때, 나는...", [("'팩트는 이렇고, 원칙대로 가자!' 객관적인 사실을 중심으로 냉철하게 판단! 🧊", "T"), ("'다들 기분 상하지 않게 잘 해결해 보자!' 모두가 만족할 수 있는 방법을 찾으려 노력! 🤝", "F")]),
    ("신나는 여행을 떠날 때, 내 계획은...", [("'일단 가자! 가서 생각하면 되지!' 즉흥적인 여행을 즐기는 편! 🗺️", "P"), ("'숙소, 맛집, 이동 경로까지 완벽하게!' 모든 걸 미리 계획해야 마음이 편해요! 📝", "J")]),
    ("마감일이 다가올 때, 내 모습은...", [("'마감 직전에 하면 집중이 잘 돼!' 여유를 부리다 마지막에 몰아서 끝내는 편! 🏃‍♀️", "P"), ("'미리미리 해야 안심이 되지!' 계획적으로 차근차근 해내서 미리 완료! ⏰", "J")]),
    ("새로운 도전을 시작할 때, 나는...", [("'일단 해보면서 만들어가자!' 시작하면서 방향을 잡고 정리하는 편! 🤸‍♀️", "P"), ("'시작 전에 계획부터 완벽하게!' 완벽한 준비가 되어야 시작할 수 있어요! ✍️", "J")])
]
mbti_descriptions = {
    "ISTJ": "📚 논리적이고 책임감 강한 집콕러! 은근히 웃긴 드립으로 주변을 놀라게 해줄 때가 있어요.",
    "ISFJ": "🧸 따뜻하고 배려심 많은 힐링러! 무뚝뚝해 보여도 속은 마시멜로처럼 폭신폭신.",
    "INFJ": "☕ 이상주의적 감성러! 가끔 세계 평화를 꿈꾸면서 티 한 잔으로 힐링하곤 합니다.",
    "INTJ": "🗂️ 분석적이고 독립적인 전략가! 남들 눈치 안 보고, 자기 길을 똑부러지게 가죠.",
    "ISTP": "🛠️ 즉흥적이고 손재주 좋은 똑쟁이! 뜯어보고, 고치고, 만드는 걸 좋아해요.",
    "ISFP": "🎨 감성적이고 온화한 예술가! 말보단 그림, 사진, 음악으로 마음을 표현해요.",
    "INFP": "🌙 공감 능력 최강인 몽상가! 상상 속 나라에서 휴가 보내는 걸 좋아할지도?",
    "INTP": "💡 지적인 호기심에 불타는 아이디어 뱅크! 답정너 대화는 질색이랍니다.",
    "ESTP": "🎢 신나는 모험을 즐기는 분위기 메이커! 즉흥 여행이나 파티에 최적화된 타입.",
    "ESFP": "🎤 파티의 주인공, 천상 연예인! 밝은 에너지가 주변 사람들에게 전염됩니다.",
    "ENFP": "🔥 열정이 펄펄 끓는 창의적 아이디어 뱅크! 집콕은 상상만 해도 기운 빠질지도?",
    "ENTP": "🧩 논쟁을 즐기는 발명가! 토론을 좋아하는, 날카로운 사고력의 소유자.",
    "ESTJ": "📋 조직적이고 추진력 있는 리더! BUT 예상 못 한 일정 변경엔 식겁할 수도 있죠.",
    "ESFJ": "🤝 사교적이고 섬세한 케어왕! 사람 사이의 균형을 맞추는 데 타고난 능력이 있어요.",
    "ENFJ": "🌟 타인의 성장을 돕고 싶은 열정가! 흥이 오르면 파티 주최자가 되어버리기도!",
    "ENTJ": "💼 결단력 있고 카리스마 넘치는 CEO형! 맡은 바를 모조리 해결해야 직성이 풀려요."
}
mbti_weaknesses = {
    "ISTJ": "😅 융통성이 부족할 때가 있고, 변화에 대한 거부감이 있을 수 있어요.",
    "ISFJ": "🙈 자기주장을 잘 못해서 스트레스를 쌓아두기 쉽습니다.",
    "INFJ": "🌫️ 지나치게 이상주의적이라 현실과 타협이 어려울 수 있습니다.",
    "INTJ": "🙃 독립적이지만 때로는 고집이 세고 대인관계 스킬이 부족할 수 있어요.",
    "ISTP": "🤐 감정표현이 서툴러 주변 사람들이 속마음을 알기 어려울 수 있어요.",
    "ISFP": "🙃 자신만의 공간을 지나치게 중시하여 협업이 어려울 수 있습니다.",
    "INFP": "☁️ 현실적 문제를 회피하고, 상상 속에만 머무를 때가 있어요.",
    "INTP": "🤓 지적 논쟁을 좋아하지만, 공감 능력이 부족해 보일 수 있어요.",
    "ESTP": "⚡ 충동적이고 계획 없이 움직여서 주변을 당황하게 만들 수 있어요.",
    "ESFP": "🌀 지나치게 즉흥적이라 장기적 계획이나 목표 설정이 어려울 수 있어요.",
    "ENFP": "🌪️ 한 가지에 집중하기보다는 너무 많은 아이디어만 내놓고 끝낼 수 있어요.",
    "ENTP": "🙊 논쟁을 즐겨서 상대를 피곤하게 만들거나 감정 상하게 할 수 있어요.",
    "ESTJ": "📏 과도한 통제력을 발휘하려 할 수 있고, 융통성이 떨어질 수 있어요.",
    "ESFJ": "😇 타인의 평가에 예민해져서 자신을 지나치게 희생할 수 있어요.",
    "ENFJ": "🔥 과도한 책임감에 스스로를 몰아세우고 지쳐버릴 때가 있어요.",
    "ENTJ": "😤 때로는 권위적이고 독단적으로 보일 수 있으며 완벽주의 경향이 있어요."
}

# 페이지 레이아웃
st.set_page_config(page_title="3분 MBTI 테스트", page_icon="🌸", layout="centered")

# 파스텔톤 CSS
st.markdown(
    """
    <style>
    body {
        background-color: #fffdfc;
    }
    .question-card {
        background: #fff7fa;
        padding: 20px;
        border-radius: 20px;
        margin-bottom: 20px;
        border: 2px dashed #ffccd5;
    }
    .stButton > button {
        background: #fffbfe;
        border: none;
        padding: 10px 22px;
        border-radius: 20px;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton > button:hover {
        transform: scale(1.05);
    }
    </style>
    """,
    unsafe_allow_html=True
)


# 세션 상태 초기화
if "answers" not in st.session_state:
    st.session_state.answers = {}
if "questions_shuffled" not in st.session_state:
    st.session_state.questions_shuffled = random.sample(range(len(questions)), len(questions))

# 헤더 섹션
st.title("💖 3분 MBTI 테스트 💖")
st.markdown("나도 몰랐던 내 진짜 성격은? 🤔 아래 질문에 솔직하게 답해주세요!")
st.write("---")

# 진행 상황 바
progress_percent = len(st.session_state.answers) / len(questions) if questions else 0
st.progress(progress_percent, text=f"**진행도:** {len(st.session_state.answers)} / {len(questions)}")
st.write("---")

# 질문 섹션
no = 1
for i in st.session_state.questions_shuffled:
    q, opts = questions[i]
    st.markdown(f"<div class='question-card'><b>Q{no}. {q}</b></div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        choice1_text, choice1_indicator = opts[0]
        st.button(choice1_text, key=f"q{i}_btn1", on_click=lambda i=i, indicator=choice1_indicator: st.session_state.answers.update({i: indicator}), use_container_width=True)

    with col2:
        choice2_text, choice2_indicator = opts[1]
        st.button(choice2_text, key=f"q{i}_btn2", on_click=lambda i=i, indicator=choice2_indicator: st.session_state.answers.update({i: indicator}), use_container_width=True)

    if i in st.session_state.answers:
        st.markdown(f"<p style='color: #4CAF50;'>✅선택 완료!</p>", unsafe_allow_html=True)
    st.write("---")
    no += 1


progress_percent = len(st.session_state.answers) / len(questions) if questions else 0
st.progress(progress_percent, text=f"**진행도:** {len(st.session_state.answers)} / {len(questions)}")
st.write("---")

# 결과 보기 버튼 및 초기화 버튼
col_btn1, col_btn2 = st.columns(2)
with col_btn1:
    res = st.button("결과 보기", use_container_width=True, help="결과 보기")

with col_btn2:
    # 테스트 다시 시작 버튼
    if st.button("테스트 다시 시작", use_container_width=True, help="테스트 다시 시작"):
        st.session_state.answers = {}
        st.session_state.questions_shuffled = random.sample(range(len(questions)), len(questions))
        st.rerun() 

if res:
        if len(st.session_state.answers) < len(questions):
            st.warning("앗! 모든 질문에 답해야 결과를 볼 수 있어요! 😅")
        else:
            st.balloons()
            counts = {k: 0 for k in ["I", "E", "S", "N", "T", "F", "P", "J"]}
            for v in st.session_state.answers.values():
                counts[v] += 1
            
            mbti = ""
            mbti += "I" if counts["I"] >= counts["E"] else "E"
            mbti += "S" if counts["S"] >= counts["N"] else "N"
            mbti += "T" if counts["T"] >= counts["F"] else "F"
            mbti += "P" if counts["P"] >= counts["J"] else "J"
            
            st.markdown(f"<h3 style='text-align: center;'>🎉 당신의 MBTI는... <strong style='color: #FF69B4;'>{mbti}</strong> 입니다! 🎉</h3>", unsafe_allow_html=True)
            st.write("---")
            
            st.subheader("💡 당신의 매력 포인트는?")
            st.info(mbti_descriptions[mbti])
            
            st.subheader("⚠️ 이런 점은 조심하면 더 좋아요!")
            st.warning(mbti_weaknesses[mbti])