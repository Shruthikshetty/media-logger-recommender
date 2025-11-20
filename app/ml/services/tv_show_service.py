# this file contains the service class for tv show
# its responsible for loading the model and providing a simple method to get recommendation

import pickle
import os
import logging

# build path to the model file
baseDir = os.path.abspath(os.path.dirname(__file__))
TV_SHOW_MODEL_PATH = os.path.join(baseDir, "..", "tv_show_model.pkl")


class TvShowService:
    # class variable to store the loaded model
    model = None

    @classmethod
    def getModel(cls):
        """Loads the tv show model into memory if its not already loaded."""
        if cls.model is None:
            try:
                with open(TV_SHOW_MODEL_PATH, "rb") as f:
                    cls.model = pickle.load(f)
            except FileNotFoundError:
                logging.error(f"Error: The file '{TV_SHOW_MODEL_PATH}' was not found.")
                cls.model = None
            except Exception as e:
                logging.error(f"An error occurred while loading the model: {e}")
                cls.model = None
        return cls.model

    @classmethod
    def predictSimilar(cls, tv_show_id, n=10):
        """
        This will predict similar tv shows to the id provided
        will return a list of tv show ids that are similar
        by default it will return 10 (n=10)
        """
        # load the model in case its not loaded
        model = cls.getModel()
        # if model is not loaded for some reason
        if model is None:
            raise RuntimeError("Model is not loaded")

        try:
            # get the similar tv shows and training df from the model
            similarity_matrix = model["similarity_matrix"]
            df = model["training_data"]

            # clean the input
            tv_show_id = tv_show_id.strip()

            # get index
            idx = df.index.get_loc(tv_show_id)

            # get similarity
            similarities = similarity_matrix[idx]
            # get top n
            top_indices = similarities.argsort()[::-1][1 : n + 1]
            similar_tv_shows = df.index[top_indices].tolist()
            return similar_tv_shows

        except KeyError:
            raise ValueError(f"tv show id '{tv_show_id}' not found in training data")

        except Exception as e:
            logging.error(f"An error occurred while generating recommendations: {e}")
            return []
