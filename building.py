import classroom

class AcademicBuilding:
    """
    Make a class to work with data about educational buildingю
    """
    def __init__(self, address, classrooms):
        self.address = address
        self.classrooms = classrooms
    

    def total_equipment(self):
        """
        Gives information about all equipment in the building.
        """
        first_lst = []
        sec_lst = []

        for classroom in self.classrooms:
            for thing in classroom.equipment:
                first_lst.append(thing)
        
        for equipment in first_lst:
            element = tuple([equipment, first_lst.count(equipment)])
            sec_lst.append(element)

        return list(set(sec_lst))
    

    def __str__(self):
        result = self.address

        for room in self.classrooms:
            result += '\n' + room.__str__()

        return result


if __name__ == "__main__":
    classroom_016 = classroom.Classroom('016', 80, ['PC', 'projector', 'mic'])
    classroom_007 = classroom.Classroom('007', 12, ['TV'])
    classroom_008 = classroom.Classroom('008', 25, ['PC', 'projector'])
    classrooms = [classroom_016, classroom_007, classroom_008]
    building = AcademicBuilding('Kozelnytska st. 2a', classrooms)
    # print(building.address)
    # for room in building.classrooms:
    #     print(room)
    # print(building.total_equipment())
    # print(building)
