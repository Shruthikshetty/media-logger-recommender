# this file contains all the resource endpoints for movies

from flask_restful import Resource

# class for similar endpoint api/similar/tv-shows
class SimilarTVShows(Resource):
    def get(self , id = None):
        """
        This will predict similar tv shows to the id provided
        will return a list of tv show ids that are similar
        it will return 10
        """
        return {"success": True, "similar_tv_shows": []}, 200