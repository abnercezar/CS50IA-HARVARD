import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(link for link in pages[filename] if link in pages)

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Retornar uma distribuição de probabilidade sobre qual página visitar em seguida,
    dada uma página atual.

    Com probabilidade `damping_factor`, escolha um link aleatoriamente
    vinculado por `página`. Com probabilidade `1 - fator de amortecimento`, escolha
    um link escolhido aleatoriamente em todas as páginas do corpus.
    """
    transition_probability = {}
    num_pages = len(corpus)
    num_links = len(corpus[page])

    for p in corpus:
        transition_probability[p] = (1 - damping_factor) / num_pages

    for linked_page in corpus[page]:
        transition_probability[linked_page] += damping_factor / num_links

    return transition_probability


def sample_pagerank(corpus, damping_factor, n):
    """
    Retorne valores de PageRank para cada página amostrando `n` páginas
    de acordo com o modelo de transição, começando com uma página aleatória.

    Retorne um dicionário onde as chaves são nomes de páginas e os valores são
    seu valor estimado de PageRank (um valor entre 0 e 1). Todos
    Os valores do PageRank devem somar 1.
    """
    num_pages = len(corpus)
    ranks = {page: 0 for page in corpus}

    current_page = random.choice(list(corpus.keys()))

    for _ in range(n):
        probabilities = transition_model(corpus, current_page, damping_factor)
        current_page = random.choices(
            list(probabilities.keys()),
            weights=list(probabilities.values()),
            k=1
        )[0]

        ranks[current_page] += 1 / n

    return ranks


def iterate_pagerank(corpus, damping_factor):
    """
    Retorne valores de PageRank para cada página atualizando iterativamente
    Valores do PageRank até a convergência.

    Retorne um dicionário onde as chaves são nomes de páginas e os valores são
    seu valor estimado de PageRank (um valor entre 0 e 1). Todos
    Os valores do PageRank devem somar 1.
    """
    ranks = {page: 1 / len(corpus) for page in corpus}

    while True:
        new_ranks = {}

        for page in corpus:
            rank = (1 - damping_factor) / len(corpus)

            for linked_page in corpus:
                if page in corpus[linked_page]:
                    rank += damping_factor * ranks[linked_page] / len(corpus[linked_page])

            new_ranks[page] = rank

        if all(abs(new_ranks[page] - ranks[page]) < 0.000001 for page in corpus):
            break

        ranks = new_ranks

    return ranks


if __name__ == "__main__":
    main()
