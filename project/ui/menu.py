"""Menu interativo com fluxo simples e limpo."""

from pathlib import Path

from core.analyzer import AnalisadorResultado, analisar_ficheiro, pesquisar_posts
from ui import report
from ui.terminal import Cor, colorir, input_opcao, limpar_ecra, pausar


CAMINHO_DADOS = Path(__file__).parent.parent / 'data' / 'posts.txt'



def carregar_dados(caminho: Path = CAMINHO_DADOS) -> AnalisadorResultado | None:
    """Carrega e analisa o ficheiro de dados."""
    limpar_ecra()
    report.mostrar_cabecalho()

    if not caminho.exists():
        print(colorir(f'Ficheiro nao encontrado: {caminho}', Cor.VERMELHO))
        print('Coloque o ficheiro posts.txt em project/data/.')
        pausar()
        return None

    resultado = analisar_ficheiro(caminho)
    print(f'Ficheiro: {caminho}')
    print(colorir(f'Posts analisados: {resultado.total_posts}', Cor.VERDE))
    pausar()
    return resultado



def _mostrar_menu_principal(resultado: AnalisadorResultado):
    limpar_ecra()
    report.mostrar_cabecalho()

    print('Resumo rapido:')
    print(f'- Posts analisados : {resultado.total_posts}')
    print(f'- Hashtags unicas : {resultado.total_hashtags_unicas}')
    print(f'- Mencoes unicas  : {resultado.total_mencoes_unicas}')
    print(colorir('-' * 70, Cor.CINZA))

    print('1 - Resumo geral')
    print('2 - Top 10 palavras')
    print('3 - Top 5 hashtags')
    print('4 - Top 5 mencoes')
    print('5 - Lista de URLs')
    print('6 - Relatorio completo')
    print('7 - Pesquisar posts')
    print('8 - Recarregar ficheiro')
    print('0 - Sair')



def _handle_relatorio(resultado: AnalisadorResultado, funcao_relatorio):
    limpar_ecra()
    report.mostrar_cabecalho()
    funcao_relatorio(resultado)
    pausar()



def _handle_pesquisa(resultado: AnalisadorResultado):
    limpar_ecra()
    report.mostrar_cabecalho()
    print('Pesquisa por palavra, hashtag (#) ou mencao (@).\n')

    try:
        termo = input('Termo de pesquisa: ').strip()
    except (KeyboardInterrupt, EOFError):
        return

    if not termo:
        print('Termo vazio. Pesquisa cancelada.')
        pausar()
        return

    report.relatorio_pesquisa(termo, pesquisar_posts(resultado, termo))
    pausar()


def iniciar():
    """Ponto de entrada do menu interativo."""
    resultado = carregar_dados()
    if resultado is None:
        return

    opcoes_validas = ['0', '1', '2', '3', '4', '5', '6', '7', '8']

    while True:
        _mostrar_menu_principal(resultado)
        opcao = input_opcao('Escolha uma opcao: ', opcoes_validas)

        if opcao == '0':
            limpar_ecra()
            report.mostrar_cabecalho()
            print('Aplicacao encerrada.')
            print()
            break

        if opcao == '1':
            _handle_relatorio(resultado, report.relatorio_resumo)
        elif opcao == '2':
            _handle_relatorio(resultado, report.relatorio_palavras)
        elif opcao == '3':
            _handle_relatorio(resultado, report.relatorio_hashtags)
        elif opcao == '4':
            _handle_relatorio(resultado, report.relatorio_mencoes)
        elif opcao == '5':
            _handle_relatorio(resultado, report.relatorio_urls)
        elif opcao == '6':
            _handle_relatorio(resultado, report.relatorio_completo)
        elif opcao == '7':
            _handle_pesquisa(resultado)
        elif opcao == '8':
            novo_resultado = carregar_dados()
            if novo_resultado is not None:
                resultado = novo_resultado

        
