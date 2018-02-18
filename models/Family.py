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
        U.S. 25 Adds a child to the existing family dictionary if a child with the same name doesn't already
        exist for this family.
        """
        dup_names = []
        dup_birthdays = []
        for child in self.children:
            if child in individuals:
                if individuals[child] in dup_names:
                    print("Duplicate Child's name exists for family: " + individuals[child].name)
                    dup_names.append(individuals[child].name)

                if individuals[child].birthday in dup_birthdays:
                    print("Duplicate Child's birthday exists for family: " + individuals[child].birthday)
                    dup_birthdays.append(individuals[child].birthday)
        return dup_names == [] and dup_birthdays == []
