import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 페이지 설정
st.set_page_config(layout="wide", page_title="2차시: 데이터 분석의 중요성")
# 네비게이션 버튼
col1, col2, col3 = st.columns([1,3,1])
with col1:
    if st.button('⬅️ 이전 차시로'):
        st.switch_page("pages/week1.py")  
with col3:
    if st.button('다음 차시 ➡️'):
        st.switch_page("pages/week3.py")  

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
        .data-info {
            background-color: #f0f2f6;
            padding: 15px;
            border-radius: 10px;
            margin: 10px 0;
        }
    </style>
""", unsafe_allow_html=True)

# 데이터 로드 함수
@st.cache_data
def load_data():
    df = pd.read_csv('bikeborrow.csv', encoding='cp949')
    # 시간대 데이터 처리
    df['시간'] = df['기준_시간대'].astype(str).str.zfill(4)
    df['시간대'] = pd.to_datetime(df['시간'], format='%H%M').dt.hour
    # 출발지 구 추출 - NaN 값 처리 추가
    df['출발_구'] = df['시작_대여소명'].fillna('').astype(str).apply(
        lambda x: x.split('_')[0].replace('동', '').strip() if x else '알수없음'
    )
    return df

# 타이틀
st.markdown('<h1 class="title">🚲 2차시: 데이터로 보는 따릉이 이야기</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">우리 동네 사람들은 언제, 어디서, 어떻게 따릉이를 이용할까요?</p>', unsafe_allow_html=True)

# 데이터 로드
df = load_data()

# 전체 데이터 미리보기
st.markdown("### 📊 전체 데이터 살펴보기")
st.markdown('<div class="data-info">먼저 전체 데이터를 살펴볼까요?</div>', unsafe_allow_html=True)
st.dataframe(df.head(10))

# 지역 선택
st.markdown("### 🎯 지역 선택하기")
selected_region = st.selectbox(
    "분석하고 싶은 지역을 선택하세요",
    sorted(df['출발_구'].unique())
)

# 선택된 지역의 데이터만 필터링
filtered_df = df[df['출발_구'] == selected_region]

if not filtered_df.empty:
    st.markdown(f"## 📈 {selected_region} 따릉이 이용 분석")
    
    # 1. 시간대별 이용 현황
    st.markdown("### ⏰ 시간대별 이용 현황")
    hourly_usage = filtered_df.groupby('시간대')['전체_건수'].sum().reset_index()
    
    fig_time = px.line(hourly_usage, 
                       x='시간대', 
                       y='전체_건수',
                       title=f'{selected_region} 시간대별 이용 건수',
                       labels={'시간대': '시간', '전체_건수': '이용 건수'})
    
    fig_time.update_layout(height=400)
    st.plotly_chart(fig_time, use_container_width=True)
    
    # 2. 이용 시간 분포
    st.markdown("### ⌛ 이용 시간 분포")
    
    fig_duration = px.histogram(filtered_df, 
                               x='전체_이용_분',
                               title=f'{selected_region} 이용 시간 분포',
                               labels={'전체_이용_분': '이용 시간(분)', 'count': '건수'},
                               nbins=30)
    
    fig_duration.update_layout(height=400)
    st.plotly_chart(fig_duration, use_container_width=True)
    
    # 3. 주요 목적지 분석
    st.markdown("### 🎯 주요 목적지 TOP 10")
    destination_counts = filtered_df.groupby('종료_대여소명')['전체_건수'].sum().sort_values(ascending=False).head(10)
    
    fig_dest = px.bar(destination_counts,
                      title=f'{selected_region} 주요 목적지',
                      labels={'index': '목적지', 'value': '이용 건수'},
                      orientation='h')
    
    fig_dest.update_layout(height=500)
    st.plotly_chart(fig_dest, use_container_width=True)
    
    # 통계 요약
    st.markdown("### 📊 이용 통계 요약")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("총 이용 건수", f"{filtered_df['전체_건수'].sum():,}건")
    with col2:
        avg_duration = filtered_df['전체_이용_분'].mean()
        st.metric("평균 이용 시간", f"{avg_duration:.1f}분")
    with col3:
        avg_distance = filtered_df['전체_이용_거리'].mean()
        st.metric("평균 이동 거리", f"{avg_distance:.0f}m")
    
    # 추가 인사이트
    st.markdown("""
        <div class="data-info">
            <h4>💡 분석 결과를 통해 알 수 있는 점</h4>
            <ul>
                <li>가장 바쁜 시간대는 언제인가요?</li>
                <li>평균적으로 얼마나 오래 자전거를 탈까요?</li>
                <li>주로 어디로 이동하나요?</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
else:
    st.warning("선택한 지역의 데이터가 없습니다.")