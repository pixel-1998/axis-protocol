# AXIS Protocol

> The Protocol is the Contract. Everything else is implementation.

## The Specification

```
State
   │
   ▼
Transform
   │
   ▼
State
```

Mathematically: **Sₙ₊₁ = T(Sₙ)**

## The Only Laws

1. Every Transform receives a State.
2. Every Transform returns a State.
3. The Kernel never interprets the State.
4. The Kernel never knows the Transform.
5. Any future technology must implement only: State -> State.
6. A Transform may terminate the pipeline early by producing a final State instead of continuing composition. Remaining Transforms do not execute.

## Why This Exists

This is an experiment in finding the smallest possible contract for orchestrating state transformations.

It will not survive because someone believed in it. It will survive because people can implement it, extend it, and use it to solve real problems without changing this minimal contract.

That is what makes a protocol last.

## Use It

```python
from axis import Axis, Transform

class MyTransform(Transform):
    def __call__(self, state):
        state["result"] = "done"
        return state

axis = Axis()
axis.use(MyTransform())
final_state = axis.run({"start": True})
```

**For the formal specification, see [SPEC.md](SPEC.md).**

No license. No restrictions. No permission needed.
