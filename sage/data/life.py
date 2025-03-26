from sage.node import Node, Root

life = Root(name="Life", score=1, summary="Life")
health = Node(name="Health", score=1, parent=life, summary="Physical well-being")
finances = Node(name="Finances", score=1, parent=life, summary="Money")
social = Node(name="Social", score=1, parent=life, summary="")
career = Node(name="Career", score=1, parent=life, summary="")
personal_development = Node(name="Personal Development", score=1, parent=life, summary="")
diet = Node(name="Diet", score=1, parent=health, summary="")
fitness = Node(name="Fitness", score=1, parent=health, summary="")
mental_health = Node(name="Mental Health", score=1, parent=health, summary="")
tobacoo_use = Node(name="Tobacoo Use", score=1, parent=health, summary="")
alcohol_use = Node(name="Alcohol Use", score=1, parent=health, summary="")
skin_care = Node(name="Skin Care", score=1, parent=health, summary="")
