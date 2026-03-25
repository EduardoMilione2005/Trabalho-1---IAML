import json
import os


class Recommender:
    def __init__(self):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        file_path = os.path.join(base_dir, "data", "movies.json")

        with open(file_path, "r", encoding="utf-8") as f:
            self.movies = json.load(f)

    def recomendar_por_genero(self, genero):
        return [
            filme for filme in self.movies
            if filme["genero"] == genero
        ]