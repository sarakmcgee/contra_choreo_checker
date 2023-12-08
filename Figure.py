class Figure:
    def __init__(self, name: str, length: int, pos_shift: int, description: str, aliases: list, dancers: str = "partner", orient: str = None):
        self.__name = name
        self.length = length
        self.pos_shift = pos_shift
        self.__description = description
        self.aliases = aliases
        self.dancers = dancers
        self.orient = orient
   

    def __str__(self) -> str:
        return str(self.__name)


    def get_name(self):
        return self.__name
    

    def get_length(self):
        return self.length
    

    def get_pos_shift(self):
        return self.pos_shift
    

    def get_description(self):
        return self.__description
    

    def get_aliases(self):
        return self.aliases
    

    def get_dancers(self):
        return self.dancers
    
    def get_orient(self):
        return self.orient
    
    
    def set_length(self, mod_length):
        self.length = mod_length


    def set_pos_offset(self, mod_pos_offset):
        self.pos_offset = mod_pos_offset


    def set_dancers(self, dancers):
        self.dancers = dancers


    def set_orient(self, orient):
        self.orient = orient