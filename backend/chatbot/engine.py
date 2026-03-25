from backend.chatbot.questions import identificar_intencao, pergunta_continuidade
from backend.chatbot.recommender import Recommender
from backend.models.user_preferences import UserPreferences


class ChatbotEngine:
    def __init__(self, user_id):
        print("DEBUG: Engine carregado corretamente")
        self.user_id = user_id
        self.preferences = UserPreferences()
        self.recommender = Recommender()

    def get_response(self, message: str) -> str:
        if not message:
            return "Desculpe, não entendi. Pode repetir? Que tipo de filme você gosta?"

        intencao = identificar_intencao(message)

        if intencao.startswith("genero"):
            genero = intencao.split("_")[1]

            self.preferences.adicionar_genero(genero)

            recomendacoes = self.recommender.recomendar_por_genero(genero)

            if recomendacoes:
                filmes = ", ".join([f["titulo"] for f in recomendacoes])

                return (
                    f"Encontrei alguns filmes de {genero}: {filmes}. "
                    f"{pergunta_continuidade()}"
                )

            return f"Não encontrei filmes de {genero}. Quer tentar outro gênero?"

        return "Você pode me dizer um gênero? (ação, comédia, terror)"
