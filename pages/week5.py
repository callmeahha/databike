import streamlit as st
import pandas as pd
import plotly.express as px

# 페이지 설정
st.set_page_config(layout="wide", page_title="5차시: 데이터 분석 정리하기")
# 네비게이션 버튼
col1, col2, col3 = st.columns([1,3,1])
with col1:
    if st.button('⬅️ 이전 차시'):
        st.switch_page("pages/week4.py")
with col3:
    if st.button('처음으로 ➡️'):
        st.switch_page("app.py")

# CSS 스타일 추가
st.markdown("""
    <style>
        .title {
            color: #FF6B6B;
            text-align: center;
            padding: 20px;
            font-size: 2.8em;
            font-weight: bold;
            background: linear-gradient(120deg, #FFE5E5 0%, #FFF0F0 100%);
            border-radius: 15px;
            margin-bottom: 20px;
        }
        .subtitle {
            text-align: center;
            color: #666;
            font-size: 1.2em;
            margin-bottom: 30px;
        }
        .objective-box {
            background-color: #E3F2FD;
            padding: 20px;
            border-radius: 10px;
            margin: 10px 0;
        }
        .evaluation-box {
            background-color: #F5F5F5;
            padding: 15px;
            border-radius: 10px;
            margin: 10px 0;
            border-left: 5px solid #FF6B6B;
        }
        .summary-box {
            background-color: #E8F5E9;
            padding: 20px;
            border-radius: 10px;
            margin: 15px 0;
        }
    </style>
""", unsafe_allow_html=True)

# 타이틀
st.markdown('<h1 class="title">🎓 5차시: 우리의 데이터 분석 여정 정리하기</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">지금까지 배운 내용을 돌아보고 정리해보아요! 📝</p>', unsafe_allow_html=True)

# 학습 목표 확인
st.markdown("""
    <div class="objective-box">
        <h3>📚 학습 목표</h3>
        <ol>
            <li>실생활 데이터의 디지털 활용 가치 이해하기</li>
            <li>목적에 맞는 데이터 수집과 관리</li>
            <li>데이터의 다양한 시각화 방법 이해</li>
            <li>데이터 기반 의미 해석</li>
            <li>데이터를 활용한 융합적 문제 해결</li>
        </ol>
    </div>
""", unsafe_allow_html=True)

# 자기 평가 섹션
st.markdown("### 📊 나의 학습 성취도 체크")

# 학습 목표별 이해도 체크
understanding_levels = {
    "실생활 데이터의 디지털 활용 가치를 이해했나요?": 0,
    "목적에 맞는 데이터를 수집하고 관리할 수 있나요?": 0,
    "데이터를 다양한 형태로 시각화할 수 있나요?": 0,
    "데이터를 기반으로 의미를 해석할 수 있나요?": 0,
    "데이터를 활용해 문제를 해결할 수 있나요?": 0
}

for question in understanding_levels.keys():
    understanding_levels[question] = st.slider(
        question,
        min_value=1,
        max_value=5,
        value=3,
        help="1: 전혀 못함, 5: 매우 잘함"
    )

# 이해도 시각화
understanding_df = pd.DataFrame({
    '학습 목표': list(understanding_levels.keys()),
    '이해도': list(understanding_levels.values())
})

fig = px.bar(understanding_df, 
            x='이해도', 
            y='학습 목표',
            orientation='h',
            title='나의 학습 목표 달성도')

st.plotly_chart(fig, use_container_width=True)

# 학습 내용 확인 퀴즈
st.markdown("### ✍️ 학습 내용 확인하기")

# 퀴즈 1
st.markdown("""
    <div class="evaluation-box">
        <h4>1. 데이터 분석의 가치</h4>
    </div>
""", unsafe_allow_html=True)

q1 = st.radio(
    "따릉이 데이터 분석을 통해 알 수 있는 가장 중요한 정보는 무엇일까요?",
    ["자전거의 수명", "이용자들의 패턴과 필요", "자전거의 가격", "날씨 정보"]
)

if st.button('정답 확인 1'):
    if q1 == "이용자들의 패턴과 필요":
        st.success("정답입니다! 데이터 분석을 통해 사용자들의 필요와 패턴을 파악할 수 있어요.")
    else:
        st.error("다시 생각해보세요. 데이터 분석의 주요 목적은 무엇일까요?")

# 퀴즈 2
st.markdown("""
    <div class="evaluation-box">
        <h4>2. 데이터 시각화의 중요성</h4>
    </div>
""", unsafe_allow_html=True)

q2 = st.radio(
    "데이터 시각화가 중요한 이유는 무엇인가요?",
    ["단순히 예쁘게 보이기 위해",
     "복잡한 데이터를 이해하기 쉽게 표현하기 위해",
     "컴퓨터 활용 능력을 보여주기 위해",
     "최신 트렌드를 따르기 위해"]
)

if st.button('정답 확인 2'):
    if q2 == "복잡한 데이터를 이해하기 쉽게 표현하기 위해":
        st.success("정답입니다! 시각화는 복잡한 데이터를 쉽게 이해할 수 있게 도와줍니다.")
    else:
        st.error("다시 생각해보세요. 시각화의 주요 목적은 무엇일까요?")

# 퀴즈 3
st.markdown("""
    <div class="evaluation-box">
        <h4>3. 데이터 기반 의사결정</h4>
    </div>
""", unsafe_allow_html=True)

q3 = st.radio(
    "새로운 따릉이 대여소 위치를 정할 때 가장 중요한 데이터는 무엇일까요?",
    ["자전거 색상에 대한 선호도",
     "이용자의 연령대",
     "주변 지역의 이용 패턴과 수요",
     "자전거 브랜드 선호도"]
)

if st.button('정답 확인 3'):
    if q3 == "주변 지역의 이용 패턴과 수요":
        st.success("정답입니다! 실제 이용 패턴과 수요를 분석하는 것이 가장 중요해요.")
    else:
        st.error("다시 생각해보세요. 위치 선정에 가장 중요한 정보는 무엇일까요?")

# 최종 소감 작성
st.markdown("### 💭 나의 데이터 분석 여정 정리하기")
st.text_area("이번 수업을 통해 배운 점과 느낀 점을 자유롭게 적어보세요.", height=150)

if st.button("제출하기"):
    st.balloons()
    st.success("수고하셨습니다! 여러분은 이제 데이터 분석 전문가입니다! 🎉")

# 학습 정리
st.markdown("""
    <div class="summary-box">
        <h3>🎯 핵심 정리</h3>
        <ul>
            <li>데이터는 우리 주변의 다양한 현상을 이해하는 데 도움을 줍니다.</li>
            <li>목적에 맞는 데이터 수집과 분석이 중요합니다.</li>
            <li>시각화는 데이터를 쉽게 이해하고 해석하는 데 도움을 줍니다.</li>
            <li>데이터 기반의 의사결정은 더 나은 결과를 가져올 수 있습니다.</li>
            <li>데이터 분석은 다양한 분야에서 활용될 수 있습니다.</li>
        </ul>
    </div>
""", unsafe_allow_html=True)