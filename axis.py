# The Protocol is the Contract.
# Everything else is implementation.
# No permission needed. Use as you wish.

from abc import ABC, abstractmethod
from typing import Any, Dict

State = Dict[str, Any]


class Transform(ABC):
    @abstractmethod
    def __call__(self, state: State) -> State:
        ...


class Axis:
    def __init__(self):
        self.transforms = []

    def use(self, transform: Transform):
        self.transforms.append(transform)
        return self

    def run(self, state: State) -> State:
        for transform in self.transforms:
            state = transform(state)
        return state
