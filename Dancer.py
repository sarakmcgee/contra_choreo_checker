class Dancer:
    """This class represents a single dancer within figures, tracking their position throughout the dance
    
    Attributes:
        role (str): The role this dancer will be executing. Note that this program uses the gender-neutral role monikers "lark" and "raven", in which the lark stands on the the left of the couple and the raven stand on the right. See aliases in the global variables of contra_choreo_checker.py for other gendered mappings to these roles.
        couple (int): The number of the couple pair to which this dancer belongs, within the minor set. As in English Country Dancing, ones are closest to the stage and progress down the hall, while twos face the stage and progress up toward the band.
        position (int): The dancer's position within the minor set, numbered clockwise from the upper left corner.
    """
    def __init__(self, role: str, couple: int, position: int):
        """Constructs a Dancer object

        Args:
            role (str): The role this dancer will be executing, raven or lark
            couple (int): The number of the couple pair to which this dancer belongs, within the minor set
            position (int): The dancer's position within the minor set, numbered clockwise from the upper left corner.
        """
        self.__role = role
        self.__couple = couple
        self.position = position

    def __str__(self) -> str:
        """String method for Dancer class

        Returns:
            str: concatenation of role and couple number
        """
        return self.__role + "_" + str(self.__couple)
    

    def get_role(self) -> str:
        """Accesses role on the Dancer object

        Returns:
            str: The role this dancer will be executing, raven or lark
        """
        return self.__role


    def get_couple(self) -> int:
        """Accesses couple number on the Dancer object 

        Returns:
            int: The number of the couple pair to which this dancer belongs, within the minor set
        """
        return self.__couple
    

    def get_position(self) -> int:
        """Accesses the current position of this dancer

        Returns:
            int: position number within the minor set, numbered clockwise from the upper left corner.
        """
        return self.position


    def set_position(self, position: int) -> None:
        """Sets the dancer's position to a new value, updated from the figures executed

        Args:
            position (int): position number within the minor set, numbered clockwise from the upper left corner.
        """
        self.position = position