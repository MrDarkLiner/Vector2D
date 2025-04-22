from math import sqrt

class Vector2D:
    def __init__(self, x: int | float, y: int | float):
        """
        Init method of Vector2D class

        Args:
            x (int | float) : x coordinate of vector
            y (int | float) : y coordinate of vector
        Return:
            None
        """
        if not isinstance(x, (int, float)):
            raise TypeError("Attribute 'x' is not an int or float data type")
        if not isinstance(y, (int, float)):
            raise TypeError("Attribute 'y' is not an int or float data type")
        self._x = float(x)
        self._y = float(y)

    def __str__(self) -> str:
        """
        Return a string values of x, y

        Return:
            str: in format {'x': x, 'y': y}
        """
        return f"{{'x': {self._x}, 'y': {self._y}}}"

    def get_x(self) -> float:
        return self._x
    def get_y(self) -> float:
        return self._y

    def __add__(self, other):
        """
        Addition of two Vector2D objects

        Return:
            Vector2D: x, y
        """
        if not isinstance(other, Vector2D):
            raise TypeError("Addition is possible only for two Vector2D objects")
        return Vector2D(self._x + other.get_x(), self._y + other.get_y())
    def __sub__(self, other):
        """
        Subtraction of two Vector2D objects

        Return:
            Vector2D: x, y
        """
        if not isinstance(other, Vector2D):
            raise TypeError("Subtraction is possible only for two Vector2D objects")
        return Vector2D(self._x - other.get_x(), self._y - other.get_y())
    def __mul__(self, scalar):
        """
        Multiplication of two Vector2D objects

        Return:
            Vector2D: x, y
        """
        if not isinstance(scalar, (int, float)):
            raise TypeError("Multiplication is possible only by a scalar (int or float data type)")
        return Vector2D(self._x * scalar, self._y * scalar)
    def __eq__(self, other) -> bool:
        """
         Equation of two Vector2D objects

         Return:
             Vector2D: x, y
         """
        if not isinstance(other, Vector2D):
            raise TypeError("Equation is possible only for two Vector2D objects")
        return self._x == other.get_x() and self._y == other.get_y()

    def mag(self) -> float:
        """
         Magnitude of Vector2D object

         Return:
             float: magnitude of vector
         """
        return sqrt(self._x ** 2 + self._y ** 2)

    def unit(self):
        """
         Unit of Vector2D object

         Return:
             Vector2D: x, y
         """
        mag = self.mag()
        if mag == 0:
            raise ValueError("Magnitude cannot be zero")
        return Vector2D(self._x / mag, self._y / mag)

    def dot(self, other) -> float:
        """
         Dot product of two Vector2D objects
         Return:
             float: dot products of two vectors
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