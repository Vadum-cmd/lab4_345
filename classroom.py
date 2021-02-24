class Classroom:
    '''
    Makes a class for work with data about classrooms.
    '''
    def __init__(self, number, capacity, equipment):
        self.number = number
        self.capacity = capacity
        self.equipment = equipment


    def __str__(self):
        return """Classroom {0} has a capacity of {1} persons and has the following \
equipment: {2}.""".format(self.number, self.capacity, ", ".join(self.equipment))


    def is_larger(self, room):
        pass


classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
classroom_007 = Classroom('007', 12, ['TV'])
classroom_016.is_larger(classroom_007)