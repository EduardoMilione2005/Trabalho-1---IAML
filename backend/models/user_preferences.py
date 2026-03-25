class UserPreferences:
    def __init__(self):
        self.generos = []

    def adicionar_genero(self, genero):
        if genero not in self.generos:
            self.generos.append(genero)