# this file contains all the resource endpoints for movies

from flask_restful import Resource

from app.ml.services.tv_show_service import TvShowService


# class for similar endpoint api/similar/tv-shows
class SimilarTVShows(Resource):
    def get(self, id=None):
        """
        This will predict similar tv shows to the id provided
        will return a list of tv show ids that are similar
        it will return 10
        """
        # check if tv show id is provided
        if id is None:
            return {"success": False, "message": "No tv show id provided."}, 400

        try:
            # predict similar tv shows
            similar_tv_shows = TvShowService.predictSimilar(id, n=10)
            return {"success": True, "similar_tv_shows": similar_tv_shows}, 200

        except ValueError as e:
            return {"success": False, "message": str(e)}, 404

        except Exception as e:
            return {"success": False, "message": str(e)}, 500
