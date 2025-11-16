# this file contains the service class for movies
# its responsible for loading the model and providing a simple method to get recommendations

import pickle
import os
import logging

# build path to the model file
baseDir = os.path.abspath(os.path.dirname(__file__))
MOVIE_MODEL_PATH = os.path.join(baseDir, "..", "movie_model.pkl")


class MovieService:
    # class variable to store the loaded model
    model = None

    @classmethod
    def getModel(cls):
        """Loads the movie model into memory if its not already loaded."""
        if cls.model is None:
            try:
                with open(MOVIE_MODEL_PATH, "rb") as f:
                    cls.model = pickle.load(f)
            except FileNotFoundError:
                logging.error(f"Error: The file '{MOVIE_MODEL_PATH}' was not found.")
                cls.model = None
            except Exception as e:
                logging.error(f"An error occurred while loading the model: {e}")
                cls.model = None
        return cls.model

    @classmethod
    def predictSimilar(cls, movie_id, n=10):
        """
        This will predict similar movies to the id provided
        will return a list of movie ids that are similar
        by default it will return 10
        """
        # load the model in case its not already loaded
        model = cls.getModel()
        # if model is not loaded
        if model is None:
            return []

        try:
            # get the similar movies and training df from the model
            similarity_matrix = model["similarity_matrix"]
            df = model["training_data"]

            # clean the input
            movie_id = movie_id.strip()  

            # get index 
            idx = df.index.get_loc(movie_id)

            # get similarity
            similarities = similarity_matrix[idx]
            # get top n
            top_indices = similarities.argsort()[::-1][1:n+1]
            similar_movies = df.index[top_indices].tolist()
            return similar_movies


        except Exception as e:
            logging.error(f"An error occurred while generating recommendations: {e}")
            return []
