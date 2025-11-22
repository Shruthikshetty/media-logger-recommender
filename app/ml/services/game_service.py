# this file contains the
# service class that is responsible for loading your model.pkl
# providing a simple method to get recommendations.
# This abstracts the machine learning logic away from the API endpoint logic.

import pickle
import os
import logging

# build path to the model file
baseDir = os.path.abspath(os.path.dirname(__file__))
GAME_MODEL_PATH = os.path.join(baseDir, "..", "game_model.pkl")


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
    def predictSimilar(cls, game_id, n=10):
        """
        This will predict similar games to the id provided
        will return a list of game ids that are similar
        by default it will return 10 (n=10)
        """
        # load the model in case its not already loaded
        model = cls.getModel()

        # if model is not loaded
        if model is None:
            raise RuntimeError("Model is not loaded")

        # get the similar games
        try:
            # The Cosine Similarity Matrix)
            similarity_matrix = model["similarity_matrix"]
            df = model["training_data"]

            # clean the input
            game_id = game_id.strip()

            # get index
            idx = df.index.get_loc(game_id)

            # get similarity
            similarities = similarity_matrix[idx]
            # get top n
            top_indices = similarities.argsort()[::-1][1 : n + 1]
            similar_games = df.index[top_indices].tolist()
            return similar_games

        except KeyError:
            raise ValueError(f"game id '{game_id}' not found in training data")

        except Exception as e:
            logging.error(f"An error occurred while generating recommendations: {e}")
            raise Exception(f"An error occurred while generating recommendations: {e}")
