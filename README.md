# Anime Recommendation System

This is a content based anime recommendation system builty on myanimelist.net database available in [Kaggle](https://www.kaggle.com/datasets/hernan4444/anime-recommendation-database-2020).

The trained model is deployed as a streamlit web app:

<img src="bit.ly_anime_recommend.png" alt= "Streamlit web app" width="150" height="150" href="https://bit.ly/anime_recommend">

https://bit.ly/anime_recommend

Developed by: [Marcelo Vargas dos Santos](https://github.com/mvsantosdev)


Project content:

    -   similarity_model.ipynb : In this jupyter notebook I developed a model based on cosine similarity distance of the sinopses vectorized using the ti-idf nlp model.
    -   index.py : This is the script used by streamlit to deploy the webapp.
    -   utils.py : Implements utility functions, such as a web scraping to get an anime info from myanimelist.net.