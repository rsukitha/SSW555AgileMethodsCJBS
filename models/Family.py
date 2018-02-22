"""
Class to represent a Family based on GEDCOM data sets.
"""


class Family:
    __slots__ = "id", "married", "divorced", "husband_id", "husband_name", "wife_id", "wife_name", "children"

    def __init__(self, unique_id):
        self.id = unique_id
        self.children = {}
        self.husband_name = "NA"
        self.wife_name = "NA"
        self.divorced = "NA"

    def validate_children(self, individuals):
        """
        U.S. 25 Validates whether a Child with the same name and birthday exists in the family.
        """
        child_name_bday_dict = {}
        duplicates = []
        for child_id in self.children:
            if child_id in individuals:
                child = individuals[child_id]
                if child.name in child_name_bday_dict and child_name_bday_dict[child.name] == child.birthday:
                    duplicates.append(child)
                    print("ERROR: FAMILY: US25: {}: Child with name: {} and birthday {} already exists".format(
                        self.id, child.name, child.birthday))
                child_name_bday_dict[child.name] = child.birthday
        return duplicates == []
