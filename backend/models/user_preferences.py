import unicodedata

def normalizar_texto(texto: str) -> str:
    texto = texto.lower().strip()
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(c for c in texto if unicodedata.category(c) != "Mn")
    return texto

class UserPreferences:
    def __init__(self):
        self.genero = None
        self.ano = None
        self.duracao = None
        self.intensidade = None
        self.popularidade = None
        self.plot_twist = None

    def adicionar_genero(self, genero):
        self.genero = normalizar_texto(genero)

    def definir_ano(self, valor):
        valor = normalizar_texto(valor)
        if valor in ["novo", "novos", "recente", "recentes"]:
            self.ano = "novo"
        elif valor in ["classico", "classicos", "antigo", "antigos"]:
            self.ano = "classico"

    def definir_duracao(self, valor):
        valor = normalizar_texto(valor)
        if valor in ["curto", "curtos"]:
            self.duracao = "curto"
        elif valor in ["longo", "longos"]:
            self.duracao = "longo"

    def definir_intensidade(self, valor):
        valor = normalizar_texto(valor)
        if valor in ["leve", "leves"]:
            self.intensidade = "leve"
        elif valor in ["intenso", "intensos"]:
            self.intensidade = "intenso"

    def definir_popularidade(self, valor):
        valor = normalizar_texto(valor)
        if valor in ["popular", "populares"]:
            self.popularidade = "alta"
        elif valor in ["diferente", "diferentes", "menos conhecido", "menos conhecidos"]:
            self.popularidade = "baixa"

    def definir_plot_twist(self, valor):
        valor = normalizar_texto(valor)
        if valor in ["sim", "s", "yes"]:
            self.plot_twist = "sim"
        elif valor in ["nao", "não", "n"]:
            self.plot_twist = "nao"
