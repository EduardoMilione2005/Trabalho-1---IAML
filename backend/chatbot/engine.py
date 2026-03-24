class ChatbotEngine:
    def __init__(self, user_id):
        self.user_id = user_id

    def get_response(self, message: str) -> str:
        if not message:
            return "Desculpe, não entendi. Pode repetir? Que tipo de filme você gosta?"

        return "Olá! Que tipo de filme você gosta? Pode ser ação, comédia ou terror 😊"