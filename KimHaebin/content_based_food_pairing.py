import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

food_paring_df = pd.read_csv('data_cleansed.csv')

# user_input_list = []
# user_input = input('Which food?: ')
# user_input_list.append(user_input)

def concat_dataframe(user_input, food_paring_df=food_paring_df):
    user_input_df = pd.DataFrame({
        'vintage_id': [None],
        'vintage_name': [None],
        'vintage_year': [None],
        'vintage_price': [None],
        'vintage_ratings_average': [None],
        'vintage_ratings_count': [None],
        'vintage_wine_id': [None],
        'vintage_wine_name': [None],
        'vintage_winery': [None],
        'vintage_country': [None],
        'vintage_region': [None],
        'vintage_wine_type': [None],
        'acidity': [None],
        'fizziness': [None],
        'intensity': [None],
        'sweetness': [None],
        'tannin': [None],
        'flavor': [None],
        'varietal_name': [None],
        'body_description': [None],
        'acidity_description': [None],
        'foods': [user_input]
    })

    user_input_df['foods'] = user_input_df['foods'].apply(lambda food: ', '.join(food) if isinstance(food, list) else food)
    print(user_input_df)
    food_paring_df_new_added = pd.concat([food_paring_df, user_input_df], ignore_index=True)
    return food_paring_df_new_added

def weighted_rating(food_paring_df_new_added):
    C = food_paring_df_new_added['vintage_ratings_average'].mean()
    m = food_paring_df_new_added['vintage_ratings_count'].quantile(0.5)
    v = food_paring_df_new_added['vintage_ratings_count']
    R = food_paring_df_new_added['vintage_ratings_average']
    weighted_rating = (v / (v + m)) * R + (m / (v + m)) * C
    return weighted_rating

def add_weighted_ratings_column(weighted_rating, food_paring_df_new_added):
    food_paring_df_new_added['weighted_ratings'] = weighted_rating(food_paring_df)
    food_paring_df_new_added_wr = food_paring_df_new_added
    return food_paring_df_new_added_wr

def food_cosine_similarity_analysis(food_paring_df_new_added_wr, max_price, min_price):
    count_vectorizer = CountVectorizer(ngram_range=(1, 3))
    foods_vec = count_vectorizer.fit_transform(food_paring_df_new_added_wr['foods'])
    foods_sim = cosine_similarity(foods_vec, foods_vec)
    wine_idx_by_foods_sim = foods_sim.argsort(axis=1)[:, ::-1]

    wine_idx = len(food_paring_df_new_added_wr) - 1
    recommended_idx = wine_idx_by_foods_sim[wine_idx, : 20]
    recommended_idx = recommended_idx[recommended_idx != wine_idx]
    df_recommended = food_paring_df_new_added_wr.iloc[recommended_idx]
    df_recommended_price_range = df_recommended[(df_recommended['vintage_price'] > min_price) & (df_recommended['vintage_price'] < max_price)]
    df_recommended_ratings = df_recommended_price_range.sort_values(by='weighted_ratings', ascending=False)
    return df_recommended_ratings

