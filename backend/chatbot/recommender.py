import json
import os


class Recommender:
    def __init__(self):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        file_path = os.path.join(base_dir, "data", "movies.json")

        with open(file_path, "r", encoding="utf-8") as f:
            self.movies = json.load(f)

    def recomendar_por_preferencias(self, preferences):
        resultados = []

        filmes_filtrados = [
            filme for filme in self.movies
            if preferences.genero is None or filme["genero"] == preferences.genero
        ]

        for filme in filmes_filtrados:
            score = 0

            if preferences.ano == "novo" and filme["ano"] >= 2010:
                score += 1
            elif preferences.ano == "classico" and filme["ano"] < 2010:
                score += 1

            if preferences.intensidade and filme["leve_ou_intenso"] == preferences.intensidade:
                score += 2

            if preferences.duracao == "curto" and filme["duracao"] <= 120:
                score += 1
            elif preferences.duracao == "longo" and filme["duracao"] > 120:
                score += 1

            if preferences.popularidade == "popular" and filme["popularidade"] == "alta":
                score += 1
            elif preferences.popularidade == "diferente" and filme["popularidade"] in ["media", "baixa"]:
                score += 1

            if preferences.plot_twist and filme["plot_twist"] == preferences.plot_twist:
                score += 2

            resultados.append((filme, score))

        resultados.sort(key=lambda x: (x[1], x[0]["nota"]), reverse=True)

        filmes_ordenados = [filme for filme, score in resultados]

        if preferences.plot_twist is not None:
            return filmes_ordenados[:1]

        return filmes_ordenados[:3]