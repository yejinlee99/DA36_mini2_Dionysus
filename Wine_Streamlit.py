import streamlit as st
from wine_beginner import *
from wine_food import *



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
    st.write("당신은 와린이 시군요!! 당신에게 알맞은 와인을 추천해 드리겠습니다.")
    col1, col2 = st.columns(2)
    with col1:
        # '홈으로 돌아가기' 버튼
        if st.button('홈으로 돌아가기', icon = '🏠', use_container_width=True):
            st.session_state.page = 'home'  # 버튼 클릭 시 홈 페이지로 이동
    with col2:
        # '추천 시작' 버튼
        if st.button('추천 시작하기!', icon = '🍷', use_container_width=True):
            st.session_state.page = 'wine_beginner_step1'  # 버튼 클릭 시 step1 페이지로 이동


# '질문1' 페이지
elif st.session_state.page == 'wine_beginner_step1':
    st.session_state.selected_values = []
    st.title("Step 1. 더 선호하시는 것은 무엇입니까? ")
    if st.button('고기🥩', icon = '🥩', use_container_width=True):
        answer1 = 'dry', 'firm', 'tannins', 'red', 'flavor', 'dark', 'cabernet', 'sauvignon'
        st.session_state.selected_values.append(answer1)
        st.session_state.page = 'wine_beginner_step2'  # 버튼 클릭 시 페이지 변경
    if st.button('생선🐟', icon = '🐟', use_container_width=True):
        answer1 = 'fruit', 'white', 'crisp', 'fresh', 'bright', 'touch', 'sauvignon', 'light'
        st.session_state.selected_values.append(answer1)
        st.session_state.page = 'wine_beginner_step2'
    if st.button('채소🥬', icon = '🥬', use_container_width=True):
        answer1 = 'fruit', 'white', 'crisp', 'fresh', 'bright', 'touch', 'sauvignon', 'light'
        st.session_state.selected_values.append(answer1)
        st.session_state.page = 'wine_beginner_step2'

    # '홈으로 돌아가기' 버튼
    if st.button('홈으로 돌아가기', icon = '🏠'):
        st.session_state.page = 'home'  # 버튼 클릭 시 홈 페이지로 이동

# '질문2' 페이지
elif st.session_state.page == 'wine_beginner_step2':
    st.title("Step 2. 더 선호하시는 것은 무엇입니까? ")
    if st.button('트로피칼🍍', icon = '🍍', use_container_width=True):
        answer2 = 'fruit', 'apple', 'peach', 'pear', 'ripe', 'fruity', 'smooth', 'juicy', 'white', 'flavor', 'smooth', 'soft', 'sauvignon', 'rich', 'round', 'plum', 'sweet'
        st.session_state.selected_values.append(answer2)
        st.session_state.page = 'wine_beginner_step3'  # 버튼 클릭 시 페이지 변경
    if st.button('시트러스🍊', icon = '🍊', use_container_width=True):
        answer2 = 'fruit', 'citrus', 'lemon', 'acidity', 'fruity', 'juicy', 'white', 'flavor', 'crisp', 'green', 'fresh', 'bright', 'touch', 'sauvignon', 'light'
        st.session_state.selected_values.append(answer2)
        st.session_state.page = 'wine_beginner_step3'
    if st.button('베리🍒', icon = '🍒', use_container_width=True):
        answer2 = 'fruit', 'red', 'berry', 'blackberry', 'raspberry', 'black cherry', 'bright', 'cabernet', 'sauvignon'
        st.session_state.selected_values.append(answer2)
        st.session_state.page = 'wine_beginner_step3'
    if st.button('향신료🫚', icon = '🫚', use_container_width=True):
        answer2 = 'structure', 'firm', 'red', 'flavor', 'spicy', 'spice', 'dark', 'character', 'rich'
        st.session_state.selected_values.append(answer2)
        st.session_state.page = 'wine_beginner_step3'

    col1, col2 = st.columns(2)
    with col1:
        # '홈으로 돌아가기' 버튼
        if st.button('홈으로 돌아가기', icon='🏠', use_container_width=True):
            st.session_state.page = 'home'  # 버튼 클릭 시 홈 페이지로 이동
    with col2:
        # '이전으로 돌아가기' 버튼
        if st.button('이전 페이지로 돌아가기', icon='⬅️', use_container_width=True):
            st.session_state.page = 'wine_beginner_step1'

# '질문3' 페이지
elif st.session_state.page == 'wine_beginner_step3':
    st.title("Step 3. 더 선호하시는 것은 무엇입니까? ")

    if st.button('장미꽃🌹', icon = '🌹', use_container_width=True):
        answer3 = 'structure', 'firm', 'red', 'dark', 'rich'
        st.session_state.selected_values.append(answer3)
        st.session_state.page = 'wine_beginner_step4'  # 버튼 클릭 시 페이지 변경
    if st.button('제비꽃🌸', icon = '🌸', use_container_width=True):
        answer3 = 'smooth', 'red', 'flavor', 'finish', 'dark', 'soft', 'texture', 'cabernet', 'sauvignon', 'rich', 'nose'
        st.session_state.selected_values.append(answer3)
        st.session_state.page = 'wine_beginner_step4'
    if st.button('백합🌼', icon = '🌼', use_container_width=True):
        answer3 = 'white', 'crisp', 'fresh', 'bright', 'touch', 'light'
        st.session_state.selected_values.append(answer3)
        st.session_state.page = 'wine_beginner_step4'
    if st.button('나무🌳', icon = '🌳', use_container_width=True):
        answer3 = 'dry', 'structure', 'firm', 'red', 'dark', 'texture', 'cabernet', 'sauvignon', 'oak', 'vanilla', 'years', 'feel', 'toast', 'lead', 'age'
        st.session_state.selected_values.append(answer3)
        st.session_state.page = 'wine_beginner_step4'

    col1, col2 = st.columns(2)
    with col1:
        # '홈으로 돌아가기' 버튼
        if st.button('홈으로 돌아가기', icon='🏠', use_container_width=True):
            st.session_state.page = 'home'  # 버튼 클릭 시 홈 페이지로 이동
    with col2:
        # '이전으로 돌아가기' 버튼
        if st.button('이전 페이지로 돌아가기', icon='⬅️', use_container_width=True):
            st.session_state.page = 'wine_beginner_step2'

# '질문4' 페이지
elif st.session_state.page == 'wine_beginner_step4':
    st.title("Step 4. 더 선호하시는 것은 무엇입니까? ")
    if st.button('달콤한 초콜릿❤️', icon = '❤️', use_container_width=True):
        answer4 = 'juicy', 'crisp', 'bright', 'chocolate', 'sweet', 'light'
        st.session_state.selected_values.append(answer4)
        st.session_state.page = 'wine_beginner_step5'  # 버튼 클릭 시 페이지 변경
    if st.button('카카오 50%🤎', icon = '🤎', use_container_width=True):
        answer4 = 'smooth', 'soft', 'chocolate', 'hint', 'sweet'
        st.session_state.selected_values.append(answer4)
        st.session_state.page = 'wine_beginner_step5'
    if st.button('카카오 100%🍫', icon = '🍫', use_container_width=True):
        answer4 = 'dry', 'structure', 'firm', 'tannins', 'red', 'dark', 'chocolate', 'lead'
        st.session_state.selected_values.append(answer4)
        st.session_state.page = 'wine_beginner_step5'

    col1, col2 = st.columns(2)
    with col1:
        # '홈으로 돌아가기' 버튼
        if st.button('홈으로 돌아가기', icon='🏠', use_container_width=True):
            st.session_state.page = 'home'  # 버튼 클릭 시 홈 페이지로 이동
    with col2:
        # '이전으로 돌아가기' 버튼
        if st.button('이전 페이지로 돌아가기', icon='⬅️', use_container_width=True):
            st.session_state.page = 'wine_beginner_step3'

# '질문5' 페이지
elif st.session_state.page == 'wine_beginner_step5':
    st.title("Step 5. 어떤 김치를 더 좋아하세요?")
    if st.button('묵은지🌶️', icon = '🌶️', use_container_width=True):
        answer5 = 'dry', 'structure', 'firm', 'tannins', 'red', 'white', 'cabernet', 'sauvignon', 'oak', 'years', 'age'
        st.session_state.selected_values.append(answer5)
        st.session_state.page = 'wine_beginner_step6'  # 버튼 클릭 시 페이지 변경
    if st.button('신김치🧄', icon = '🧄', use_container_width=True):
        answer5 = 'acidity', 'fruit', 'lemon', 'white', 'green', 'crisp', 'fresh', 'bright', 'light', 'age'
        st.session_state.selected_values.append(answer5)
        st.session_state.page = 'wine_beginner_step6'
    if st.button('조금 익은 김치🧅', icon = '🧅', use_container_width=True):
        answer5 = 'smooth', 'plum', 'soft', 'round'
        st.session_state.selected_values.append(answer5)
        st.session_state.page = 'wine_beginner_step6'

    col1, col2 = st.columns(2)
    with col1:
        # '홈으로 돌아가기' 버튼
        if st.button('홈으로 돌아가기', icon='🏠', use_container_width=True):
            st.session_state.page = 'home'  # 버튼 클릭 시 홈 페이지로 이동
    with col2:
        # '이전으로 돌아가기' 버튼
        if st.button('이전 페이지로 돌아가기', icon='⬅️', use_container_width=True):
            st.session_state.page = 'wine_beginner_step4'

# '질문6' 페이지
elif st.session_state.page == 'wine_beginner_step6':
    st.title("Step 6. 좋아하는 커피 종류를 알려주세요.")
    if st.button('라떼🥛', icon = '🥛', use_container_width=True):
        answer6 = 'smooth', 'soft', 'light', 'round'
        st.session_state.selected_values.append(answer6)
        st.session_state.page = 'wine_beginner_step7'  # 버튼 클릭 시 페이지 변경
    if st.button('에스프레소☕', icon = '☕', use_container_width=True):
        answer6 = 'dry', 'structure', 'firm', 'tannins', 'red', 'dark', 'rich', 'character'
        st.session_state.selected_values.append(answer6)
        st.session_state.page = 'wine_beginner_step7'
    if st.button('아메리카노🥤', icon = '🥤', use_container_width=True):
        answer6 = 'dry', 'smooth', 'soft', 'rich', 'hint', 'round'
        st.session_state.selected_values.append(answer6)
        st.session_state.page = 'wine_beginner_step7'

    col1, col2 = st.columns(2)
    with col1:
        # '홈으로 돌아가기' 버튼
        if st.button('홈으로 돌아가기', icon='🏠', use_container_width=True):
            st.session_state.page = 'home'  # 버튼 클릭 시 홈 페이지로 이동
    with col2:
        # '이전으로 돌아가기' 버튼
        if st.button('이전 페이지로 돌아가기', icon='⬅️', use_container_width=True):
            st.session_state.page = 'wine_beginner_step5'

# '질문7' 페이지
elif st.session_state.page == 'wine_beginner_step7':
    st.title("Step 7. 홍차의 떫은 맛에 더 익숙한가요?")
    if st.button('진하게 우려낸🥇', icon = '🥇', use_container_width=True):
        answer7 = 'dry', 'structure', 'firm', 'tannins', 'red', 'dark'
        st.session_state.selected_values.append(answer7)
        st.session_state.page = 'wine_beginner_final'  # 버튼 클릭 시 페이지 변경
    if st.button('적당히 우려낸🥈', icon = '🥈', use_container_width=True):
        answer7 = 'structure', 'red', 'dark', 'smooth', 'soft', 'hint'
        st.session_state.selected_values.append(answer7)
        st.session_state.page = 'wine_beginner_final'
    if st.button('연하게 우려낸🥉', icon = '🥉', use_container_width=True):
        answer7 = 'smooth', 'soft', 'touch', 'light'
        st.session_state.selected_values.append(answer7)
        st.session_state.page = 'wine_beginner_final'

    col1, col2 = st.columns(2)
    with col1:
        # '홈으로 돌아가기' 버튼
        if st.button('홈으로 돌아가기', icon='🏠', use_container_width=True):
            st.session_state.page = 'home'  # 버튼 클릭 시 홈 페이지로 이동
    with col2:
        # '이전으로 돌아가기' 버튼
        if st.button('이전 페이지로 돌아가기', icon='⬅️', use_container_width=True):
            st.session_state.page = 'wine_beginner_step6'

# 결과 확인하러가기 페이지
elif st.session_state.page == 'wine_beginner_final':
    st.title('모든 질문이 끝났습니다.')
    st.write('결과 확인까지 다소 시간이 걸릴 수 있습니다. 잠시만 기다려 주세요~')
    if st.button('결과 확인하러 가기🍇', icon='🍇', use_container_width=True):
        st.session_state.page = 'wine_beginner_final_result'

# 와린이 파이널 페이지
elif st.session_state.page == 'wine_beginner_final_result':
    st.title('🤔와린이 와인 추천 완료🤔')

    wine_beginner_recommendation_result = wine_beginner_recommendation(st.session_state.selected_values)
    
    st.write("🍷당신이 좋아할 것 같은 Top 3 와인🍷")
    st.write(f"🥇 Top 1. {wine_beginner_recommendation_result[0]}")
    st.write(f"🥈 Top 2. {wine_beginner_recommendation_result[1]}")
    st.write(f"🥉 Top 3. {wine_beginner_recommendation_result[2]}")

    st.write("😵당신이 좋아하지 않을 것 같은 Top 3 와인😵")
    st.write(f"🧨 Bottom 1. {wine_beginner_recommendation_result[-1]}")
    st.write(f"🧨 Bottom 2. {wine_beginner_recommendation_result[-2]}")
    st.write(f"🧨 Bottom 3. {wine_beginner_recommendation_result[-3]}")

    col1, col2 = st.columns(2)
    with col1:
        # '홈으로 돌아가기' 버튼
        if st.button('홈으로 돌아가기', icon = '🏠', use_container_width=True):
            st.session_state.page = 'home'  # 버튼 클릭 시 홈 페이지로 이동
    with col2:
        # '다시 추천 받기' 버튼
        if st.button('다시 추천 받기!', icon = '🔄', use_container_width=True):
            st.session_state.page = 'wine_beginner_step1'  # 버튼 클릭 시 다시 step1 페이지로 이동




# <!--해빈 start-->

# 음식에 어울리는 와인 추천 페이지
elif st.session_state.page == 'wine_food':
    st.title('맛잘알 와인 추천🍽️')

    st.write("당신은 음식에 어울리는 와인을 찾고 있으시군요!!")
    st.write("당신에게 알맞은 와인을 추천해 드리겠습니다.")
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
    st.title("함께 페어링할 음식을 골라주세요~")

    # 세션 상태에 리스트가 없다면 초기화
    if 'user_input' not in st.session_state:
        st.session_state.user_input = []
    if 'user_text' not in st.session_state:
        st.session_state.user_text = []

    # 음식 종류 선택하기
    food_options = ['aperitif', 'appetizers', 'beef','cheese','cured','desserts','fish','goat',\
                    'junk','lamb','lean','lemon','meat','milk', 'mushrooms', 'pasta',\
                    'pork' ,'poultry' ,'raw', 'salmon', 'shellfish' ,'snacks','tuna','vegetarian']
    st.session_state.add_food_option = st.pills("🥘어떤 음식과 곁들이실건가요?🥘", food_options, selection_mode="multi")
    # 눌린 버튼 저장용 세션 상태 초기화
    # if 'user_input' not in st.session_state:
    #     st.session_state.user_input = []
    #     st.session_state.add_food_option = []
    for food in st.session_state.add_food_option:
        if food not in st.session_state.user_input :
            if food:
                st.session_state.user_input.append(food)

    # 맛 종류 선택하기
    taste_options = ['soft', 'spicy', 'mild', 'rich', 'lean', 'fruity', 'sweet']
    st.session_state.add_taste_option = st.pills("👅어떤 맛의 음식인가요?👅", taste_options, selection_mode="multi")
    # # 눌린 버튼 저장용 세션 상태 초기화
    # if 'user_input' not in st.session_state:
    #     st.session_state.user_input = []
    #     st.session_state.add_taste_option = []
    for taste in st.session_state.add_taste_option:
        if taste not in st.session_state.user_input:
            if taste:
                st.session_state.user_input.append(taste)

    st.session_state.add_food = st.text_input("👇직접 입력하고 싶어요👇",placeholder="Write your food and press Enter to apply")
    if st.session_state.add_food not in st.session_state.user_input:
        # 리스트에 입력된 내용을 추가
        st.session_state.user_text.append(st.session_state.add_food)
        # 입력 필드 초기화
        # st.session_state.text_input = ""
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
        st.session_state.add_food_option = []
        st.session_state.add_taste_option = []
        st.session_state.page = 'wine_food_input'

    st.markdown(f"👉Your Choice: {st.session_state.user_input}.")
    print(st.session_state.user_input)

    on = st.toggle("Price setting")
    st.write("Price setting OFF range: 0 ~ 3,500,000 KRD")

    if on:
        price_range = st.slider(
            '💲가격대를 설정해주세요💲(단위: KRD)',
            min_value=10_000,  # 최소값
            max_value=300_000,  # 최대값
            value=(30_000, 70_000),  # 기본 범위 값
            step=5_000  # 슬라이더 단위 간격 설정
        )

        st.session_state.max_price = price_range[0]
        st.session_state.min_price = price_range[1]

    else:
        st.session_state.max_price = 3_500_000
        st.session_state.min_price = 0

    if st.button('결과 확인하러 가기🍇', icon='🍇', use_container_width=True):
        st.session_state.page = 'wine_food_result'

# 와린이 파이널 페이지
elif st.session_state.page == 'wine_food_result':
    st.title('🍽️맛잘알 와인 추천 완료🍽️')

    wine_food_result = content_based_food_pairing(st.session_state.user_input, st.session_state.max_price, st.session_state.min_price)

    st.write(f"🍷당신이 선택한 음식 {st.session_state.user_input}과 어울리는 와인은🍷")
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

# <!--해빈 end-->


























