class Contra_Dance:
    def __init__(self, initial_list: list = [], phrase_counter: int = 1, time_remaining: int = 32):
        self.figure_list = initial_list.copy()
        self.phrase_counter = phrase_counter
        self.time_remaining = time_remaining


    def __str__(self) -> str:
        return str(self.figure_list)
    

    def get_figure_list(self):
        return self.figure_list
    

    def get_phrase_counter(self):
        return self.phrase_counter

    
    def get_time_remaining(self):
        return self.time_remaining
    
    def set_time_remaining(self, time_remaining):
        self.time_remaining = time_remaining


    def increment_phrase_counter(self):
        self.phrase_counter += 1

   
    def push(self, item):
        self.figure_list.append(item)


    def pop(self):
        self.figure_list.pop()


    def dump(self):
        for i in range(1, len(self.figure_list) -1):
            print(str(self.figure_list[i]))