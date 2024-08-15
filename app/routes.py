# app/routes.py
from flask import Blueprint, render_template, request
import pandas as pd
from app.user_profiles import personalized_recommendations
from app.collaborative_filtering import load_user_ratings
from app.content_based import load_product_features

main = Blueprint('main', __name__)

@main.route('/')
def index():
    """Render the index page where users can enter their User ID."""
    return render_template('index.html')

@main.route('/recommendations', methods=['POST'])
def recommendations():
    """Generate recommendations for the user based on their reviews and ratings."""
    user_id = int(request.form['user_id'])
    user_ratings = load_user_ratings()
    product_features = load_product_features()
    
    # Load the user's reviews from the product_reviews.csv file
    reviews_df = pd.read_csv('data/product_reviews.csv')
    user_reviews = reviews_df[reviews_df['user_id'] == user_id]['review'].tolist()
    
    # Get personalized recommendations
    recommended_products = personalized_recommendations(user_id, user_ratings, product_features, user_reviews)
    
    return render_template('recommendations.html', recommendations=recommended_products)
