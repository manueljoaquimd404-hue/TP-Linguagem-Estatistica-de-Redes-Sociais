"""
core/reader.py
──────────────
Gerador responsável pela leitura eficiente do ficheiro de posts.

Usa yield para processar o ficheiro linha por linha sem carregar
todo o conteúdo na memória — ideal para ficheiros de grande dimensão.
"""

from pathlib import Path
from typing import Generator


def ler_posts(caminho: str | Path) -> Generator[str, None, None]:
    """
    Gerador que lê e pré-processa cada post do ficheiro.

    Passos de pré-processamento por linha:
      1. Remove espaços em branco nas extremidades.
      2. Ignora linhas vazias.
      3. Converte para minúsculas.
      4. Remove pontuação básica (preserva # @ / : . para entidades).

    Args:
        caminho: Caminho para o ficheiro de posts (.txt).

    Yields:
        str: Cada post pré-processado, pronto para extracção.

    Raises:
        FileNotFoundError: Se o ficheiro não existir.
    """
    # Pontuação a eliminar — exclui os caracteres usados em entidades
    pontuacao = '!"$%&\'()*+,;<=>?[\\]^_`{|}~'
    tabela_remocao = str.maketrans('', '', pontuacao)

    with open(caminho, 'r', encoding='utf-8') as f:
        for linha in f:
            linha = linha.strip()
            if not linha:
                continue
            linha = linha.lower()
            linha = linha.translate(tabela_remocao)
            yield linha


def contar_linhas(caminho: str | Path) -> int:
    """
    Conta o número total de posts (linhas não vazias) no ficheiro.

    Args:
        caminho: Caminho para o ficheiro.

    Returns:
        int: Número de posts.
    """
    return sum(1 for _ in ler_posts(caminho))
