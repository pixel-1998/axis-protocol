import pytest
from axis import Axis, Transform, StopPipeline


class Increment(Transform):
    def __call__(self, state):
        state["count"] = state.get("count", 0) + 1
        return state


class Double(Transform):
    def __call__(self, state):
        state["count"] = state["count"] * 2
        return state


def test_normal_composition():
    axis = Axis().use(Increment()).use(Double())
    assert axis.run({"count": 1}) == {"count": 4}


def test_transform_must_return_state():
    class Buggy(Transform):
        def __call__(self, state):
            state["count"] = 1

    with pytest.raises(TypeError):
        Axis().use(Buggy()).run({"count": 1})


def test_stop_pipeline_short_circuits():
    class CheckFlag(Transform):
        def __call__(self, state):
            if state.get("stop"):
                raise StopPipeline(state)
            return state

    axis = Axis().use(CheckFlag()).use(Double())
    assert axis.run({"count": 5, "stop": True}) == {"count": 5, "stop": True}


def test_stop_pipeline_requires_state():
    class BuggyStop(Transform):
        def __call__(self, state):
            raise StopPipeline("not a dict")

    with pytest.raises(TypeError):
        Axis().use(BuggyStop()).run({"count": 1})


def test_run_requires_initial_state():
    with pytest.raises(TypeError):
        Axis().use(Increment()).run(None)
