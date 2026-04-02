class UserPreferences:
    def __init__(self):
        self.genero = None
        self.ano = None
        self.duracao = None
        self.intensidade = None
        self.popularidade = None
        self.plot_twist = None

    def adicionar_genero(self, genero):
        self.genero = genero.lower()

    def definir_ano(self, valor):
        valor = valor.lower()
        if "novo" in valor or "recente" in valor:
            self.ano = "novo"
        elif "classico" in valor or "antigo" in valor:
            self.ano = "classico"

    def definir_duracao(self, valor):
        valor = valor.lower()
        if "curto" in valor:
            self.duracao = "curto"
        elif "longo" in valor:
            self.duracao = "longo"

    def definir_intensidade(self, valor):
        valor = valor.lower()
        if "leve" in valor:
            self.intensidade = "leve"
        elif "intenso" in valor:
            self.intensidade = "intenso"

    def definir_popularidade(self, valor):
        valor = valor.lower()
        if "popular" in valor:
            self.popularidade = "alta"
        elif "diferente" in valor or "menos conhecido" in valor:
            self.popularidade = "baixa"

    def definir_plot_twist(self, valor):
        valor = valor.lower()
        if "sim" in valor:
            self.plot_twist = "sim"
        elif "nao" in valor or "não" in valor:
            self.plot_twist = "nao"