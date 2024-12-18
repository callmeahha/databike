import streamlit as st
import pandas as pd
import plotly.express as px
import folium
from streamlit_folium import folium_static

# 페이지 설정
st.set_page_config(layout="wide", page_title="4차시: 따릉이 공공사업 제안")
# 네비게이션 버튼
col1, col2, col3 = st.columns([1,3,1])
with col1:
    if st.button('⬅️ 이전 차시로'):
        st.switch_page("pages/week3.py")  
with col3:
    if st.button('다음 차시 ➡️'):
        st.switch_page("pages/week5.py")  

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
        .idea-box {
            background-color: #E3F2FD;
            padding: 20px;
            border-radius: 10px;
            margin: 10px 0;
        }
        .analysis-box {
            background-color: #FFF3E0;
            padding: 15px;
            border-radius: 10px;
            margin: 10px 0;
        }
    </style>
""", unsafe_allow_html=True)

# 타이틀
st.markdown('<h1 class="title">🚲 4차시: 따릉이 이용자 대상으로 한 공공사업 설계</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">데이터를 기반으로 우리 동네에 필요한 따릉이 공공사업을 제안해보아요! 🌟</p>', unsafe_allow_html=True)

# 이전 분석 결과 요약
st.markdown("### 📊 이전 분석 결과 살펴보기")
tab1, tab2 = st.tabs(["시간대별 패턴", "이용 시간 분석"])

with tab1:
   st.markdown("""
       <div class="analysis-box">
           <h4>⏰ 시간대별 특징을 정리해보세요</h4>
           <p>분석한 데이터를 바탕으로 시간대별 특징을 적어보세요.</p>
       </div>
   """, unsafe_allow_html=True)
   
   time_pattern = st.text_area("시간대별 특징:", height=150,
                              help="예시: 출근 시간대 이용량, 점심시간 패턴 등")

with tab2:
   st.markdown("""
       <div class="analysis-box">
           <h4>⌛ 이용 시간 특징을 정리해보세요</h4>
           <p>분석한 데이터를 바탕으로 이용 시간 특징을 적어보세요.</p>
       </div>
   """, unsafe_allow_html=True)
   
   usage_pattern = st.text_area("이용 시간 특징:", height=150,
                               help="예시: 평균 이용 시간, 장거리 이용 패턴 등")

# 추가 분석 희망사항
st.markdown("### 🔍 추가 분석 희망사항")

st.markdown("""
   <div class="analysis-box">
       <h4>더 알고 싶은 데이터와 활용 방안</h4>
   </div>
""", unsafe_allow_html=True)

additional_data = st.text_area("어떤 데이터를 추가적으로 분석하고 싶은가요?", 
                            height=100,
                            help="예시: 연령대별 이용 패턴, 날씨와 이용량의 관계 등")

data_usage = st.text_area("그 데이터를 분석하여 어떻게 사용하고 싶은가요?",
                        height=100,
                        help="예시: 연령대별 맞춤 서비스 개발, 날씨 기반 대여소 운영 계획 등")


# 프로젝트 제안 섹션
st.markdown("### 💡 공공사업 아이디어 제안")

# 지역 선택
selected_region = st.selectbox(
    "프로젝트를 진행할 지역을 선택하세요",
    ["강남구", "서초구", "송파구", "종로구", "마포구", "영등포구"]  # 예시 지역
)

# 사업 유형 선택
project_type = st.multiselect(
    "어떤 종류의 프로젝트인가요? (여러 개 선택 가능)",
    ["안전 강화", "편의성 개선", "환경 보호", "건강 증진", "문화/관광", "교통 연계"]
)

# 타겟 시간대 선택
target_time = st.select_slider(
    "주로 어느 시간대를 타겟으로 하나요?",
    options=["새벽(0-6시)", "아침(6-9시)", "오전(9-12시)", 
             "점심(12-14시)", "오후(14-17시)", "저녁(17-20시)", 
             "밤(20-24시)"]
)

# 예상 효과 선택
effects = st.multiselect(
    "기대되는 효과는 무엇인가요? (여러 개 선택 가능)",
    ["이용자 수 증가", "안전성 향상", "지역 경제 활성화", 
     "환경 보호", "건강 증진", "관광 활성화"]
)

# 아이디어 입력
st.markdown("""
    <div class="idea-box">
        <h4>🎈 나의 아이디어</h4>
    </div>
""", unsafe_allow_html=True)

project_title = st.text_input("프로젝트 제목을 입력하세요")
project_description = st.text_area("프로젝트 내용을 자세히 설명해주세요")
expected_budget = st.number_input("예상 소요 비용 (만원)", min_value=0)

# 제출 버튼
if st.button("아이디어 제출하기"):
    st.balloons()
    st.success("멋진 아이디어네요! 👏")
    
    # 제출된 아이디어 요약
    st.markdown("""
        <div class="idea-box">
            <h4>📝 제출된 아이디어 요약</h4>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
            - **프로젝트명**: {project_title}
            - **지역**: {selected_region}
            - **사업 유형**: {', '.join(project_type)}
            - **타겟 시간대**: {target_time}
        """)
    with col2:
        st.markdown(f"""
            - **기대 효과**: {', '.join(effects)}
            - **예상 비용**: {expected_budget}만원
        """)
    
    st.markdown("**상세 내용**")
    st.info(project_description)

# 추가 참고 자료
st.markdown("### 📚 아이디어 참고자료")
st.markdown("""
    <div class="analysis-box">
        <h4>효과적인 공공사업 제안을 위한 팁</h4>
        <ul>
            <li>데이터 분석 결과를 활용해 필요성을 입증하세요</li>
            <li>구체적인 대상과 목표를 설정하세요</li>
            <li>실현 가능한 예산과 일정을 고려하세요</li>
            <li>기대되는 효과를 구체적으로 설명하세요</li>
        </ul>
    </div>
""", unsafe_allow_html=True)