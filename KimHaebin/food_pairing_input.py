import streamlit as st
import pandas as pd
import content_based_food_pairing

st.title('😋맛잘알 당신을 위한 와인 추천😋')

user_input = []
multi_selected = st.multiselect(
    label='🥘어떤 음식과 곁들이실건가요?🥘',
    options=['beef', 'fish', 'pasta'],
)

if multi_selected:
    user_input.append(multi_selected)
print(user_input)

price_range = st.slider(
    '💲가격대를 설정해주세요.💲(단위: KRD)',
    min_value=10_000,  # 최소값
    max_value=500_000,  # 최대값
    value=(30_000, 70_000),# 기본 범위 값
    step=5_000  # 슬라이더 단위 간격 설정
)
max_price = price_range[0]
min_price = price_range[1]

print(max_price, min_price)

food_paring_df_new_added = content_based_food_pairing.concat_dataframe(user_input)
weighted_rating = content_based_food_pairing.weighted_rating(food_paring_df_new_added)
food_paring_df_new_added_wr = content_based_food_pairing.add_weighted_ratings_column(weighted_rating, food_paring_df_new_added)
df_recommended_ratings = content_based_food_pairing.food_cosine_similarity_analysis(food_paring_df_new_added_wr, max_price, min_price)


