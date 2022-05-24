import numpy as np

def distance(x1, y1, x2, y2):
    """Returns the Euclidean distance between two points."""

    return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def triangle_area(x1, y1, x2, y2, x3, y3):
    """Calculates the area of a triangle with vertices (x1, y1), (x2, y2) and
    (x3, y3).
    """

    # Calculate the distances of each side
    a = distance(x1, y1, x2, y2)
    b = distance(x2, y2, x3, y3)
    c = distance(x3, y3, x1, y1)
    s = (a + b + c) / 2

    return np.sqrt(s * (s-a) * (s-b) * (s-c))


def insideTriangle(xp, yp, xA, yA, xB, yB, xC, yC):
    """Returns true if the input point (xp, yp) is inside the triangle of
    vertices A(x, y), B(x, y) and C(x, y), or false otherwise.
    """

    # Calculate area of the entire triangle
    total_area = round(triangle_area(xA, yA, xB, yB, xC, yC), 5)

    # Calculate the inner areas
    area_1 = round(triangle_area(xA, yA, xB, yB, xp, yp), 5)
    area_2 = round(triangle_area(xB, yB, xC, yC, xp, yp), 5)
    area_3 = round(triangle_area(xA, yA, xC, yC, xp, yp), 5)

    # Verify if point is inside the triangle
    if total_area == area_1 + area_2 + area_3:
        return True
    else:
        return False
