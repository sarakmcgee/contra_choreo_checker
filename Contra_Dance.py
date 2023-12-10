class Contra_Dance:
    """A Stack which lists the figures of one contra dance, and tracks the phrases and beats available in the phrase while the dance is being built.

    Attributes:
        figure_list (list): The list of figures within the dance.
        phrase_counter (int): counter to keep track of how many phrases have been composed
        time_remaining (int): number of beats left in the current phrase
    """
    def __init__(self, initial_list: list = [], phrase_counter: int = 1, time_remaining: int = 32):
        """Constructs a Contra_Dance object

        Args:
            initial_list (list, optional): The list of figures within the dance, may be loaded in on construction. Defaults to [].
            phrase_counter (int, optional): counter to keep track of how many phrases have been composed. Defaults to 1.
            time_remaining (int, optional): number of beats left in the current phrase. Defaults to 32.
        """
        self.figure_list = initial_list.copy()
        self.phrase_counter = phrase_counter
        self.time_remaining = time_remaining


    def __str__(self) -> str:
        """String method for Contra_Dance class

        Returns:
            str: The figure list of the dance as a string
        """
        return str(self.figure_list)
    

    def get_figure_list(self) -> list:
        """Accesses figure list within Contra_Dance object

        Returns:
            list: List of figures within the dance
        """
        return self.figure_list
    

    def get_phrase_counter(self) -> int:
        """Accesses phrase counter within Contra_Dance object

        Returns:
            int: counter to keep track of how many phrases have been composed
        """
        return self.phrase_counter

    
    def get_time_remaining(self) -> int:
        """Accesses time remaining (i.e. the number of beats left in the current phrase) within Contra_Dance object

        Returns:
            int: number of beats left in the current phrase
        """
        return self.time_remaining
    
    def set_time_remaining(self, time_remaining: int) -> None:
        """Sets time_remaining attribute to a new value

        Args:
            time_remaining (int): number of beats left in the current phrase
        """
        self.time_remaining = time_remaining


    def increment_phrase_counter(self) -> None:
        """Increments the phrase counter by 1 when the end of the phrase is reached
        """
        self.phrase_counter += 1

   
    def push(self, figure) -> None:
        """Adds new figure to the top of the figure_list Stack

        Args:
            figure (Figure): figure to be added to the dance
        """
        self.figure_list.append(figure)


    def pop(self) -> None:
        """Removes figure from the top of the figure_list Stack
        """
        self.figure_list.pop()


    def dump(self):
        """Prints all figures in the figure list from first to most recently added
        """
        for figure in self.figure_list:
            print(str(figure))