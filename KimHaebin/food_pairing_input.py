import streamlit as st

st.title('😋맛잘알 당신을 위한 와인 추천😋')

user_input = []
food_options = ['aperitif', 'appetizers', 'beef','cheese','cured','desserts','fish','goat','junk','lamb','lean','lemon','meat','milk', 'mushrooms', 'pasta',\
           'pork' ,'poultry' ,'raw', 'salmon', 'shellfish' ,'snacks','tuna','vegetarian']
add_food_option = st.pills("🥘어떤 음식과 곁들이실건가요?🥘", food_options, selection_mode="multi")
for food in add_food_option:
    user_input.append(food)

taste_options = ['soft', 'spicy', 'mild', 'rich', 'lean', 'fruity', 'sweet']
add_taste_option = st.pills("👅어떤 맛의 음식인가요?👅", taste_options, selection_mode="multi")
for taste in add_taste_option:
    user_input.append(taste)

if 'user_text' not in st.session_state:
    st.session_state.user_text = []
if 'text_input' not in st.session_state:
    st.session_state.text_input = ""

add_food = st.text_input("👇직접 입력하고 싶어요👇",placeholder="Write your food and press Enter to apply")
if add_food:
    # 리스트에 입력된 내용을 추가
    st.session_state.user_text.append(add_food)
    # 입력 필드 초기화
    st.session_state.text_input = ""

for food in st.session_state.user_text:
    user_input.append(food)

if st.button("Reset choice"):
    st.session_state.user_text = []
    user_input = []

st.markdown(f"👉Your Choice: {user_input}.")
print(user_input)

on = st.toggle("Price setting")

if on:
    price_range = st.slider(
        '💲가격대를 설정해주세요💲(단위: KRD)',
        min_value=10_000,  # 최소값
        max_value=300_000,  # 최대값
        value=(30_000, 70_000),  # 기본 범위 값
        step=5_000  # 슬라이더 단위 간격 설정
    )

    max_price = price_range[0]
    min_price = price_range[1]

else:
    max_price = 3_500_000
    min_price = 0

print(max_price, min_price)

# food_paring_df_new_added = content_based_food_pairing.concat_dataframe(user_input)
# weighted_rating = content_based_food_pairing.weighted_rating(food_paring_df_new_added)
# food_paring_df_new_added_wr = content_based_food_pairing.add_weighted_ratings_column(weighted_rating, food_paring_df_new_added)
# df_recommended_ratings = content_based_food_pairing.food_cosine_similarity_analysis(food_paring_df_new_added_wr, max_price, min_price)
#

