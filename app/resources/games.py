# this file contains all the resource endpoints for games

from flask_restful import Resource, reqparse
from app.ml.services.game_service import GameService


class SimilarGames(Resource):

    def get(self, id=None):
        """
        This will predict similar games to the game id provided
        will return a list of 10 game ids that are similar
        """
        # get n from the request
        parser = reqparse.RequestParser()
        parser.add_argument("n", type=int, location="args", default=10)
        args = parser.parse_args()
        n = args["n"]

        try:
            # predict similar games
            similar_games = GameService.predictSimilar(id, n=n)
            return {"success": True, "similar_games": similar_games}, 200

        except ValueError as e:
            return {"success": False, "message": str(e)}, 404

        except Exception as e:
            return {"success": False, "message": str(e)}, 500
