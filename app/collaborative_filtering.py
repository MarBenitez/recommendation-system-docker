# app/collaborative_filtering.py
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def load_user_ratings(filepath='data/user_ratings.csv'):
    """Load user ratings from a CSV file."""
    try:
        user_ratings = pd.read_csv(filepath, index_col='user_id')
        return user_ratings
    except FileNotFoundError:
        print(f"Error: The file {filepath} was not found.")
        return pd.DataFrame()
    except Exception as e:
        print(f"Error loading user ratings: {e}")
        return pd.DataFrame()

def collaborative_filtering(user_id, user_ratings):
    """Perform collaborative filtering to generate recommendations."""
    if user_ratings.empty:
        print("Error: User ratings data is empty.")
        return []

    if user_id not in user_ratings.index:
        print(f"Error: User ID {user_id} not found in the data.")
        return []
    
    # Compute cosine similarity between users
    user_similarity = cosine_similarity(user_ratings.fillna(0))
    
    # Identify similar users
    user_index = user_ratings.index.get_loc(user_id)
    similar_users = user_similarity[user_index]
    
    # Weighted recommendations based on similar users
    weighted_ratings = np.dot(similar_users, user_ratings.fillna(0))
    recommended_products = np.argsort(weighted_ratings)[::-1]
    
    return recommended_products[:5]  # Return top 5 recommendations