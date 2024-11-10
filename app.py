import streamlit as st
from streamlit_pills import pills
from wine_beginner import *
from wine_food import *
import time


# 버튼에 스타일을 추가하는 CSS 코드
st.markdown("""
    <style>
    .stButton > button {
        background-color: #d2426a; /* 버튼 배경 색상 */
        color: white; /* 텍스트 색상 */
        border-radius: 5px; /* 둥근 모서리 */
        border: 2px solid #F97190;
        padding: 0.5em 1em;
    }
    .stButton > button:hover {
        background-color: #F97190; /* 호버 시 색상 */
        border: 2px solid #F97190;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("""
    <style>
    [theme]
    primaryColor="#ec58c0"
    backgroundColor="#F3EEED"
    secondaryBackgroundColor="#f97190"
    textColor="#d2426a"
     </style>
    """, unsafe_allow_html=True)


# 세션 상태를 사용하여 페이지를 추적
if 'page' not in st.session_state:
    st.session_state.page = 'home'  # 기본 페이지는 'home'


# 홈 페이지
if st.session_state.page == 'home':
    st.title('🍷와인 추천 시스템🍷')
    st.write("안녕하세요. 당신이 좋아할 만한 와인을 추천해 드립니다!!")

    # '와잘알 와인추천' 버튼
    if st.button('와잘알 와인 추천🤓', icon="🤓", use_container_width=True):
        st.session_state.page = 'wine_expert'  # 버튼 클릭 시 페이지 변경
    st.write("☝️ 와인에 대해 잘 아시는 당신! 이걸 이용해 보세요!")

    # '와린이 와인추천' 버튼
    if st.button('와린이 와인 추천🤔', icon="🤔", use_container_width=True):
        st.session_state.page = 'wine_beginner'  # 버튼 클릭 시 페이지 변경
    st.write("☝️ 와인에 대해 잘 모르는 당신! 이걸 이용해 보세요!")

    # '음식에 어울리는  와인추천' 버튼
    if st.button('맛잘알 와인 추천🍽️', icon="🍽️", use_container_width=True):
        st.session_state.page = 'wine_food'  # 버튼 클릭 시 페이지 변경
    st.write("☝️ 음식에 어울리는 와인을 찾고 있는 당신! 이걸 이용해 보세요!")

# 와잘알 추천 페이지
elif st.session_state.page == 'wine_expert':
    st.title('🤓와잘알 추천 시스템🤓')
    st.write("당신은 와잘알이시군요!! 당신에게 알맞은 와인을 추천해 드리겠습니다.")

    # '홈으로 돌아가기' 버튼
    if st.button('홈으로 돌아가기'):
        st.session_state.page = 'home'  # 버튼 클릭 시 홈 페이지로 이동

# 와린이 추천 페이지
elif st.session_state.page == 'wine_beginner':
    st.title('🤔와린이 추천🤔')
    st.write("📢 와인에 대해 잘 모르시겠다고요?")
    st.write("📢 걱정 하지 마세요!!")
    st.write("📢 제가 당신에게 알맞은 와인을 추천해 드리겠습니다.😁👍")
    col1, col2 = st.columns(2)
    with col1:
        # '홈으로 돌아가기' 버튼
        if st.button('홈으로 돌아가기', icon='🏠', use_container_width=True):
            st.session_state.page = 'home'  # 버튼 클릭 시 홈 페이지로 이동
    with col2:
        # '추천 시작' 버튼
        if st.button('추천 시작하기!', icon='🍷', use_container_width=True):
            st.session_state.page = 'wine_beginner_step1'  # 버튼 클릭 시 step1 페이지로 이동

# '질문1' 페이지
elif st.session_state.page == 'wine_beginner_step1':
    st.session_state.selected_values = []
    st.title("Step 1.")
    st.subheader("더 선호하시는 것은 무엇입니까? ")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("./png/고기.jpg", use_container_width=True)
    with col2:
        st.image("./png/생선.jpg", use_container_width=True)
    with col3:
        st.image("./png/채소.jpg", use_container_width=True)

    if st.button('고기', icon='🥩', use_container_width=True):
        answer1 = 'dry', 'firm', 'tannins', 'red', 'flavor', 'dark', 'cabernet', 'sauvignon'
        st.session_state.selected_values.append(answer1)
        st.session_state.page = 'wine_beginner_step2'  # 버튼 클릭 시 페이지 변경
    if st.button('생선', icon='🐟', use_container_width=True):
        answer1 = 'fruit', 'white', 'crisp', 'fresh', 'bright', 'touch', 'sauvignon', 'light'
        st.session_state.selected_values.append(answer1)
        st.session_state.page = 'wine_beginner_step2'
    if st.button('채소', icon='🥬', use_container_width=True):
        answer1 = 'fruit', 'white', 'crisp', 'fresh', 'bright', 'touch', 'sauvignon', 'light'
        st.session_state.selected_values.append(answer1)
        st.session_state.page = 'wine_beginner_step2'

    # '홈으로 돌아가기' 버튼
    if st.button('홈으로 돌아가기', icon='🏠'):
        st.session_state.page = 'home'  # 버튼 클릭 시 홈 페이지로 이동

# '질문2' 페이지
elif st.session_state.page == 'wine_beginner_step2':
    st.title("Step 2.")
    st.subheader("더 선호하시는 것은 무엇입니까? ")

    col1, col2 = st.columns(2)
    with col1:
        st.image("./png/트로피칼.jpg", use_container_width=True)
    with col2:
        st.image("./png/시트러스.jpg", use_container_width=True)

    col1, col2 = st.columns(2)
    with col1:
        st.image("./png/베리.jpg", use_container_width=True)
    with col2:
        st.image("./png/향신료.jpg", use_container_width=True)

    if st.button('열대과일 ( 망고, 파인애플, 멜론 )', icon='🍍', use_container_width=True):
        answer2 = 'fruit', 'apple', 'peach', 'pear', 'ripe', 'fruity', 'smooth', 'juicy', 'white', 'flavor', 'smooth', 'soft', 'sauvignon', 'rich', 'round', 'plum', 'sweet'
        st.session_state.selected_values.append(answer2)
        st.session_state.page = 'wine_beginner_step3'  # 버튼 클릭 시 페이지 변경
    if st.button('감귤류 ( 레몬, 라임, 자몽 )', icon='🍊', use_container_width=True):
        answer2 = 'fruit', 'citrus', 'lemon', 'acidity', 'fruity', 'juicy', 'white', 'flavor', 'crisp', 'green', 'fresh', 'bright', 'touch', 'sauvignon', 'light'
        st.session_state.selected_values.append(answer2)
        st.session_state.page = 'wine_beginner_step3'
    if st.button('베리류 ( 딸기, 체리, 라즈베리 )', icon='🍒', use_container_width=True):
        answer2 = 'fruit', 'red', 'berry', 'blackberry', 'raspberry', 'black cherry', 'bright', 'cabernet', 'sauvignon'
        st.session_state.selected_values.append(answer2)
        st.session_state.page = 'wine_beginner_step3'
    if st.button('향신료 ( 후추, 계피, 정향 )', icon='🫚', use_container_width=True):
        answer2 = 'structure', 'firm', 'red', 'flavor', 'spicy', 'spice', 'dark', 'character', 'rich'
        st.session_state.selected_values.append(answer2)
        st.session_state.page = 'wine_beginner_step3'

    # '홈으로 돌아가기' 버튼
    if st.button('홈으로 돌아가기', icon='🏠'):
        st.session_state.page = 'home'  # 버튼 클릭 시 홈 페이지로 이동


# '질문3' 페이지
elif st.session_state.page == 'wine_beginner_step3':
    st.title("Step 3.")
    st.subheader("더 선호하시는 것은 무엇입니까? ")

    col1, col2 = st.columns(2)
    with col1:
        st.image("./png/장미꽃.jpg", use_container_width=True)
    with col2:
        st.image("./png/제비꽃.jpg", use_container_width=True)

    col1, col2 = st.columns(2)
    with col1:
        st.image("./png/백합.jpg", use_container_width=True)
    with col2:
        st.image("./png/나무.jpg", use_container_width=True)

    if st.button('장미꽃', icon='🌹', use_container_width=True):
        answer3 = 'structure', 'firm', 'red', 'dark', 'rich'
        st.session_state.selected_values.append(answer3)
        st.session_state.page = 'wine_beginner_step4'  # 버튼 클릭 시 페이지 변경
    if st.button('제비꽃', icon='🌸', use_container_width=True):
        answer3 = 'smooth', 'red', 'flavor', 'finish', 'dark', 'soft', 'texture', 'cabernet', 'sauvignon', 'rich', 'nose'
        st.session_state.selected_values.append(answer3)
        st.session_state.page = 'wine_beginner_step4'
    if st.button('백합', icon='🌼', use_container_width=True):
        answer3 = 'white', 'crisp', 'fresh', 'bright', 'touch', 'light'
        st.session_state.selected_values.append(answer3)
        st.session_state.page = 'wine_beginner_step4'
    if st.button('나무', icon='🌳', use_container_width=True):
        answer3 = 'dry', 'structure', 'firm', 'red', 'dark', 'texture', 'cabernet', 'sauvignon', 'oak', 'vanilla', 'years', 'feel', 'toast', 'lead', 'age'
        st.session_state.selected_values.append(answer3)
        st.session_state.page = 'wine_beginner_step4'

    # '홈으로 돌아가기' 버튼
    if st.button('홈으로 돌아가기', icon='🏠'):
        st.session_state.page = 'home'  # 버튼 클릭 시 홈 페이지로 이동

# '질문4' 페이지
elif st.session_state.page == 'wine_beginner_step4':
    st.title("Step 4.")
    st.subheader("더 선호하시는 것은 무엇입니까? ")

    col1, col2, col3 = st.columns(3)
    with col2:
        st.image("./png/초콜릿.jpg", use_container_width=True)

    if st.button('달콤한 초콜릿', use_container_width=True):
        answer4 = 'juicy', 'crisp', 'bright', 'chocolate', 'sweet', 'light'
        st.session_state.selected_values.append(answer4)
        st.session_state.page = 'wine_beginner_step5'  # 버튼 클릭 시 페이지 변경
    if st.button('카카오 50%', use_container_width=True):
        answer4 = 'smooth', 'soft', 'chocolate', 'hint', 'sweet'
        st.session_state.selected_values.append(answer4)
        st.session_state.page = 'wine_beginner_step5'
    if st.button('카카오 100%', use_container_width=True):
        answer4 = 'dry', 'structure', 'firm', 'tannins', 'red', 'dark', 'chocolate', 'lead'
        st.session_state.selected_values.append(answer4)
        st.session_state.page = 'wine_beginner_step5'

    # '홈으로 돌아가기' 버튼
    if st.button('홈으로 돌아가기', icon='🏠'):
        st.session_state.page = 'home'  # 버튼 클릭 시 홈 페이지로 이동

# '질문5' 페이지
elif st.session_state.page == 'wine_beginner_step5':
    st.title("Step 5.")
    st.subheader("어떤 김치를 더 좋아하세요? ")

    col1, col2, col3 = st.columns(3)
    with col2:
        st.image("./png/김치.jpg", use_container_width=True)

    if st.button('묵은지', use_container_width=True):
        answer5 = 'dry', 'structure', 'firm', 'tannins', 'red', 'white', 'cabernet', 'sauvignon', 'oak', 'years', 'age'
        st.session_state.selected_values.append(answer5)
        st.session_state.page = 'wine_beginner_step6'  # 버튼 클릭 시 페이지 변경
    if st.button('신김치', use_container_width=True):
        answer5 = 'acidity', 'fruit', 'lemon', 'white', 'green', 'crisp', 'fresh', 'bright', 'light', 'age'
        st.session_state.selected_values.append(answer5)
        st.session_state.page = 'wine_beginner_step6'
    if st.button('조금 익은 김치', use_container_width=True):
        answer5 = 'smooth', 'plum', 'soft', 'round'
        st.session_state.selected_values.append(answer5)
        st.session_state.page = 'wine_beginner_step6'

    # '홈으로 돌아가기' 버튼
    if st.button('홈으로 돌아가기', icon='🏠'):
        st.session_state.page = 'home'  # 버튼 클릭 시 홈 페이지로 이동

# '질문6' 페이지
elif st.session_state.page == 'wine_beginner_step6':
    st.title("Step 6.")
    st.subheader("어떤 종류의 커피를 좋아하세요?")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("./png/라떼.jpg", use_container_width=True)
    with col2:
        st.image("./png/에스프레소.jpg", use_container_width=True)
    with col3:
        st.image("./png/아메리카노.jpg", use_container_width=True)

    if st.button('라떼', icon='🥛', use_container_width=True):
        answer6 = 'smooth', 'soft', 'light', 'round'
        st.session_state.selected_values.append(answer6)
        st.session_state.page = 'wine_beginner_step7'  # 버튼 클릭 시 페이지 변경
    if st.button('에스프레소', icon='☕', use_container_width=True):
        answer6 = 'dry', 'structure', 'firm', 'tannins', 'red', 'dark', 'rich', 'character'
        st.session_state.selected_values.append(answer6)
        st.session_state.page = 'wine_beginner_step7'
    if st.button('아메리카노', icon='🥤', use_container_width=True):
        answer6 = 'dry', 'smooth', 'soft', 'rich', 'hint', 'round'
        st.session_state.selected_values.append(answer6)
        st.session_state.page = 'wine_beginner_step7'

    # '홈으로 돌아가기' 버튼
    if st.button('홈으로 돌아가기', icon='🏠'):
        st.session_state.page = 'home'  # 버튼 클릭 시 홈 페이지로 이동

# '질문7' 페이지
elif st.session_state.page == 'wine_beginner_step7':
    st.title("Step 7.")
    st.subheader("어떤 맛의 홍차를 좋아하세요?")

    col1, col2, col3 = st.columns(3)
    with col2:
        st.image("./png/홍차.jpg", use_container_width=True)

    if st.button('진하게 우려낸', use_container_width=True):
        answer7 = 'dry', 'structure', 'firm', 'tannins', 'red', 'dark'
        st.session_state.selected_values.append(answer7)
        st.session_state.page = 'wine_beginner_final'  # 버튼 클릭 시 페이지 변경
    if st.button('적당히 우려낸', use_container_width=True):
        answer7 = 'structure', 'red', 'dark', 'smooth', 'soft', 'hint'
        st.session_state.selected_values.append(answer7)
        st.session_state.page = 'wine_beginner_final'
    if st.button('연하게 우려낸', use_container_width=True):
        answer7 = 'smooth', 'soft', 'touch', 'light'
        st.session_state.selected_values.append(answer7)
        st.session_state.page = 'wine_beginner_final'

    # '홈으로 돌아가기' 버튼
    if st.button('홈으로 돌아가기', icon='🏠'):
        st.session_state.page = 'home'  # 버튼 클릭 시 홈 페이지로 이동

# 결과 확인하러가기 페이지
elif st.session_state.page == 'wine_beginner_final':
    st.title('모든 질문이 끝났습니다.')
    st.write('결과 확인까지 다소 시간이 걸릴 수 있습니다. 잠시만 기다려 주세요~')
    if st.button('결과 확인하러 가기🍇', icon='🍇', use_container_width=True):
        st.session_state.page = 'wine_beginner_final_result'

# 와린이 파이널 페이지
elif st.session_state.page == 'wine_beginner_final_result':
    result_title, result_country, result_price, result_variety, result_winery, result_points = wine_beginner_recommendation(st.session_state.selected_values)

    st.header("🍷 추천 와인 Best 3")
    st.header("🥇 Best 1")
    st.subheader(f"{result_title[0]}")
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"🌎 생산 나라 : {result_country[0]}")
        st.write(f"🍇 품종 / 종류 : {result_variety[0]}")
        st.write(f"🛖 와이너리 : {result_winery[0]}")
    with col2:
        st.write(f"🌟 평점 : :red[{result_points[0]}] / 100 점")
        st.write(f"💲가격 ( USD ) : {result_price[0]}")

    st.header("🥈 Best 2")
    st.subheader(f"{result_title[1]}")
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"🌎 생산 나라 : {result_country[1]}")
        st.write(f"🍇 품종 / 종류 : {result_variety[1]}")
        st.write(f"🛖 와이너리 : {result_winery[1]}")
    with col2:
        st.write(f"🌟 평점 : :red[{result_points[1]}] / 100 점")
        st.write(f"💲가격 ( USD ) : {result_price[1]}")

    st.header("🥉 Best 3")
    st.subheader(f"{result_title[2]}")
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"🌎 생산 나라 : {result_country[2]}")
        st.write(f"🍇 품종 / 종류 : {result_variety[2]}")
        st.write(f"🛖 와이너리 : {result_winery[2]}")
    with col2:
        st.write(f"🌟 평점 : :red[{result_points[2]}] / 100 점")
        st.write(f"💲가격 ( USD ) : {result_price[2]}")


    st.header("😵 비추천 와인 Worst 3")
    st.header("🖤 Worst 1")
    st.subheader(f"{result_title[-1]}")
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"🌎 생산 나라 : {result_country[-1]}")
        st.write(f"🍇 품종 / 종류 : {result_variety[-1]}")
        st.write(f"🛖 와이너리 : {result_winery[-1]}")
    with col2:
        st.write(f"🌟 평점 : :blue[{result_points[-1]}] / 100 점")
        st.write(f"💲가격 ( USD ) : {result_price[-1]}")

    st.header("🖤 Worst 2")
    st.subheader(f"{result_title[-2]}")
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"🌎 생산 나라 : {result_country[-2]}")
        st.write(f"🍇 품종 / 종류 : {result_variety[-2]}")
        st.write(f"🛖 와이너리 : {result_winery[-2]}")
    with col2:
        st.write(f"🌟 평점 : :blue[{result_points[-2]}] / 100 점")
        st.write(f"💲가격 ( USD ) : {result_price[-2]}")

    st.header("🖤 Worst 3")
    st.subheader(f"{result_title[-3]}")
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"🌎 생산 나라 : {result_country[-3]}")
        st.write(f"🍇 품종 / 종류 : {result_variety[-3]}")
        st.write(f"🛖 와이너리 : {result_winery[-3]}")
    with col2:
        st.write(f"🌟 평점 : :blue[{result_points[-3]}] / 100 점")
        st.write(f"💲가격 ( USD ) : {result_price[-3]}")

    col1, col2 = st.columns(2)
    with col1:
        # '홈으로 돌아가기' 버튼
        if st.button('홈으로 돌아가기', icon='🏠', use_container_width=True):
            st.session_state.page = 'home'  # 버튼 클릭 시 홈 페이지로 이동
    with col2:
        # '다시 추천 받기' 버튼
        if st.button('다시 추천 받기', icon='🔄', use_container_width=True):
            st.session_state.page = 'wine_beginner_step1'  # 버튼 클릭 시 다시 step1 페이지로 이동

# 음식에 어울리는 와인 추천 페이지
elif st.session_state.page == 'wine_food':
    st.title('🍽️맛잘알 와인 추천🍽️')

    st.write("📢 당신은 음식에 어울리는 와인을 찾고 있으시군요!")
    st.write("📢 음식에 페어링할 와인을 추천해 드리겠습니다.")
    col1, col2 = st.columns(2)
    with col1:
        # '홈으로 돌아가기' 버튼
        if st.button('홈으로 돌아가기', icon='🏠', use_container_width=True):
            st.session_state.page = 'home'  # 버튼 클릭 시 홈 페이지로 이동
    with col2:
        # '추천 시작' 버튼
        if st.button('추천 시작하기!', icon='🍷', use_container_width=True):
            st.session_state.page = 'wine_food_input'  # 버튼 클릭 시 input 페이지로 이동


elif st.session_state.page == 'wine_food_input':
    st.title("Food to pair with Wine🍽️")
    st.session_state.user_input = []
    st.session_state.user_text = []

    # 음식 종류 선택하기
    food_options = ['aperitif', 'appetizers', 'beef','cheese','cured','desserts','fish','goat',\
                    'junk','lamb','lean','lemon','meat','milk', 'mushrooms', 'pasta',\
                    'pork' ,'poultry' ,'raw', 'salmon', 'shellfish' ,'snacks','tuna','vegetarian']

    add_food_option = st.pills("🥘어떤 음식과 곁들이실건가요?🥘", food_options, selection_mode="multi")
    for food in add_food_option:
        if food not in st.session_state.user_input :
            if food:
                st.session_state.user_input.append(food)

    # 맛 종류 선택하기
    taste_options = ['soft', 'spicy', 'mild', 'rich', 'lean', 'fruity', 'sweet']
    add_taste_option = st.pills("👅어떤 맛의 음식인가요?👅", taste_options, selection_mode="multi")
    for taste in add_taste_option:
        if taste not in st.session_state.user_input:
            if taste:
                st.session_state.user_input.append(taste)

    # 직접 입력
    add_food = st.text_input("👇직접 입력하고 싶어요👇",placeholder="Write your food and press Enter to apply")
    if add_food not in st.session_state.user_input:
        if add_food:
            # 리스트에 입력된 내용을 추가
            st.session_state.user_text.append(add_food)
            # 입력 필드 초기화
            st.session_state.text_input = ""

    if 'user_input' not in st.session_state:
        st.session_state.user_input = []
        st.session_state.user_text = []
    for food in st.session_state.user_text:
        if food not in st.session_state.user_input:
            st.session_state.user_input.append(food)

    # 선택 내용 초기화
    if st.button("Reset choice"):
        st.session_state.user_text = []
        st.session_state.user_input = []
        add_food_option = []
        add_taste_option = []

    st.markdown(f"👉Your Choice: {st.session_state.user_input}.")
    # print(st.session_state.user_input)

    on = st.toggle("Price setting")
    st.write("※ 미설정 시 0 ~ 350만원 사이의 와인을 추천해드립니다")

    st.session_state.max_price= 3_500_000
    st.session_state.min_price = 0

    if on:
        price_range = st.slider(
            '💲가격대를 설정해주세요💲단위: 원(KRD)',
            min_value=10_000,  # 최소값
            max_value=300_000,  # 최대값
            value=(30_000, 70_000),  # 기본 범위 값
            step=5_000  # 슬라이더 단위 간격 설정
        )

        st.session_state.max_price = price_range[1]
        st.session_state.min_price = price_range[0]


    if st.button('결과 확인하러 가기🍇', icon='🍇', use_container_width=True):
        # st.session_state.user_text = []
        # st.session_state.user_input = []
        st.session_state.page = 'wine_food_result'

# 와린이 파이널 페이지
elif st.session_state.page == 'wine_food_result':
    st.title('🍽️맛잘알 와인 추천 완료🍽️')

    wine_food_result = content_based_food_pairing(st.session_state.user_input, st.session_state.max_price, st.session_state.min_price)

    st.write(f"당신이 선택한 {st.session_state.user_input}와/과 어울리는 와인은 🍷Best 10🍷")
    st.dataframe(wine_food_result)
    # st.write(f"🥇 Top 1. {wine_food_result[0]}")
    # st.write(f"🥈 Top 2. {wine_food_result[1]}")
    # st.write(f"🥉 Top 3. {wine_food_result[2]}")

    col1, col2 = st.columns(2)
    with col1:
        # '홈으로 돌아가기' 버튼
        if st.button('홈으로 돌아가기', icon='🏠', use_container_width=True):
            st.session_state.page = 'home'  # 버튼 클릭 시 홈 페이지로 이동
    with col2:
        # '다시 추천 받기' 버튼
        if st.button('다시 추천 받기!', icon='🔄', use_container_width=True):
            st.session_state.page = 'wine_food_input'  # 버튼 클릭 시 다시 step1 페이지로 이동




























