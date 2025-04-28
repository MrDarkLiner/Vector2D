# Vector2D Module

A Python module for creating and manipulating 2D vectors. Supports vector addition, subtraction, scalar multiplication, magnitude calculation, unit vector generation, dot product computation and angle calculation.

## Features

- Create 2D vectors with x and y coordinates
- Add and subtract two vectors
- Multiply a vector by a scalar
- Check if two vectors are equal
- Calculate the magnitude (length) of a vector
- Generate the unit (normalized) vector
- Compute the dot product of two vectors
- Calculate angle between two vectors

## Installation

Download the `vector2d.py` file and import it into your project.

```python
from vector2d import Vector2D
```

## Class Documentation

Class and its methods are fully documented with clear Python docstrings, following practices for easy understanding and use.

### Class

`Vector2D(x, y)`

### Parameters

- `x (int | float)`: X-coordinate of the vector
- `y (int | float)`: Y-coordinate of the vector

### Methods
- `get_x() -> float`: Returns the x coordinate.
- `get_y() -> float`: Returns the y coordinate.
- `__add__(other: Vector2D) -> Vector2D`: Adds two vectors.
- `__sub__(other: Vector2D) -> Vector2D`: Subtracts two vectors.
- `__mul__(scalar: int | float) -> Vector2D`: Multiplies a vector by a scalar.
- `__rmul__(scalar: int | float) -> Vector2D`: Provides reversed multiplication.
- `__eq__(other: Vector2D) -> bool`: Checks if two vectors are equal.
- `mag() -> float`: Returns the magnitude of the vector.
- `unit() -> Vector2D`: Returns the unit vector (vector with magnitude 1).
- `dot(other: Vector2D) -> float`: Calculates the dot product of two vectors.
- `angle(other: Vector2D) -> float`: Calculates the angle between two vectors.

## Error Handling

- Raises `TypeError` if incorrect types are passed to methods.
- Raises `ValueError` when trying to calculate unit or angle for a zero-magnitude vector.

## Example

https://github.com/maksymkulbaka/Vector2D/blob/8e8dd430e563f7ee6f81f2c18a76f484a1eb086d/vector2d_example.py#L1-L19
