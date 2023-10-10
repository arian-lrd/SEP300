class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, vector_other):
        return Vector(self.x + vector_other.x, self.y + vector_other.y)

    def __sub__(self, vector_other):
        return Vector(self.x - vector_other.x, self.y - vector_other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        return Vector(self.x / scalar, self.y / scalar)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
        #returns the printable representation of the specified object as a string


# Example Usage
v1 = Vector(2, 3)
v2 = Vector(1, 1)
print(v1)

# Addition
sum_vector = v1 + v2
print("Sum:", sum_vector)  # Output: Sum: Vector(3, 4)

# Subtraction
diff_vector = v1 - v2
print("Difference:", diff_vector)  # Output: Difference: Vector(1, 2)

# Scalar Multiplication
scaled_vector = v1 * 2
print("Scaled:", scaled_vector)  # Output: Scaled: Vector(4, 6)

# Scalar Division
divided_vector = v1 / 2
print("Divided:", divided_vector)  # Output: Divided: Vector(1.0, 1.5)
