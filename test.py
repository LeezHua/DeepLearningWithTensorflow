# compute loss()
def compute_error_for_line_given_points(b, w, points):
    totalError = 0
    for point in points:
        x = point[0]
        y = point[1]
        totalError += (y - (w * x))

        