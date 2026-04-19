"""
core/analyzer.py
────────────────
Motor de análise central da aplicação.

Coordena o gerador (reader), as funções de extracção (extractor)
e acumula as contagens usando collections.Counter.

Expõe:
  - AnalisadorResultado  → dataclass com todos os resultados
  - analisar_ficheiro()  → função principal de análise
  - pesquisar_posts()    → pesquisa por palavra/hashtag/menção
"""

from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

from core.reader import ler_posts
from core.extractor import (
    extrair_hashtags,
    extrair_mencoes,
    extrair_urls,
    extrair_palavras,
)


@dataclass
class AnalisadorResultado:
    """
    Estrutura de dados que contém todos os resultados da análise.
    Usar dataclass torna o código mais limpo e autodocumentado.
    """
    contador_palavras:  Counter = field(default_factory=Counter)
    contador_hashtags:  Counter = field(default_factory=Counter)
    contador_mencoes:   Counter = field(default_factory=Counter)
    todas_urls:         set     = field(default_factory=set)
    total_urls:         int     = 0
    total_posts:        int     = 0
    posts_raw:          list    = field(default_factory=list)  # Para pesquisa

    # Estatísticas derivadas (calculadas após análise)
    @property
    def total_palavras_unicas(self) -> int:
        return len(self.contador_palavras)

    @property
    def total_hashtags_unicas(self) -> int:
        return len(self.contador_hashtags)

    @property
    def total_mencoes_unicas(self) -> int:
        return len(self.contador_mencoes)

    @property
    def total_urls_unicos(self) -> int:
        return len(self.todas_urls)


def analisar_ficheiro(caminho: str | Path) -> AnalisadorResultado:
    """
    Analisa o ficheiro de posts e retorna um AnalisadorResultado completo.

    Usa o gerador ler_posts() para processar linha a linha de forma
    eficiente, acumulando contagens com Counter.update().

    Args:
        caminho: Caminho para o ficheiro posts.txt.

    Returns:
        AnalisadorResultado com todas as contagens e entidades.
    """
    resultado = AnalisadorResultado()

    for post in ler_posts(caminho):
        resultado.total_posts += 1
        resultado.posts_raw.append(post)

        # Extrai entidades de cada post
        hashtags = extrair_hashtags(post)
        mencoes  = extrair_mencoes(post)
        urls     = extrair_urls(post)
        palavras = extrair_palavras(post)

        # Acumula contagens
        resultado.contador_palavras.update(palavras)
        resultado.contador_hashtags.update(hashtags)
        resultado.contador_mencoes.update(mencoes)

        # URLs: total (com repetição) e únicos (set)
        resultado.total_urls += len(urls)
        resultado.todas_urls.update(urls)

    return resultado


def pesquisar_posts(resultado: AnalisadorResultado, termo: str) -> list[tuple[int, str]]:
    """
    Pesquisa posts que contenham um determinado termo.

    Suporta pesquisa por:
      - Palavra comum     →  'python'
      - Hashtag           →  '#angola'
      - Menção            →  '@joaotech'

    Args:
        resultado: Resultado da análise já calculado.
        termo:     Termo de pesquisa (sem distinção de maiúsculas).

    Returns:
        Lista de tuplos (número_do_post, texto_do_post).
    """
    termo = termo.lower().strip()
    encontrados = []

    for i, post in enumerate(resultado.posts_raw, start=1):
        if termo in post:
            encontrados.append((i, post))

    return encontrados


def obter_estatisticas_avancadas(resultado: AnalisadorResultado) -> dict:
    """
    Calcula estatísticas adicionais sobre o corpus de posts.

    Returns:
        Dicionário com métricas avançadas.
    """
    total_palavras_corpus = sum(resultado.contador_palavras.values())
    total_hashtags_corpus = sum(resultado.contador_hashtags.values())
    total_mencoes_corpus  = sum(resultado.contador_mencoes.values())

    # Média de hashtags por post
    media_hashtags = round(total_hashtags_corpus / resultado.total_posts, 2) \
        if resultado.total_posts > 0 else 0

    # Hashtag mais usada
    top_hashtag = resultado.contador_hashtags.most_common(1)
    hashtag_dominante = f"#{top_hashtag[0][0]} ({top_hashtag[0][1]}x)" \
        if top_hashtag else 'N/A'

    return {
        'total_palavras_corpus':  total_palavras_corpus,
        'total_hashtags_corpus':  total_hashtags_corpus,
        'total_mencoes_corpus':   total_mencoes_corpus,
        'media_hashtags_por_post': media_hashtags,
        'hashtag_dominante':      hashtag_dominante,
        'diversidade_vocabulario': round(
            resultado.total_palavras_unicas / total_palavras_corpus * 100, 1
        ) if total_palavras_corpus > 0 else 0,
    }
