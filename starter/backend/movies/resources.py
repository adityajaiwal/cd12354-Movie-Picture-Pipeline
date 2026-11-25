from flask import jsonify, request
from flask.views import MethodView

# Dummy database to hold movie examples
movies = {
    "123": {"title": "Top Gun: Maverick", "description": "Fighter planes"},
    "456": {"title": "Sonic the Hedgehog", "description": "Blue Sega character"},
    "789": {"title": "A Quiet Place", "description": "Scary monsters"},
}


class Movies(MethodView):
    def get(self, movie_id):
        if movie_id is None:
            # Return a list of all movies
            return jsonify({"movies": [dict({"title": movie["title"]}, **{"id": i}) for i, movie in movies.items()]})
        else:
            # Return the details of a specific movie
            return jsonify({"movie": movies[str(movie_id)]})

    def post(self):
        data = request.get_json()

        movie_id = data.get("id")
        movies[movie_id] = {
            "title": data.get("title"),
            "description": data.get("description")
        }

        return jsonify({"movie": movies[movie_id]}), 201

    def delete(self, movie_id):
        movie_id = str(movie_id)

        if movie_id not in movies:
            return jsonify({"message": "Movie not found"}), 404

        deleted_movie = movies.pop(movie_id)

        return jsonify({
            "message": "Movie deleted successfully",
            "movie": deleted_movie
        }), 200

    def put(self, movie_id):
        data = request.get_json()

        movie_id = str(movie_id)

        if movie_id not in movies:
            return jsonify({"message": "Movie not found"}), 404

        movies[movie_id] = {
            "title": data.get("title"),
            "description": data.get("description")
        }

        return jsonify({"movie": movies[movie_id]}), 200
