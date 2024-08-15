# app/content_based.py
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_product_features(filepath='data/product_features.csv'):
    """Load product features from a CSV file."""
    try:
        product_features = pd.read_csv(filepath, index_col='product_id')
        return product_features
    except FileNotFoundError:
        print(f"Error: The file {filepath} was not found.")
        return pd.DataFrame()
    except Exception as e:
        print(f"Error loading product features: {e}")
        return pd.DataFrame()

def content_based_recommendations(user_ratings, product_features):
    """Generate content-based recommendations based on product features."""
    if user_ratings.empty or product_features.empty:
        print("Error: Either user ratings or product features data is empty.")
        return []

    # Combine all features into a single string for each product
    product_features['combined_features'] = product_features.apply(lambda x: ' '.join(x.astype(str)), axis=1)
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(product_features['combined_features'])
    
    product_similarity = cosine_similarity(tfidf_matrix, tfidf_matrix)
    product_similarity_df = pd.DataFrame(product_similarity, index=product_features.index, columns=product_features.index)
    
    recommended_scores = {}
    
    for product_id in user_ratings.index:
        if pd.notna(user_ratings.get(product_id, None)):  # Use .get to handle missing product_ids
            similar_products = product_similarity_df.get(product_id, pd.Series())
            weighted_scores = similar_products * user_ratings[product_id]
            
            for idx, score in weighted_scores.items():
                if idx in recommended_scores:
                    recommended_scores[idx] += score
                else:
                    recommended_scores[idx] = score
    
    sorted_recommended_products = sorted(recommended_scores.items(), key=lambda x: x[1], reverse=True)
    recommended_product_ids = [product_id for product_id, score in sorted_recommended_products[:5]]
    
    return recommended_product_ids