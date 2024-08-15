# Personalized Recommendation System

![Status](https://img.shields.io/badge/status-under_construction-yellow)

This project is a personalized recommendation system that uses a hybrid approach to suggest products or content to users. The system combines collaborative filtering based on user similarities and sentiment analysis to adjust recommendations according to user preferences detected in reviews.

## 🚧 Project Status

**This project is currently under active development.** Some features may not be fully implemented, and the system might undergo significant changes as improvements are made. Please feel free to explore, provide feedback, or contribute!

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Overview

The personalized recommendation system is designed to provide users with tailored product recommendations based on their ratings and reviews. It leverages machine learning techniques and natural language processing (NLP) to deliver accurate and relevant suggestions.

## Features
- **Collaborative Filtering**: Recommends products based on similarities between users' ratings.
- **Content-Based Filtering**: Suggests products based on product features and user preferences.
- **Sentiment Analysis**: Analyzes user reviews to further refine recommendations.
- **Web Interface**: Users can log in, view their recommendations, and adjust preferences.
- **Docker Support**: The application is containerized using Docker for easy deployment.

## Technologies Used
- **Python 3.10**
- **Flask**: Web framework used to build the web interface.
- **Pandas & NumPy**: Data manipulation and numerical operations.
- **scikit-learn**: Machine learning algorithms.
- **Transformers & PyTorch**: NLP for sentiment analysis.
- **Docker**: Containerization of the application.
- **HTML & CSS**: Front-end design and layout.

## Installation

### Prerequisites
- [Docker](https://www.docker.com/products/docker-desktop) installed on your machine.
- [Git](https://git-scm.com/) for version control.

### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/MarBenitez/recommendation-system-docker
    cd recommendation-system-docker
    ```

2. Build the Docker image:
    ```bash
    docker-compose up --build
    ```

3. The application should now be running on `http://localhost:8081`.

## Usage

1. Open your web browser and navigate to `http://localhost:8081`.
2. Enter your user ID to get personalized recommendations.
3. View the recommended products and adjust your preferences.

## Project Structure
```
├── app
│ ├── static
│ │ └── style.css # CSS for styling the web pages
│ ├── templates
│ │ ├── index.html # Homepage template
│ │ └── recommendations.html # Recommendations page template
│ ├── collaborative_filtering.py # Collaborative filtering logic
│ ├── content_based.py # Content-based filtering logic
│ ├── sentiment_analysis.py # Sentiment analysis logic
│ ├── user_profiles.py # User profile generation
│ ├── routes.py # Flask routes and view functions
│ └── app.py # Flask application factory
├── data
│ ├── product_features.csv # CSV file with product features
│ ├── product_reviews.csv # CSV file with user reviews
│ └── user_ratings.csv # CSV file with user ratings
├── models
│ ├── ber_model_hf.py # Model loading and sentiment prediction
├── docker-compose.yml # Docker Compose file
├── Dockerfile # Dockerfile for building the image
├── requirements.txt # Python dependencies
└── README.md # Project documentation
´´´

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request with your changes.

### Steps to Contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
