from sage import node


def test_Root():
    root = node.Root(name="root", score=1.1)
    assert root.name == "root"


def test_Node():
    root = node.Root(name="root", score=1.1)
    test = node.Node(name="test", score=0.9, parent=root, summary="test summary")
    assert test.summary
    assert not test.unimportance  # empty default
    assert isinstance(test, node.Node)
    assert isinstance(test, node.Root)
