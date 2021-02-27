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


    def is_larger(self, oth_room):
        """
        Gives an answer about which room can accommodate more people.
        """
        return self.capacity > oth_room.capacity
    

    def equipment_differences(self, oth_room):
        """
        Compares equipment amoung rooms.
        """
        unique_equipment = []
        for thing in self.equipment:
            if thing not in oth_room.equipment:
                unique_equipment.append(thing)
        return unique_equipment
    

    def __repr__(self):
        return f'Classroom({self.number}, {self.capacity}, {self.equipment})'


if __name__ == "__main__":
    classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
    classroom_007 = Classroom('007', 12, ['TV'])
    # print(classroom_016)
    # print(classroom_016.is_larger(classroom_007))
    # print(classroom_016.equipment_differences(classroom_007))
    # print(classroom_016.__repr__())
