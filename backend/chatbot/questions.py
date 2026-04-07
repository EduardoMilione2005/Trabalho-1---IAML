import re
import unicodedata

def normalizar_texto(texto: str) -> str:
    """
    Converte texto para minúsculo, remove espaços extras e acentos.
    """
    texto = texto.lower().strip()
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(c for c in texto if unicodedata.category(c) != "Mn")
    return texto

def identificar_intencao(mensagem: str) -> str:
    """
    Identifica a intenção do usuário com base em palavras-chave.
    Usa regex com limites de palavra para gêneros, evitando confusões
    como 'acao' dentro de 'animacao'.
    """
    if not mensagem or not mensagem.strip():
        return "desconhecido"

    mensagem = normalizar_texto(mensagem)

    # Saudações
    if mensagem in ["oi", "ola", "bom dia", "boa tarde", "boa noite"]:
        return "saudacao"

    # Agradecimento
    if "obrigado" in mensagem or "valeu" in mensagem:
        return "agradecimento"

    generos = {
        "acao": ["acao"],
        "comedia": ["comedia", "engracado"],
        "terror": ["terror", "medo"],
        "drama": ["drama"],
        "romance": ["romance", "romantico"],
        "ficcao": ["ficcao", "scifi"],
        "animacao": ["animacao", "desenho"],
        "aventura": ["aventura"],
        "suspense": ["suspense", "misterio"]
    }

    for genero, palavras in generos.items():
        for palavra in palavras:
            padrao = r"\b" + re.escape(palavra) + r"\b"
            if re.search(padrao, mensagem):
                return f"genero_{genero}"

    if "filme" in mensagem or "recomenda" in mensagem or "indica" in mensagem:
        return "pedir_recomendacao"

    return "desconhecido"


perguntas = [
    ("ano", "Você prefere filmes mais novos ou clássicos?"),
    ("intensidade", "Prefere algo mais leve ou mais intenso?"),
    ("duracao", "Prefere filmes curtos ou longos?"),
    ("popularidade", "Quer sugestões populares ou diferentes?"),
    ("plot_twist", "Gosta de filmes com plot twist?")
]
