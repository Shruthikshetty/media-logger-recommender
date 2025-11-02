# this file contains the
# service class that is responsible for loading your model.pkl
# providing a simple method to get recommendations.
# This abstracts the machine learning logic away from the API endpoint logic.

import pickle
import os
import logging

# build path to the model file
baseDir = os.path.abspath(os.path.dirname(__file__))
GAME_MODEL_PATH = os.path.join(baseDir, '..', 'game_model.pkl')


class GameService:
    # class variable to hold the game model
    model = None

    @classmethod
    def getModel(cls):
        """Loads the game model into memory if its not already loaded."""
        if cls.model is None:
            try:
                with open(GAME_MODEL_PATH, "rb") as f:
                    cls.model = pickle.load(f)
            except FileNotFoundError:
                logging.error(f"Error: The file '{GAME_MODEL_PATH}' was not found.")
                cls.model = None
            except Exception as e:
                logging.error(f"An error occurred while loading the model: {e}")
                cls.model = None
        return cls.model

    @classmethod
    def predictSimilar(cls, game_title, n=10):
        model = cls.getModel()

        # if model is not loaded
        if model is None:
            return []

        # get the similar games
        try:
            # The Cosine Similarity Matrix)
            cosine_sim = model["similarity_matrix"]
            # the cleaned dataframe
            df = model["df"]
            # The Title-to-Index Mapping
            indices = model["indices"]
            # get the index of the game title
            idx = indices[game_title]
            # It sorts this list of tuples in descending order based on the similarity score
            sim_scores = list(enumerate(cosine_sim[idx]))
            sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
            sim_scores = sim_scores[1 : n + 1]
            game_indices = [i[0] for i in sim_scores]
            # return the top n similar games
            similar_games = df["title"].iloc[game_indices]
            return similar_games.to_list()  # return as a list
        
        except Exception as e:
            logging.error(f"An error occurred while generating recommendations: {e}")
            return []
