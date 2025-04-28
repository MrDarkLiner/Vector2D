# Vector2D Module

A simple Python module for 2D vector operations such as addition, subtraction, scalar multiplication, magnitude calculation, unit vector finding, and dot product computation.

## Features

- Create 2D vectors with x and y coordinates
- Add and subtract two vectors
- Multiply a vector by a scalar
- Check if two vectors are equal
- Calculate the magnitude (length) of a vector
- Generate the unit (normalized) vector
- Compute the dot product of two vectors

## Installation

No installation needed. Just download the `vector2d.py` file and import it into your project.

```python
from vector2d import Vector2D
```

## Class Documentation

### `Vector2D(x, y)`

#### Parameters

- `x (int | float)`: X-coordinate of the vector
- `y (int | float)`: Y-coordinate of the vector

#### Methods
- `get_x() -> float`: Returns the x coordinate.
- `get_y() -> float`: Returns the y coordinate.
- `__add__(other: Vector2D) -> Vector2D`: Adds two vectors.
- `__sub__(other: Vector2D) -> Vector2D`: Subtracts two vectors.
- `__mul__(scalar: int | float) -> Vector2D`: Multiplies a vector by a scalar.
- `__eq__(other: Vector2D) -> bool`: Checks if two vectors are equal.
- `mag() -> float`: Returns the magnitude of the vector.
- `unit() -> Vector2D`: Returns the unit vector (vector with magnitude 1).
- `dot(other: Vector2D) -> float`: Calculates the dot product of two vectors.

## Error Handling

- Raises TypeError if incorrect types are passed to methods.
- Raises ValueError when trying to create a unit vector for a zero-magnitude vector.

## Usage

```python
# Create vectors
vect1 = Vector2D(2, 3)
vect2 = Vector2D(3, 5)

# Display vectors
print(vect1)  # Output: {'x': 2.0, 'y': 3.0}

# Add vectors
print(vect1 + vect2)  # Output: {'x': 5.0, 'y': 8.0}

# Subtract vectors
print(vect1 - vect2)  # Output: {'x': -1.0, 'y': -2.0}

# Scalar multiplication
print(vect1 * 3)  # Output: {'x': 6.0, 'y': 9.0}

# Check equality
print(vect1 == vect2)  # Output: False

# Vector magnitude
print(vect1.mag())  # Output: 3.605551275463989

# Unit vector
print(vect1.unit())  # Output: {'x': 0.5547..., 'y': 0.8320...}

# Dot product
print(vect1.dot(vect2))  # Output: 21.0
```
