from dataclasses import dataclass, field
from typing import Self


@dataclass
class Root:
    """Root node; no parent"""

    name: str
    score: float
    summary: str


@dataclass
class Node(Root):
    """Define attributes for each node"""

    parent: Self | Root

    # (note, score) e.g. ("A, B, and C", +2)
    ideal: list[tuple] = field(default_factory=lambda: [])
    importance: list[tuple] = field(default_factory=lambda: [])
    unimportance: list[tuple] = field(default_factory=lambda: [])
    learn_more: list[str] = field(default_factory=lambda: [])
