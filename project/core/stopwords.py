"""
core/stopwords.py
─────────────────
Lista de stopwords em português — palavras sem valor analítico
que são excluídas da contagem de frequência de palavras.
"""

STOPWORDS: frozenset = frozenset({
    # Artigos
    'o', 'a', 'os', 'as', 'um', 'uma', 'uns', 'umas',
    # Preposições simples e combinadas
    'de', 'do', 'da', 'dos', 'das', 'em', 'no', 'na', 'nos', 'nas',
    'por', 'para', 'com', 'sem', 'sob', 'sobre', 'entre', 'até',
    'desde', 'ao', 'à', 'aos', 'às', 'pelo', 'pela', 'pelos', 'pelas',
    # Conjunções
    'e', 'ou', 'mas', 'porém', 'porque', 'que', 'se', 'quando', 'como',
    'pois', 'logo', 'assim', 'nem', 'também', 'portanto',
    # Pronomes pessoais e possessivos
    'eu', 'tu', 'ele', 'ela', 'nós', 'vós', 'eles', 'elas',
    'me', 'te', 'se', 'lhe', 'lhes', 'meu', 'minha', 'teu', 'tua',
    'seu', 'sua', 'nosso', 'nossa', 'vosso', 'vossa',
    # Pronomes demonstrativos / indefinidos
    'este', 'esta', 'estes', 'estas', 'esse', 'essa', 'isso', 'aqui',
    'ali', 'lá', 'tudo', 'nada', 'algo', 'alguém', 'ninguém',
    # Advérbios comuns
    'já', 'mais', 'menos', 'muito', 'pouco', 'bem', 'mal', 'não',
    'sim', 'só', 'ainda', 'mesmo', 'cada', 'sempre', 'nunca', 'talvez',
    # Quantificadores
    'todo', 'toda', 'todos', 'todas', 'outro', 'outra', 'outros',
    # Verbos auxiliares e de ligação muito frequentes
    'é', 'são', 'está', 'estão', 'foi', 'eram', 'ser', 'estar',
    'ter', 'há', 'vai', 'vão', 'tem', 'têm', 'pode', 'podem',
    'deve', 'devem', 'fica', 'ficam',
})
