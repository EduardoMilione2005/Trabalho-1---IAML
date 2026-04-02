def identificar_intencao(mensagem: str) -> str:
    mensagem = mensagem.lower()

    if mensagem in ["oi", "ola", "olá", "bom dia", "boa tarde", "boa noite"]:
        return "saudacao"

    if "obrigado" in mensagem or "valeu" in mensagem:
        return "agradecimento"

    generos = {
        "acao": ["acao", "ação"],
        "comedia": ["comedia", "comédia", "engraçado"],
        "terror": ["terror", "medo"],
        "drama": ["drama"],
        "romance": ["romance", "romantico"],
        "ficcao": ["ficcao", "ficção", "sci-fi"],
        "animacao": ["animacao", "animação", "desenho"],
        "aventura": ["aventura"],
        "suspense": ["suspense", "mistério", "misterio"]
    }

    for genero, palavras in generos.items():
        for palavra in palavras:
            if palavra in mensagem:
                return f"genero_{genero}"

    return "resposta"


perguntas = [
    ("ano", "Você prefere filmes mais novos ou clássicos?"),
    ("intensidade", "Prefere algo mais leve ou mais intenso?"),
    ("duracao", "Prefere filmes curtos ou longos?"),
    ("popularidade", "Quer sugestões populares ou diferentes?"),
    ("plot_twist", "Gosta de filmes com plot twist?")
]