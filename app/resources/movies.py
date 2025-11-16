# this file contains all the resource endpoints for movies

from flask_restful import Resource, reqparse

# from app.ml.services.movie_service import MovieService


# class for similar endpoint api/similar/movies
class SimilarMovies(Resource):
    # get 10 similar movies from the provided movie id
    def get(self, id=None):
        # check if movie id is provided
        if id is None:
            return {"success": False, "message": "No movie id provided."}, 400
        
        return {"success": True, "similar_movies": []}, 200
