"""Utilitarios de terminal usados pela aplicacao."""

import os
import platform
import sys


def _suporta_ansi() -> bool:
    """Deteta suporte basico a ANSI."""
    if os.environ.get('NO_COLOR') or os.environ.get('TERM') == 'dumb':
        return False
    if platform.system() == 'Windows':
        return bool(
            os.environ.get('WT_SESSION')
            or os.environ.get('ANSICON')
            or os.environ.get('TERM_PROGRAM')
        )
    return hasattr(sys.stdout, 'isatty') and sys.stdout.isatty()


ANSI = _suporta_ansi()


class Cor:
    """Constantes de cor ANSI (vazias sem suporte)."""

    if ANSI:
        RESET = '\033[0m'
        BOLD = '\033[1m'
        DIM = '\033[2m'

        CINZA = '\033[90m'
        VERMELHO = '\033[91m'
        VERDE = '\033[92m'
        AMARELO = '\033[93m'
        CIANO = '\033[96m'
    else:
        RESET = ''
        BOLD = ''
        DIM = ''
        CINZA = ''
        VERMELHO = ''
        VERDE = ''
        AMARELO = ''
        CIANO = ''


def limpar_ecra():
    """Limpa o ecra com fallback para ambientes limitados."""
    # 1) Tenta ANSI (funciona na maioria dos terminais modernos).
    if hasattr(sys.stdout, 'write'):
        try:
            sys.stdout.write('\033[2J\033[H')
            sys.stdout.flush()
        except OSError:
            pass

    # 2) Tenta comando nativo do sistema.
    comando = 'cls' if platform.system() == 'Windows' else 'clear'
    codigo = os.system(comando)

    # 3) Fallback final para consoles que nao interpretam ANSI/clear.
    if codigo != 0 or not (hasattr(sys.stdout, 'isatty') and sys.stdout.isatty()):
        print('\n' * 120, end='')


def colorir(texto: str, *estilos: str) -> str:
    """Aplica estilos ao texto quando ANSI esta disponivel."""
    if not ANSI:
        return texto
    return ''.join(estilos) + texto + Cor.RESET


def input_opcao(prompt: str, opcoes_validas: list[str]) -> str:
    """Le e valida uma opcao do utilizador."""
    while True:
        try:
            opcao = input(prompt).strip().lower()
        except (KeyboardInterrupt, EOFError):
            print()
            return '0'

        if opcao in opcoes_validas:
            return opcao

        print(colorir(
            f'Opcao invalida. Escolha entre: {", ".join(opcoes_validas)}',
            Cor.AMARELO,
        ))


def pausar(mensagem: str = 'Prima ENTER para continuar...'):
    """Pausa ate o utilizador carregar ENTER."""
    try:
        input(colorir(f'\n{mensagem}', Cor.DIM))
    except (KeyboardInterrupt, EOFError):
        pass
