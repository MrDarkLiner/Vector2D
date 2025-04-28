"""This module provides a `Vector2D` class for creating and working with 2D vectors.

Features:
- Basic arithmetic operations: addition, subtraction
- Scalar multiplication
- Magnitude (length) calculation
- Unit vector generation
- Dot product calculation

The class includes error handling for invalid operations and type checking.
"""

from math import sqrt

class Vector2D:
    """Vector2D class for creating and working with 2D vectors.

    Class supports basic arithmetic operations,
    scalar multiplication and calculating vector length
    """
    def __init__(self, x: int | float, y: int | float):
        """Init method of Vector2D class.

        Args:
            x (int | float): X coordinate of vector.
            y (int | float): Y coordinate of vector.

        Raises:
            TypeError: Occurs if the arguments types are incorrect.
        """
        if not isinstance(x, (int, float)):
            raise TypeError("Argument 'x' is not an int or float data type")
        if not isinstance(y, (int, float)):
            raise TypeError("Argument 'y' is not an int or float data type")
        self._x = float(x)
        self._y = float(y)

    def __str__(self) -> str:
        """Returns a string of attributes of a Vector2D object

        Returns:
            str: In format "{'x': x, 'y': y}".
        """
        return f"{{'x': {self._x}, 'y': {self._y}}}"

    def get_x(self) -> float:
        return self._x
    def get_y(self) -> float:
        return self._y

    def __add__(self, other):
        """Adds coordinates of two Vector2D objects.

        Args:
            other (Vector2D): other Vector2D object.

        Returns:
            Vector2D(x, y): new Vector2D object.

        Raises:
            TypeError: Occurs if the argument is not a Vector2D object.
        """
        if not isinstance(other, Vector2D):
            raise TypeError("Addition is possible only for two Vector2D objects")
        return Vector2D(self._x + other.get_x(), self._y + other.get_y())
    def __sub__(self, other):
        """Subtracts coordinates of two Vector2D objects.

        Args:
            other (Vector2D): other Vector2D object.

        Returns:
            Vector2D(x, y): new Vector2D object.

        Raises:
            TypeError: Occurs if the argument is not a Vector2D object.
        """
        if not isinstance(other, Vector2D):
            raise TypeError("Subtraction is possible only for two Vector2D objects")
        return Vector2D(self._x - other.get_x(), self._y - other.get_y())
    def __mul__(self, scalar):
        """Multiplies coordinates of a Vector2D object by a scalar.

        Args:
            scalar (int | float): scalar by which the vector will be multiplied.

        Returns:
            Vector2D(x, y): new Vector2D object.

        Raises:
            TypeError: Occurs if the argument is not an int or float data type.
        """
        if not isinstance(scalar, (int, float)):
            raise TypeError("Multiplication is possible only by a scalar (int or float data type)")
        return Vector2D(self._x * scalar, self._y * scalar)
    def __eq__(self, other) -> bool:
        """Equalizes coordinates of two Vector2D objects.

        Args:
            other (Vector2D): other Vector2D object.

        Returns:
            bool: True if the coordinates are equal, False otherwise.

        Raises:
            TypeError: Occurs if the argument is not a Vector2D object.
        """
        if not isinstance(other, Vector2D):
            raise TypeError("Equation is possible only for two Vector2D objects")
        return self._x == other.get_x() and self._y == other.get_y()

    def mag(self) -> float:
        """Calculates the magnitude of a Vector2D object.

        Returns:
            float: Magnitude of vector.
        """
        return sqrt(self._x ** 2 + self._y ** 2)

    def unit(self):
        """Calculates the unit vector of a Vector2D object.

        Returns:
            Vector2D(x, y): new Vector2D object.

        Raises:
            ValueError: Occurs if coordinates of the Vector2D object are zero.
        """
        mag = self.mag()
        if mag == 0:
            raise ValueError("Zero vector cannot have a unit vector")
        return Vector2D(self._x / mag, self._y / mag)

    def dot(self, other) -> float:
        """Calculates the dot product of two Vector2D objects.

        Args:
            other (Vector2D): other Vector2D object.

        Returns:
            float: Dot products of two vectors.

        Raises:
            TypeError: Occurs if the argument is not a Vector2D object.
        """
        if not isinstance(other, Vector2D):
            raise TypeError("Dot product is possible only for two Vector2D objects")
        return self._x * other.get_x() + self._y * other.get_y()


if __name__ == "__main__":
    vect1 = Vector2D(2, 3)
    print(vect1)

    vect2 = Vector2D(3, 5)
    print(vect1 + vect2)
    print(vect1 - vect2)
    print(vect1 * 3)
    print(vect1 == vect2)

    print(vect1.mag())
    print(vect1.unit())
    print(vect1.dot(vect2))