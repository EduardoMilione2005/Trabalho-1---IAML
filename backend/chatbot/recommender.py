import json

class Recommender:
    def _init_(self, path="backend/data/movies.json"):
        with open(path, "r", encoding="utf-8") as f:
            self.movies = json.load(f)

    def recomendar_por_genero(self, genero):
        return [
            filme for filme in self.movies
            if filme["genero"] == genero
        ]