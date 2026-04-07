import json
import os


class Recommender:
    def __init__(self):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        file_path = os.path.join(base_dir, "data", "movies.json")

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                self.movies = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.movies = []

    def recomendar_por_preferencias(self, preferences):
        if not self.movies:
            return []

        resultados = []

        filmes_filtrados = [
            filme for filme in self.movies
            if preferences.genero is None or filme.get("genero") == preferences.genero
        ]

        for filme in filmes_filtrados:
            score = 0

            if preferences.ano in ["novo", "novos"] and filme.get("ano", 0) >= 2010:
                score += 1
            elif preferences.ano in ["classico", "clássico", "classicos", "clássicos"] and filme.get("ano", 0) < 2010:
                score += 1

            if preferences.intensidade in ["leve", "leves"] and filme.get("leve_ou_intenso") == "leve":
                score += 2
            elif preferences.intensidade in ["intenso", "intensos"] and filme.get("leve_ou_intenso") == "intenso":
                score += 2

            if preferences.duracao in ["curto", "curtos"] and filme.get("duracao", 0) <= 120:
                score += 1
            elif preferences.duracao in ["longo", "longos"] and filme.get("duracao", 0) > 120:
                score += 1

            if preferences.popularidade in ["popular", "populares"] and filme.get("popularidade") == "alta":
                score += 1
            elif preferences.popularidade in ["diferente", "diferentes"] and filme.get("popularidade") in ["media",
                                                                                                           "baixa"]:
                score += 1

            if preferences.plot_twist is not None and filme.get("plot_twist") == preferences.plot_twist:
                score += 2

            resultados.append((filme, score))

        resultados.sort(key=lambda x: (x[1], x[0].get("nota", 0)), reverse=True)

        filmes_ordenados = [filme for filme, score in resultados]

        if preferences.plot_twist is not None:
            return filmes_ordenados[:1]

        return filmes_ordenados[:3]
