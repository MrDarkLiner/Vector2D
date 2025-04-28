from vector2d import Vector2D

if __name__ == "__main__":
    help(Vector2D)

    vect1 = Vector2D(2,3)
    vect2 = Vector2D(3,5)

    print(f"Vector vect1: {vect1}")
    print(f"Vector vect2: {vect2}")

    print(f"vect1 + vect2: {vect1 + vect2}")
    print(f"vect1 - vect2: {vect1 - vect2}")
    print(f"vect1 * 3: {vect1 * 3}")
    print(f"vect1 == vect2: {vect1 == vect2}")

    print(f"Magnitude of vect1: {vect1.mag()}")
    print(f"Unit vector of vect1: {vect1.unit()}")
    print(f"Dot product of vect1 and vect2: {vect1.dot(vect2)}")
    print(f"Angle between vect1 and vect2: {vect1.angle(vect2)}")