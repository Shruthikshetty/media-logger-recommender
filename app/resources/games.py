# this file contains all the resource endpoints for games

from flask_restful import Resource, reqparse
from app.ml.services.game_service import GameService


class SimilarGames(Resource):

    # get 10 similar games for the provided game title
    def post(self):
        # set up parser
        parser = reqparse.RequestParser()
        parser.add_argument(
            "title", type=str, help="Title of the game", required=True, location="json"
        )

        args = parser.parse_args()
        game_title = args["title"]    

        # load the model
        GameService.getModel()

        # get similar games
        similar_games = GameService.predictSimilar(game_title)

        if len(similar_games) == 0:
            return {"success": False, "message": "No similar games found."}, 404

        return {"success": True, "similar_games": similar_games}, 200
