import networkx as nx
import plotly.graph_objects as go
import plotly.offline as py

from sage import network

# node_list = ["a", "b", "c", "d", "e"]
# nodes = {"a": ["b", "c", "d"], "b": ["e"]}


nodes, edges = network.get_life_nodes_and_edges()

added = set()

network = nx.Graph()

for node in nodes:
    network.add_node(node.name, summary=node.summary)

for node, parent in edges:
    network.add_edge(node.name, parent.name)


def make_edge(x, y):
    return go.Scatter(x=x, y=y, line=dict(width=1, color="cornflowerblue"), hoverinfo="skip")


pos_ = nx.spring_layout(network)

edge_trace = []
for edge in network.edges():
    char_1 = edge[0]
    char_2 = edge[1]

    x0, y0 = pos_[char_1]
    x1, y1 = pos_[char_2]

    # text = char_1 + "--" + char_2 + ": " + str(network.edges()[edge]["weight"])

    trace = make_edge([x0, x1, None], [y0, y1, None])
    edge_trace.append(trace)


node_trace = go.Scatter(
    x=[],
    y=[],
    text=[],
    textposition="top center",
    textfont_size=20,
    mode="markers+text",
    hoverinfo="text",
    marker=dict(color=[], size=[], line=None, opacity=[]),
    hovertemplate=[],
)
# For each node in midsummer, get the position and size and add to the node_trace
for node in network.nodes():
    if node == "Life":
        print(node, network.nodes[node]["summary"])
    x, y = pos_[node]
    node_trace["x"] += tuple([x])
    node_trace["y"] += tuple([y])
    node_trace["marker"]["color"] += tuple(["cornflowerblue"])
    node_trace["marker"]["size"] += tuple([10])
    node_trace["marker"]["opacity"] += tuple([1])
    node_trace["text"] += tuple(["<b>" + node + "</b>"])
    node_trace["hovertemplate"] += tuple([network.nodes[node]["summary"]])


layout = go.Layout(
    paper_bgcolor="rgba(0,0,0,0)",  # transparent background
    plot_bgcolor="rgba(0,0,0,0)",  # transparent 2nd background
    xaxis={"showgrid": False, "zeroline": False},  # no gridlines
    yaxis={"showgrid": False, "zeroline": False},  # no gridlines
)

# Create figure
fig = go.Figure(layout=layout)
# Add all edge traces
for trace in edge_trace:
    fig.add_trace(trace)
# Add node trace
fig.add_trace(node_trace)
# Remove legend
fig.update_layout(showlegend=False)
# Remove tick labels
fig.update_xaxes(showticklabels=False)
fig.update_yaxes(showticklabels=False)
# Show figure
fig.show()
