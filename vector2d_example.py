from vector2d import Vector2D

help(Vector2D) # Displays documentation about the module

vect1 = Vector2D(2,3)
vect2 = Vector2D(3,5)

print(f"Vector vect1: {vect1}") # Output: {'x': 2.0, 'y': 3.0}
print(f"Vector vect2: {vect2}") # Output: {'x': 3.0, 'y': 5.0}

print(f"vect1 + vect2: {vect1 + vect2}") # Output: {'x': 5.0, 'y': 8.0}
print(f"vect1 - vect2: {vect1 - vect2}") # Output: {'x': -1.0, 'y': -2.0}
print(f"vect1 * 3: {vect1 * 3}") # Output: {'x': 6.0, 'y': 9.0}
print(f"vect1 == vect2: {vect1 == vect2}") # Output: False

print(f"Magnitude of vect1: {vect1.mag()}") # Output: 3.605551275463989
print(f"Unit vector of vect1: {vect1.unit()}") # Output: {'x': 0.5547001962252291, 'y': 0.8320502943378437}
print(f"Dot product of vect1 and vect2: {vect1.dot(vect2)}") # Output: 21.0
print(f"Angle between vect1 and vect2: {vect1.angle(vect2)}") # Output: 0.04758310327698479