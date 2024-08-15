# app/user_profiles.py
import pandas as pd
from app.collaborative_filtering import collaborative_filtering
from app.sentiment_analysis import analyze_sentiment
from app.content_based import content_based_recommendations

def generate_user_profile(user_id, reviews):
    """Generate a user profile based on their reviews."""
    sentiments = [analyze_sentiment(review) for review in reviews]
    return {'user_id': user_id, 'sentiments': sentiments}

def personalized_recommendations(user_id, user_ratings, product_features, reviews):
    """Generate personalized recommendations based on collaborative filtering and content-based methods."""
    profile = generate_user_profile(user_id, reviews)
    collaborative_recs = collaborative_filtering(user_id, user_ratings)
    content_recs = content_based_recommendations(user_ratings, product_features)
    
    # Convert to hashable types (e.g., integers) before intersecting
    collaborative_recs = [int(product_id) for product_id in collaborative_recs.flatten()]
    content_recs = [int(product_id) for product_id in content_recs]
    
    combined_recommendations = list(set(collaborative_recs).intersection(set(content_recs)))
    
    if not combined_recommendations:
        combined_recommendations = collaborative_recs + content_recs
    
    print(f"Final Combined Recommendations: {combined_recommendations}")
    
    return combined_recommendations