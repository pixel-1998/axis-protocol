# The Protocol is the Contract.
# Everything else is implementation.
# See LICENSE.

from abc import ABC, abstractmethod
from typing import Any, Dict

State = Dict[str, Any]


class StopPipeline(Exception):
    """Raise this inside a Transform to halt the pipeline early."""
    def __init__(self, state: State):
        if not isinstance(state, dict):
            raise TypeError(
                f"StopPipeline requires a State (dict), got "
                f"{type(state).__name__}."
            )
        self.state = state


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
        if not isinstance(state, dict):
            raise TypeError(
                f"Axis.run() requires an initial State (dict), got "
                f"{type(state).__name__}."
            )

        try:
            for transform in self.transforms:
                result = transform(state)
                if not isinstance(result, dict):
                    raise TypeError(
                        f"{transform.__class__.__name__} returned "
                        f"{type(result).__name__}, not a State (dict). "
                        f"Every Transform must return a State."
                    )
                state = result
        except StopPipeline as stop:
            return stop.state
        return state
