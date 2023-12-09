class Figure:
    """This class represents a choreographic figure that is used to compose a contra dance.

    Attributes:
        name (str): the user-friendly name of the figure, used to match user input and to print out in the status of the dance
        length (int): the number of beats the figure takes to execute
        pos_shift (int): the change between dancers' start and end positions after executing the figure
        description (str): a short explanation of the figure
        aliases (list): a list of other possible references to this figure, used for matching user input
        dancers (string): the active dancers or subsets performing this figure
        orient: the direction turned or hand used in the figure (left or right)
    """
    def __init__(self, name: str, length: int, pos_shift: int, description: str, aliases: list, dancers: str = "partner", orient: str = None):
        """Constructs a Figure object

        Args:
            name (string): the user-friendly name of the figure
            length (int): the number of beats the figure takes to execute
            pos_shift (int): the change between dancers' start and end positions after executing the figure
            description (string): a short explanation of the figure
            aliases (list): a list of other possible references to this figure, used for matching user input
            dancers (string, optional): the active dancers or subsets performing this figure. Defaults to "partner"
            orient (string, optional): the direction turned or hand used to perform the figure (left or right) Defaults to None.
        """
        self.__name = name
        self.length = length
        self.pos_shift = pos_shift
        self.__description = description
        self.aliases = aliases
        self.dancers = dancers
        self.orient = orient
   

    def __str__(self) -> str:
        """String method for the Figure class

        Returns:
            str: the name of the Figure as a string
        """
        return str(self.__name)


    def get_name(self) -> str:
        """Accesses the name of the figure

        Returns:
            str: the user-friendly name of the figure
        """
        return self.__name
    

    def get_length(self) -> int:
        """Accesses the length of the figure, i.e. the number of beats the figure takes to execute

        Returns:
            int: the number of beats the figure takes to execute
        """
        return self.length
    

    def get_pos_shift(self) -> str|int:
        """Accesses the position shift of the figure, i.e. the change between dancers' start and end positions after executing the figure

        Returns:
            str|int: the change between dancers' start and end positions after executing the figure
        """
        return self.pos_shift
    

    def get_description(self) -> str:
        """Accesses the description of the figure

        Returns:
            str: a short explanation of the figure
        """
        return self.__description
    

    def get_aliases(self) -> list:
        """Accesses other terms to refer to the figure

        Returns:
            list: a list of other possible terms to refer to this figure
        """
        return self.aliases
    

    def get_dancers(self) -> str:
        """Accesses the active dancers performing this figure

        Returns:
            str: the active dancers or subsets performing this figure
        """
        return self.dancers
    
    def get_orient(self) -> str:
        """Accesses the direction or hand used to perform the figure

        Returns:
            str: the direction turned or hand used to perform the figure (left or right)
        """
        return self.orient
    
    # not currently in use, but included for extensibility
    def set_length(self, mod_length: int) -> None:
        """Modifies the length of the figure

        Args:
            mod_length (int): the number of beats the figure takes to execute
        """
        self.length = mod_length

    # not currently in use, but included for extensibility
    def set_pos_shift(self, mod_pos_shift: str|int) -> None:
        """Modifies the expected positional change of the figure

        Args:
            mod_pos_shift (str|int): the change between dancers' start and end positions after executing the figure
        """
        self.pos_shift = mod_pos_shift


    def set_dancers(self, dancers: str) -> None:
        """Sets the active dancers or subsets performing this figure

        Args:
            dancers (str): the active dancers or subsets performing this figure
        """
        self.dancers = dancers


    def set_orient(self, orient: str) -> None:
        """Sets the direction turned or hand used to perform the figure (left or right), used in figure disambiguation

        Args:
            orient (str): the direction turned or hand used to perform the figure (left or right)
        """
        self.orient = orient