"""
main.py
───────
Ponto de entrada da aplicação Analisador de Redes Sociais.

Execução:
    python main.py

Estrutura do projecto:
    social_analyzer/
    ├── main.py              ← ESTE FICHEIRO
    ├── core/
    │   ├── stopwords.py     Stopwords em português
    │   ├── reader.py        Gerador de leitura do ficheiro
    │   ├── extractor.py     Extracção com regex (hashtags, menções, URLs)
    │   └── analyzer.py      Motor de análise e contagem
    ├── ui/
    │   ├── terminal.py      Utilitários de terminal (cores, limpeza)
    │   ├── report.py        Renderização de relatórios
    │   └── menu.py          Menu interactivo
    └── data/
        └── posts.txt        Ficheiro de posts simulados
"""

import sys
from pathlib import Path

# Garante que o directório raiz do projecto está no PYTHONPATH,
# permitindo imports como 'from core.analyzer import ...'
sys.path.insert(0, str(Path(__file__).parent))

from ui.menu import iniciar


if __name__ == '__main__':
    try:
        iniciar()
    except KeyboardInterrupt:
        print('\n\n  Aplicação interrompida. Até logo!\n')
        sys.exit(0)
