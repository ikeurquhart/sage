from sage.node import Root, Node

parent_nodes = {
    "life": "top-level",
    "health": "life",
    "finances": "life",
    "social": "life",
    "career": "life",
    "personal development": "life",
    "diet": "health",
    "fitness": "health",
    "mental health": "health",
}

life = Root(score=1)
health = Node(score=1, parent=life, summary="Physical well-being")
finances = Node(score=1, parent=life, summary="Money")
