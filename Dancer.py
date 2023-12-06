class Dancer:
    def __init__(self, role: str, couple: int, position: int):
        self.__role = role
        self.__couple = couple
        self.position = position

    def __str__(self) -> str:
        return self.__role + "_" + str(self.__couple)
    

    def get_role(self) -> str:
        return self.__role


    def get_couple(self)-> int:
        return self.__couple
    

    def get_position(self)-> int:
        return self.position


    def set_position(self, position):
        self.position = position