import random
from backend.chatbot.questions import identificar_intencao, perguntas
from backend.chatbot.recommender import Recommender
from backend.models.user_preferences import UserPreferences


class ChatbotEngine:
    def __init__(self, user_id):
        self.user_id = user_id
        self.preferences = UserPreferences()
        self.recommender = Recommender()
        self.estado = "inicio"
        self.pergunta_atual = 0

        self.boas_vindas = [
            "Olá! Eu sou um chatbot de recomendação de filmes.",
            "Oi! Posso te ajudar a encontrar um filme para assistir.",
            "Seja bem-vindo! Vamos encontrar um filme para você.",
        ]

    def fazer_pergunta(self):
        if self.pergunta_atual < len(perguntas):
            return perguntas[self.pergunta_atual][1]
        else:
            return None

    def salvar_resposta(self, message):
        if self.pergunta_atual >= len(perguntas):
            return None

        tipo = perguntas[self.pergunta_atual][0]
        msg = message.lower().strip()
        valido = False

        if tipo == "ano":
            if "novo" in msg or "recente" in msg:
                self.preferences.definir_ano(msg)
                valido = True
            elif "classico" in msg or "antigo" in msg:
                self.preferences.definir_ano(msg)
                valido = True

        elif tipo == "intensidade":
            if "leve" in msg:
                self.preferences.definir_intensidade(msg)
                valido = True
            elif "intenso" in msg:
                self.preferences.definir_intensidade(msg)
                valido = True

        elif tipo == "duracao":
            if "curto" in msg:
                self.preferences.definir_duracao(msg)
                valido = True
            elif "longo" in msg:
                self.preferences.definir_duracao(msg)
                valido = True

        elif tipo == "popularidade":
            if "popular" in msg:
                self.preferences.definir_popularidade(msg)
                valido = True
            elif "diferente" in msg or "menos conhecido" in msg:
                self.preferences.definir_popularidade(msg)
                valido = True

        elif tipo == "plot_twist":
            if "sim" in msg:
                self.preferences.definir_plot_twist(msg)
                valido = True
            elif "nao" in msg or "não" in msg:
                self.preferences.definir_plot_twist(msg)
                valido = True

        if valido:
            self.pergunta_atual += 1
            return None
        else:
            return f"Não entendi sua resposta. {perguntas[self.pergunta_atual][1]}"

    def recomendar(self):
        recomendacoes = self.recommender.recomendar_por_preferencias(self.preferences)

        if not recomendacoes:
            return "Ainda estou refinando... me diga mais preferências!"

        if self.preferences.plot_twist is not None:
            filme = recomendacoes[0]
            return (
                f"Filme perfeito para você:\n"
                f"\n🎥 {filme['titulo']} ({filme['ano']})\n"
                f"⭐ Nota: {filme['nota']}/10\n"
                f"⏱️ Duração: {filme['duracao']} minutos"
            )

        nomes = ", ".join([f["titulo"] for f in recomendacoes])
        return f"🎬 Sugestões atuais: {nomes}"

    def get_response(self, message: str) -> str:
        if not message or not message.strip():
            return "Pode repetir? Não entendi muito bem."

        intencao = identificar_intencao(message)

        if self.estado == "fazendo_perguntas":
            resposta = self.salvar_resposta(message)

            if resposta:
                return resposta

            recomendacao = self.recomendar()
            proxima = self.fazer_pergunta()

            if proxima:
                return proxima
            else:
                self.estado = "recomendando"
                return recomendacao + "\n\nQuer outra recomendação?"

        if self.estado == "recomendando":
            if "sim" in message.lower() or "quero" in message.lower():
                self.pergunta_atual = 0
                self.preferences = UserPreferences()
                self.estado = "aguardando_genero"
                return "Vamos recomeçar! Qual gênero de filme você gosta?"

            if "nao" in message.lower() or "não" in message.lower():
                return "Tudo bem! Quando quiser é só pedir recomendações."

        if self.estado == "inicio":
            if not message.strip():
                return random.choice(self.boas_vindas) + " Me diga um gênero de filme para começarmos!"
            else:
                self.estado = "aguardando_genero"
                return random.choice(self.boas_vindas) + " Qual gênero de filme você gosta?"

        if intencao == "pedir_recomendacao":
            self.estado = "aguardando_genero"
            return "Claro! Qual gênero de filme você prefere? (ação, comédia, terror...)"

        if intencao.startswith("genero"):
            genero = intencao.split("_")[1]

            self.preferences = UserPreferences()
            self.pergunta_atual = 0

            self.preferences.adicionar_genero(genero)
            self.estado = "fazendo_perguntas"

            pergunta = self.fazer_pergunta()

            if pergunta:
                return f"Ótimo! Você gosta de {genero}. {pergunta}"
            else:
                return f"Ótimo! Você gosta de {genero}."

        if intencao == "agradecimento":
            self.estado = "aguardando_genero"
            return "Por nada! 😊 Quer mais recomendações? Me diga um gênero!"

        return "Não entendi muito bem 🤔. Você pode me dizer um gênero de filme?"
