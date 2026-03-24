import random

def identificar_intencao(mensagem: str) -> str:
    mensagem = mensagem.lower()

    if "ação" in mensagem:
        return "genero_acao"
    elif "comédia" in mensagem:
        return "genero_comedia"
    elif "terror" in mensagem:
        return "genero_terror"

    return "desconhecido"


def pergunta_continuidade():
    perguntas = [
        "Você prefere filmes mais novos ou clássicos?",
        "Quer recomendações parecidas com esse estilo?",
        "Prefere algo mais leve ou mais intenso?",
        "Já assistiu algum filme desse gênero?"
    ]
    return random.choice(perguntas)