# See: https://medium.com/towards-data-science/tutorial-network-visualization-basics-with-networkx-and-plotly-and-a-little-nlp-57c9bbb55bb9

from data import life

from sage.node import Node, Root


def get_life_nodes_and_edges():
    vars = [getattr(life, advice) for advice in dir(life)]
    nodes = [advice for advice in vars if isinstance(advice, Root)]

    edges = [(advice, advice.parent) for advice in vars if isinstance(advice, Node)]

    return nodes, edges


if __name__ == "__main__":
    print(get_life_nodes_and_edges())
