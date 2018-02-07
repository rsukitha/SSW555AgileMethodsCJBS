class Family:
    __slots__ = "id", "married", "divorced", "husband_id", "husband_name", "wife_id", "wife_name", "children"

    def __init__(self, unique_id):
        self.id = unique_id
        self.children = {}
        self.husband_name = "NA"
        self.wife_name = "NA"
        self.divorced = "NA"
