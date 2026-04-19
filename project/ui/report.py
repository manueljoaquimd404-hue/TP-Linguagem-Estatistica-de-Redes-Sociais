"""Renderizacao de relatorios com foco em leitura rapida."""

from core.analyzer import AnalisadorResultado, obter_estatisticas_avancadas
from ui.terminal import Cor, colorir

LARGURA = 70


def mostrar_cabecalho():
    """Mostra o cabecalho principal."""
    print(colorir('ANALISADOR DE REDES SOCIAIS', Cor.BOLD, Cor.CIANO))
    print(colorir('Trabalho Pratico 1.1', Cor.DIM))
    print(colorir('-' * LARGURA, Cor.CINZA))


def _titulo_secao(titulo: str):
    print()
    print(colorir(titulo, Cor.BOLD))
    print(colorir('-' * LARGURA, Cor.CINZA))


def _linha_chave_valor(chave: str, valor: str | int | float):
    print(f'{chave:<30} : {valor}')


def _imprimir_ranking(itens: list[tuple[str, int]], top_n: int, prefixo: str = ''):
    if not itens:
        print('Sem dados para mostrar.')
        return

    print(f"{'N':>2}  {'Item':<45} {'Freq':>6}")
    print(colorir('-' * LARGURA, Cor.CINZA))
    for pos, (item, contagem) in enumerate(itens[:top_n], start=1):
        print(f'{pos:>2}  {prefixo}{item:<45} {contagem:>6}')


def relatorio_resumo(resultado: AnalisadorResultado):
    stats = obter_estatisticas_avancadas(resultado)

    _titulo_secao('Resumo Geral')
    _linha_chave_valor('Posts analisados', resultado.total_posts)
    _linha_chave_valor('Palavras unicas', resultado.total_palavras_unicas)
    _linha_chave_valor('Hashtags unicas', resultado.total_hashtags_unicas)
    _linha_chave_valor('Mencoes unicas', resultado.total_mencoes_unicas)
    _linha_chave_valor('URLs (total)', resultado.total_urls)
    _linha_chave_valor('URLs unicos', resultado.total_urls_unicos)
    _linha_chave_valor('Media hashtags/post', stats['media_hashtags_por_post'])
    _linha_chave_valor('Diversidade vocabulario', f"{stats['diversidade_vocabulario']}%")
    _linha_chave_valor('Hashtag dominante', stats['hashtag_dominante'])


def relatorio_palavras(resultado: AnalisadorResultado, top_n: int = 10):
    _titulo_secao(f'Top {top_n} Palavras')
    _imprimir_ranking(resultado.contador_palavras.most_common(top_n), top_n)


def relatorio_hashtags(resultado: AnalisadorResultado, top_n: int = 5):
    _titulo_secao(f'Top {top_n} Hashtags')
    _imprimir_ranking(resultado.contador_hashtags.most_common(top_n), top_n, '#')


def relatorio_mencoes(resultado: AnalisadorResultado, top_n: int = 5):
    _titulo_secao(f'Top {top_n} Mencoes')
    _imprimir_ranking(resultado.contador_mencoes.most_common(top_n), top_n, '@')


def relatorio_urls(resultado: AnalisadorResultado):
    _titulo_secao('URLs')
    _linha_chave_valor('Total de URLs', resultado.total_urls)
    _linha_chave_valor('URLs unicos', resultado.total_urls_unicos)

    if not resultado.todas_urls:
        print('\nNenhum URL encontrado.')
        return

    print('\nLista de URLs unicos:')
    print(colorir('-' * LARGURA, Cor.CINZA))
    for i, url in enumerate(sorted(resultado.todas_urls), start=1):
        print(f'{i:>2}. {url}')


def relatorio_pesquisa(termo: str, encontrados: list[tuple[int, str]]):
    _titulo_secao(f'Resultados da pesquisa: "{termo}"')

    if not encontrados:
        print('Nenhum post encontrado.')
        return

    _linha_chave_valor('Posts encontrados', len(encontrados))
    print()
    for numero, post in encontrados:
        print(colorir(f'Post #{numero}', Cor.BOLD))
        print(post)
        print(colorir('-' * LARGURA, Cor.CINZA))


def relatorio_completo(resultado: AnalisadorResultado):
    relatorio_resumo(resultado)
    relatorio_palavras(resultado)
    relatorio_hashtags(resultado)
    relatorio_mencoes(resultado)
    relatorio_urls(resultado)
