class Point:
    """
    Makes class to work with coordinates of the point.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def distance_to_origin(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5


if __name__ == "__main__":
    print("I'm main!")
