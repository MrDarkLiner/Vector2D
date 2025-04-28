from vector2d import Vector2D

if __name__ == "__main__":
    help(Vector2D)

    v1 = Vector2D(2,5)
    v2 = Vector2D(4,5)

    print("Vector v1:", v1)
    print("Vector v2:", v2)

    v3 = v1 + v2
    print("v1 + v2 =", v3)

    v4 = v1 - v2
    print("v1 - v2 =", v4)

    v5 = v1 * 3
    print("v1 * 3 =", v5)

    are_equal = v1 == v2
    print("v1 == v2:", are_equal)

    mag_v1 = v1.mag()
    print("Magnitude of v1:", mag_v1)

    unit_v1 = v1.unit()
    print("Unit vector of v1:", unit_v1)

    dot_product = v1.dot(v2)
    print("Dot product of v1 and v2:", dot_product)
