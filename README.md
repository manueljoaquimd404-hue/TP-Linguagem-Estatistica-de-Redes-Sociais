Trabalho Prático 1.1: Análise de Dados de Redes Sociais (Frequência e
Padrões)
Tema: Desenvolvimento de um script Python para analisar um conjunto de dados simulado de
posts de redes sociais, identificando palavras-chave, hashtags e menções mais frequentes, e
padrões de uso.
Objetivo: Criar um programa que processe um ficheiro de texto (simulando posts de redes
sociais), extraia informações relevantes usando manipulação de strings e expressões regulares,
e apresente estatísticas básicas sobre o conteúdo.

Metodologia:
    •Geração de Dados (Opcional, para teste): Crie um ficheiro de texto (posts.txt) com
    cerca de 50-100 linhas, onde cada linha simula um post. Inclua palavras-chave, algumas
    hashtags (#tema), menções (@usuario) e URLs (https://...).
    •Leitura e Pré-processamento: Implemente uma função geradora para ler o ficheiro
    posts.txt linha por linha, convertendo o texto para minúsculas e removendo pontuação
    básica.
    •Extração de Entidades:
    ◦Use expressões regulares para extrair todas as hashtags (#palavra), menções
    (@usuario) e URLs (http(s)://...) de cada post.
    ◦Armazene essas entidades em estruturas de dados apropriadas (e.g., listas ou
    sets).
    Análise de Frequência:
    ◦Conte a frequência de cada palavra (excluindo stopwords comuns como 'e', 'o',
    'a', 'de', etc. - pode criar uma lista simples de stopwords).
    ◦Conte a frequência de cada hashtag e menção.
    ◦Utilize collections.Counter ou compreensões de dicionário para esta tarefa.
    Relatório: Apresente:
    ◦As 10 palavras mais frequentes.
    ◦As 5 hashtags mais populares.
    ◦As 5 menções mais frequentes.
    ◦O número total de URLs encontradas.  
    
Critério de Avaliação:
    •Uso de Geradores (15%): Implementação eficiente da leitura de ficheiros linha por
    linha.
    •Manipulação de Strings e Regex (30%): Correta aplicação de expressões regulares
    para extração de hashtags, menções e URLs. Pré-processamento adequado do texto.
    •Estruturas de Dados (25%): Uso apropriado de listas, sets e dicionários para
    armazenar e contar as entidades.
    •Análise de Frequência (20%): Cálculo correto das frequências e apresentação dos
    resultados.
    •Organização e Legibilidade do Código (10%): Código bem comentado,
    modularizado e fácil de entender.