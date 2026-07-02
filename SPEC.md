# AXIS Specification (Language Agnostic)

## Core Axiom
A computation is defined as a mapping from a state to another state.

## Notation
`S' = T(S)`

Where:
- `S` is any representation of state.
- `T` is any operation that maps `S` to `S'`.

## Composition
Multiple transformations compose: `S_n = T_n(...T_1(S_0))`
