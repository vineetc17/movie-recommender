# Movie Recommedation System

## Working Model
https://mrs-vineetc17-d843d3a68cb6.herokuapp.com/

## Overview
This project is an interactive movie recommendation system that suggests movies based on user preferences. It leverages machine learning, natural language processing, and various APIs to provide an engaging and user-friendly experience.

## Technologies Used
- **Streamlit**: For creating the interactive web interface.
- **Python**: Core programming language used.
  - **pandas**: For data manipulation and processing.
  - **numpy**: For numerical computations.
  - **requests**: For making API calls.
  - **pickle**: For saving and loading machine learning models.
- **scikit-learn**: For implementing the machine learning algorithms.
- **TMDB API**: For fetching movie posters and additional movie information.
- **Natural Language Processing (NLP)**: To handle and process textual data.

## Features
- **Interactive Web Interface**: Built with Streamlit to provide an intuitive user experience.
- **Data Preprocessing**: Cleaned and preprocessed movie data from TMDB datasets.
- **NLP Techniques**: Used to process movie overviews and metadata.
- **Machine Learning Model**: 
  - Built using cosine similarity to recommend movies.
  - Suggests the top 5 movies similar to the user's selection.
- **API Integration**: 
  - Fetches movie posters and details dynamically from the TMDB API.
  - Ensures up-to-date and relevant movie information.
- **Error Handling**: Robust handling of cases where movies are not found in the dataset.

## How It Works
1. **Data Preparation**: 
   - Reads movie and credits data from CSV files.
   - Processes and merges datasets to create a comprehensive dataset for recommendations.
2. **Model Building**:
   - Computes similarity between movies using cosine similarity.
   - Saves the similarity model using pickle.
3. **Web Application**:
   - Users can select a movie from a dropdown menu.
   - The system recommends 5 similar movies and displays their titles and posters.
4. **API Calls**:
   - Fetches posters and movie details using the TMDB API based on movie IDs.

## Getting Started
### Prerequisites
- Python 3.x
- Required Python libraries: Streamlit, pandas, numpy, requests, scikit-learn

### Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/vineetc17/movie-recommendation-system.git
