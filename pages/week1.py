import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 페이지 설정
st.set_page_config(layout="wide", page_title="1차시: 데이터 시각화의 중요성")
# 네비게이션 버튼
col1, col2, col3 = st.columns([1,3,1])
with col1:
    if st.button('⬅️ 처음으로'):
        st.switch_page("app.py")  # 메인 페이지로
with col3:
    if st.button('다음 차시 ➡️'):
        st.switch_page("pages/week2.py")  # 2차시로

st.markdown("<hr>", unsafe_allow_html=True)

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
        .stat-card {
            background-color: white;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            margin: 10px;
            text-align: center;
        }
        .instructions {
            background-color: #FFF3E0;
            padding: 15px;
            border-radius: 10px;
            margin: 10px 0;
        }
    </style>
""", unsafe_allow_html=True)

# 데이터 로드
@st.cache_data
def load_data():
    df = pd.read_csv('seoul.csv', encoding='cp949')
    return df

# 타이틀
st.markdown('<h1 class="title">🚲 1차시: 데이터 시각화의 중요성</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">서울시 자전거 대여/반납 현황을 다양한 그래프로 알아보아요! 📊</p>', unsafe_allow_html=True)

# 데이터 로드
df = load_data()
df = df.drop_duplicates(subset='자치구_명칭', keep='last')

# 탭 생성
tab1, tab2 = st.tabs(['📊 자치구별 현황', '🥧 비율 분석'])

with tab1:
    st.markdown('<h2 class="tab-title">📊 자치구별 대여/반납 탐험하기</h2>', unsafe_allow_html=True)
    
    st.markdown('<div class="instructions">🎯 궁금한 지역 3곳을 선택해서 비교해보세요!</div>', unsafe_allow_html=True)

    selected_districts = st.multiselect(
        '자치구를 3개 선택하세요',
        df['자치구_명칭'].unique(),
        max_selections=3
    )

    if selected_districts:
        filtered_df = df[df['자치구_명칭'].isin(selected_districts)]
        
        fig1 = go.Figure()
        
        fig1.add_trace(go.Bar(
            name='대여 횟수',
            x=filtered_df['자치구_명칭'],
            y=filtered_df['대여_건수'],
            marker_color='#FF9999'
        ))
        
        fig1.add_trace(go.Bar(
            name='반납 횟수',
            x=filtered_df['자치구_명칭'],
            y=filtered_df['반납_건수'],
            marker_color='#66B2FF'
        ))
        
        fig1.update_layout(
            barmode='group',
            xaxis_title='우리 동네',
            yaxis_title='이용 횟수',
            height=500,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(size=14)
        )
        
        st.plotly_chart(fig1, use_container_width=True)

        # 통계 카드 
        total_rental = filtered_df['대여_건수'].sum()
        total_return = filtered_df['반납_건수'].sum()

        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"""
                <div class="stat-card">
                    <h3>🚲 총 대여 횟수</h3>
                    <h2 style="color: #FF6B6B;">{total_rental:,}회</h2>
                </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
                <div class="stat-card">
                    <h3>🎯 총 반납 횟수</h3>
                    <h2 style="color: #4A90E2;">{total_return:,}회</h2>
                </div>
            """, unsafe_allow_html=True)

with tab2:
    st.markdown('<h2 class="tab-title">🥧 자치구별 비율 살펴보기</h2>', unsafe_allow_html=True)
    
    st.markdown('<div class="instructions">🔄 대여와 반납 중 하나를 선택해서 비율을 확인해보세요!</div>', unsafe_allow_html=True)
    
    metric_choice = st.radio(
        "무엇을 살펴볼까요?",
        ('대여_건수', '반납_건수'),
        format_func=lambda x: '대여 횟수' if x == '대여_건수' else '반납 횟수'
    )

    fig2 = px.pie(
        df,
        values=metric_choice,
        names='자치구_명칭',
        title=f'우리 동네별 {metric_choice.split("_")[0]} 비율',
        color_discrete_sequence=px.colors.qualitative.Set3
    )

    fig2.update_layout(
        height=700,
        font=dict(size=12)
    )
    fig2.update_traces(textposition='inside', textinfo='percent+label')

    st.plotly_chart(fig2, use_container_width=True)
    
    

# 학습 퀴즈 섹션
st.markdown("""
    <div class="fun-fact" style="background-color: #E8F5E9; margin-top: 30px;">
        <h2 style="color: #2E7D32;">📚 오늘의 학습 퀴즈</h2>
    </div>
""", unsafe_allow_html=True)

# 퀴즈 1: 데이터 이해하기
st.markdown("""
    <div style="background-color: #F5F5F5; padding: 20px; border-radius: 10px; margin: 10px 0;">
        <h3>💡 퀴즈 1: 숫자로만 된 데이터 읽어보기</h3>
    </div>
""", unsafe_allow_html=True)

# 예시 데이터 표시
example_data = pd.DataFrame({
    '대여소': ['A', 'B', 'C', 'D', 'E'],
    '대여횟수': [1205, 954, 1678, 892, 1432]
})
st.dataframe(example_data)

q1 = st.radio(
    "Q. 위 표에서 가장 많이 대여된 대여소를 찾으려면 어떤 느낌인가요?",
    [
        "한눈에 쉽게 알 수 있다",
        "숫자를 하나하나 비교해봐야 해서 시간이 걸린다",
        "어려운 계산이 필요하다"
    ]
)

if q1 == "숫자를 하나하나 비교해봐야 해서 시간이 걸린다":
    st.success("정답입니다! 👏 숫자로만 된 데이터는 비교하기 어렵죠.")

# 퀴즈 2: 시각화된 데이터 보기
st.markdown("""
    <div style="background-color: #F5F5F5; padding: 20px; border-radius: 10px; margin: 10px 0;">
        <h3>💡 퀴즈 2: 같은 데이터를 그래프로 보기</h3>
    </div>
""", unsafe_allow_html=True)

# 막대 그래프로 시각화
fig = go.Figure(data=[
    go.Bar(x=example_data['대여소'], y=example_data['대여횟수'])
])
fig.update_layout(title="대여소별 대여횟수")
st.plotly_chart(fig)

q2 = st.radio(
    "Q. 이제 가장 많이 대여된 대여소를 찾을 수 있나요?",
    [
        "그래프로 보니 한눈에 알 수 있다",
        "여전히 찾기 어렵다",
        "잘 모르겠다"
    ]
)

if q2 == "그래프로 보니 한눈에 알 수 있다":
    st.success("정답입니다! 👏 시각화하면 훨씬 쉽게 비교할 수 있죠.")

# 마무리 메시지
st.markdown("""
    <div class="data-info" style="margin-top: 30px;">
        <h3>💡 오늘의 발견!</h3>
        <p>1. 어느 지역에서 자전거를 가장 많이 이용할까요?</p>
        <p>2. 대여 횟수와 반납 횟수의 차이는 무엇을 의미할까요?</p>
        <p>3. 우리 동네는 다른 동네와 비교하면 어떤가요?</p>
    </div>
""", unsafe_allow_html=True)