"""
core/extractor.py
─────────────────
Funções de extracção de entidades usando expressões regulares.

Cada função é responsável por um único tipo de entidade:
  - Hashtags  →  #palavra
  - Menções   →  @usuario
  - URLs      →  https://...  ou  http://...
  - Palavras  →  tokens de texto comum (sem entidades, sem stopwords)
"""

import re
import string
from core.stopwords import STOPWORDS

# ──────────────────────────────────────────────────────────────
# Padrões regex compilados uma única vez (melhor performance)
# ──────────────────────────────────────────────────────────────

_RE_HASHTAG = re.compile(
    r'#([a-záéíóúàâêôãõüçñ_a-z0-9]+)',
    re.IGNORECASE
)

_RE_MENCAO = re.compile(
    r'@([a-záéíóúàâêôãõüçñ_a-z0-9]+)',
    re.IGNORECASE
)

_RE_URL = re.compile(
    r'https?://[^\s]+',
    re.IGNORECASE
)


# ──────────────────────────────────────────────────────────────
# Funções públicas de extracção
# ──────────────────────────────────────────────────────────────

def extrair_hashtags(texto: str) -> list[str]:
    """
    Extrai todas as hashtags de um post.

    Exemplo:
        '#python é incrível #dados' → ['python', 'dados']

    Args:
        texto: Post pré-processado (minúsculas).

    Returns:
        Lista de hashtags sem o símbolo '#'.
    """
    return _RE_HASHTAG.findall(texto)


def extrair_mencoes(texto: str) -> list[str]:
    """
    Extrai todas as menções (@utilizador) de um post.

    Exemplo:
        'obrigado @AnaMaria!' → ['anamaria']

    Args:
        texto: Post pré-processado.

    Returns:
        Lista de nomes de utilizador sem o símbolo '@'.
    """
    return _RE_MENCAO.findall(texto)


def extrair_urls(texto: str) -> list[str]:
    """
    Extrai todos os URLs (http/https) de um post.

    Args:
        texto: Post pré-processado.

    Returns:
        Lista de URLs completos encontrados.
    """
    return _RE_URL.findall(texto)


def extrair_palavras(texto: str) -> list[str]:
    """
    Extrai palavras comuns de um post, excluindo entidades e stopwords.

    Processo:
      1. Remove URLs, hashtags e menções do texto.
      2. Tokeniza por espaços.
      3. Filtra tokens com menos de 3 caracteres.
      4. Filtra tokens não-alfabéticos.
      5. Remove stopwords.

    Args:
        texto: Post pré-processado.

    Returns:
        Lista de palavras relevantes.
    """
    # Remove entidades especiais do texto
    limpo = _RE_URL.sub('', texto)
    limpo = _RE_HASHTAG.sub('', limpo)
    limpo = _RE_MENCAO.sub('', limpo)

    palavras = []
    for token in limpo.split():
        token = token.strip(string.punctuation)
        if len(token) >= 3 and token.isalpha() and token not in STOPWORDS:
            palavras.append(token)

    return palavras
