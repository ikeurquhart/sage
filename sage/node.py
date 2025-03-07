from dataclasses import dataclass, field
from typing import Self


@dataclass
class Root:
    """Define attributes for each node"""

    score: float


@dataclass
class Node(Root):
    """Define attributes for each node"""

    parent: Self | Root
    summary: str
    importance: list[tuple] = field(
        default_factory=lambda: []
    )  # (note, score) e.g. ("A, B, and C", +2)
    unimportance: list[tuple] = field(default_factory=lambda: [])
    learn_more: list[str] = field(default_factory=lambda: [])
