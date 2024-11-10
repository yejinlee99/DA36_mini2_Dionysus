import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def concat_dataframe(user_input):
    food_paring_df = pd.read_csv('./data/archive/data_cleansed.csv')
    user_input_df = pd.DataFrame({
        'vintage_id': [0],
        'vintage_name': [None],
        'vintage_year': [None],
        'vintage_price': [0],
        'vintage_ratings_average': [0.0],
        'vintage_ratings_count': [0],
        'vintage_wine_id': [0],
        'vintage_wine_name': [None],
        'vintage_winery': [None],
        'vintage_country': [None],
        'vintage_region': [None],
        'vintage_wine_type': [0],
        'acidity': [0.0],
        'fizziness': [0.0],
        'intensity': [0.0],
        'sweetness': [0.0],
        'tannin': [0.0],
        'flavor': [None],
        'varietal_name': [None],
        'body_description': [None],
        'acidity_description': [None],
        'foods': [user_input]
    })

    user_input_df['foods'] = user_input_df['foods'].apply(lambda food: ', '.join(food) if isinstance(food, list) else food)
    # print(user_input_df)
    food_paring_df_new_added = pd.concat([food_paring_df, user_input_df], ignore_index=True)
    return food_paring_df_new_added

def weighted_rating(food_paring_df_new_added):
    C = food_paring_df_new_added['vintage_ratings_average'].mean()
    m = food_paring_df_new_added['vintage_ratings_count'].quantile(0.5)
    v = food_paring_df_new_added['vintage_ratings_count']
    R = food_paring_df_new_added['vintage_ratings_average']
    return (v / (v + m)) * R + (m / (v + m)) * C

def add_weighted_ratings_column(food_paring_df_new_added):
    food_paring_df_new_added['weighted_ratings'] = weighted_rating(food_paring_df_new_added)
    food_paring_df_new_added_wr = food_paring_df_new_added
    return food_paring_df_new_added_wr

def food_cosine_similarity_analysis(food_paring_df_new_added_wr, max_price, min_price):
    food_paring_df_new_added_wr['foods'] = food_paring_df_new_added_wr['foods'].fillna('')
    count_vectorizer = CountVectorizer(ngram_range=(1, 3))
    foods_vec = count_vectorizer.fit_transform(food_paring_df_new_added_wr['foods'])
    foods_sim = cosine_similarity(foods_vec, foods_vec)
    wine_idx_by_foods_sim = foods_sim.argsort(axis=1)[:, ::-1]

    wine_idx = len(food_paring_df_new_added_wr) - 1
    recommended_idx = wine_idx_by_foods_sim[wine_idx, : 100]
    recommended_idx = recommended_idx[recommended_idx != wine_idx]
    df_recommended = food_paring_df_new_added_wr.iloc[recommended_idx]
    df_recommended_price_range = df_recommended[(df_recommended['vintage_price'] > min_price) & (df_recommended['vintage_price'] < max_price)]
    df_recommended_ratings = df_recommended_price_range.sort_values(by='weighted_ratings', ascending=False)
    selected_columns = ['vintage_wine_name', 'vintage_price', 'vintage_country', 'vintage_wine_type', 'varietal_name','flavor','foods']
    df_selected = df_recommended_ratings[selected_columns].reset_index(drop=True)
    return df_selected.head(10)

def content_based_food_pairing(user_input, max_price, min_price):
    food_paring_df_new_added = concat_dataframe(user_input)
    food_paring_df_new_added_wr = add_weighted_ratings_column(food_paring_df_new_added)
    df_recommended_ratings = food_cosine_similarity_analysis(food_paring_df_new_added_wr, max_price, min_price)
    return df_recommended_ratings


# print(concat_dataframe(user_input))
# food_paring_df_new_added = concat_dataframe(user_input)
# weighted_rating_ = weighted_rating(food_paring_df_new_added)
# food_paring_df_new_added_wr = add_weighted_ratings_column(food_paring_df_new_added)
# print(food_paring_df_new_added_wr)
# df_recommended_ratings = food_cosine_similarity_analysis(food_paring_df_new_added_wr, max_price, min_price)
# print(df_recommended_ratings)
