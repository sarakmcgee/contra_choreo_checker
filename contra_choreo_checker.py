from Figure import Figure
from Dancer import Dancer
from Contra_Dance import Contra_Dance

figure_descriptions = {}
figure_dict = {}

raven_1 = Dancer('raven', 1, 1)
lark_1 = Dancer('lark', 1, 2)
raven_2 = Dancer('raven', 2, 3)
lark_2 = Dancer('lark', 2, 4)

minor_set = (raven_1, lark_1, raven_2, lark_2)
req_final_pos = {raven_1: 4, lark_1: 3, raven_2: 1, lark_2: 2}

curr_dance = Contra_Dance()

help_text = "!!!!!!!!!"

def access_figure_descriptions(file_path: str) -> None:
    try:
        in_file = open(file_path, "r", encoding="utf-8")
        txt = in_file.read()
        lines = txt.split("\n")
        for line in lines:
            if line != "":
                entry = line.split(':')
                key = entry[0].strip()
                value = entry[1].strip()
                figure_descriptions[key] = value


    except FileNotFoundError:
        print(f"{file_path} not found!")
    except IOError as io:
        print(io)


def build_figure_dict() -> None:
    access_figure_descriptions("figure_descriptions.txt")
    figure_dict['allemande_left'] = Figure("Allemande Left", 8, 0, figure_descriptions["allemande"], "partners", "left")
    figure_dict['allemande_right'] = Figure("Allemande Right", 8, 0, figure_descriptions["allemande"], "partners", "right")
    figure_dict['balance'] = Figure("Balance", 4, 0, figure_descriptions["balance"], "partners")
    figure_dict['box_the_gnat'] = Figure("Box the Gnat", 4, "swap", figure_descriptions["box_the_gnat"], "partners")
    figure_dict['cali_twirl'] = Figure("California Twirl", 4, "swap", figure_descriptions["cali_twirl"], "partners")
    figure_dict['circle_left'] = Figure("Circle Left", 4, 0, figure_descriptions["circle"], orient = "left")
    figure_dict['do_si_so'] = Figure("Do-si-do", 8, 0, figure_descriptions["do_si_do"], "partners")
    figure_dict['eye_turn'] = Figure("Eye Turn", 8, 0, figure_descriptions["eye_turn"], "partners")
    figure_dict['half_hey'] = Figure("Half Hey", 8, "c_swap", figure_descriptions["half_hey"])
    figure_dict['full_hey'] = Figure("Hey for Four/Full Hey", 16, 0, figure_descriptions["full_hey"])
    figure_dict['chain'] = Figure("Raven's Chain", 8, "swap", figure_descriptions["chain"], "ravens")
    figure_dict['long_lines'] = Figure("Long Lines, Forward and Back", 8, 0, figure_descriptions["long_lines"])
    figure_dict['mad_robin'] = Figure("Mad Robin", 8, 0, figure_descriptions["mad_robin"])
    figure_dict['pass_through'] = Figure("Pass Through", 8, "swap", figure_descriptions["pass_through"], "partners")
    figure_dict['petronella'] = Figure("Petronella", 8, -2, figure_descriptions["petronella"])
    figure_dict['promenade'] = Figure("Promenade", 8, "c_swap", figure_descriptions["promenade"])
    figure_dict['pull_by'] = Figure("Pull By", 4, "swap", figure_descriptions["pull_by"], "partners")
    figure_dict['right_left_through'] = Figure("Right and Left Through", 8, "c_swap", figure_descriptions["right_left_through"])
    figure_dict['star_left'] = Figure("Left Hand Star", 8, 0, figure_descriptions["star"], orient = "left")
    figure_dict['star_right'] = Figure("Right Hand Star", 8, 0, figure_descriptions["star"], orient = "right")
    figure_dict['swing'] = Figure("Swing", 8, 0, figure_descriptions["swing"], "partners")


def list_available_figures():
    print('Available Figures:')
    for figure_key in figure_dict:
            figure = figure_dict[figure_key]
            if check_timing(figure):
                print("\t" + figure.get_name())

def check_timing(figure: Figure) -> bool:
    """This function checks if there is enough time left in the current phrase to accommodate a given figure

    Args:
        figure (Figure): The selected figure to be checked

    Returns:
        bool: The truth value of whether or not the length of the given figure can fit within the time remaining in the current phrase 
    """
    time_remaining = (curr_dance.get_time_remaining())
    if time_remaining - figure.get_length() >= 0:
        return True
    else:
        return False


def update_time_remaining(figure: Figure) -> None:
    time_remaining = (curr_dance.get_time_remaining())
    new_time_remaining = time_remaining - figure.get_length()
    curr_dance.set_time_remaining(new_time_remaining)


def check_phrase():
    if curr_dance.get_time_remaining() == 0:
        if curr_dance.get_phrase_counter() < 4:
            print(f'\nPhrase {curr_dance.get_phrase_counter()} complete!')
            print("\nYour dance so far:")
            curr_dance.dump() 
            curr_dance.increment_phrase_counter()
            curr_dance.set_time_remaining(32)
            print(f'\nNow on to Phrase {curr_dance.get_phrase_counter()}!')
        else:
            print("\nDance Complete!\n")
            curr_dance.dump()


def check_final_position(figure: Figure, dancer) -> int:
    hold = dancer.get_position()
    update_position(figure)
    if dancer.get_position != req_final_pos[dancer]:
        print(f"{dancer.get_name()} in position {dancer.get_position()}, not position {req_final_pos[dancer]} to progress")
        dancer.set_position(hold)
        return 1


def swap_position(dancer_a: Dancer, dancer_b: Dancer) -> None:
    temp_a = dancer_a.get_position()
    temp_b = dancer_b.get_position()
    dancer_a.set_position(temp_b)
    dancer_b.set_position(temp_a)    


def update_position(figure: Figure) -> None:
    pos_shift = figure.get_pos_shift()
    if pos_shift == 0:
        return
    dancers = figure.get_dancers()
    if pos_shift == "swap":
        if dancers == "partners":
            swap_position(lark_1, raven_1)
            swap_position(lark_2, raven_2)
        elif dancers == "neighbors":
            swap_position(lark_1, raven_2)
            swap_position(lark_2, raven_1)
        elif dancers == "larks":
            swap_position(lark_1, lark_2)
        elif dancers == "ravens":
            swap_position(raven_1, raven_2)

    elif pos_shift == "c_swap":
        swap_position(lark_1, lark_2)
        swap_position(raven_1, raven_2)
    
    elif type(pos_shift) == int:
        for dancer in minor_set:
            temp = dancer.get_position()
            temp = (temp + pos_shift) % 4
            if temp == 0:
                temp = 4
            dancer.set_position(temp)


def get_figure(cmd) -> Figure:
    for figure in figure_dict:
            name = figure_dict[figure].get_name()
            if cmd.strip().casefold() == name.casefold():
                return figure_dict[figure]
            

def set_dancers(figure: Figure):
    if figure.get_dancers() != None:
        if figure.get_name != "Raven's Chain":
            dancers = input("Who's dancing in this figure? partners, neighbors, ravens or larks?").strip().casefold()
            if dancers == "partners" or dancers == "neighbors" or dancers == "larks" or dancers == "ravens":
                figure.set_dancers(dancers)
            else:
                print("Please choose from the options listed.")
                set_dancers(figure)

def check_position(figure: Figure):
    if curr_dance.get_phrase_counter() == 1 and curr_dance.get_time_remaining() - figure.get_length() == 0:
        test_counter = 0
        for dancer in minor_set:
            test_counter += check_final_position(figure, dancer)
        if test_counter == 0:
            return True
        else:
            print("Invalid final figure!")
            return False
    else:    
        return True
    

def add_figure(figure):
    curr_dance.push(figure)
    update_time_remaining(figure)
    print(f"\t{figure.get_name()} added to dance!")
    check_phrase()
    print(f'\n{str(curr_dance.get_time_remaining())} beats still available in the phrase\n')


#def delete_figure():
    

def main():
    print("\n\tWelcome to the Contra Choreo Checker!\n\nLet's make a dance! Select a figure and type it below.")
    build_figure_dict()
    while True:
        cmd = input()
        if cmd.strip().casefold() == "help":
            print(help_text)
        elif cmd.strip().casefold() == "exit" or cmd == "quit":
            break
        elif cmd.strip().casefold() == 'see dance':
            print()
            curr_dance.dump()
        elif cmd.strip().casefold() == "list figures" or cmd.strip().casefold() == "list":
            list_available_figures()
        else:
            try:
                figure = get_figure(cmd)
                if figure == None:
                    raise ValueError("That figure is not yet available. Please choose from the figures below or type “help” for more options")
                if check_timing(figure):
                    set_dancers(figure)
                else:
                    raise ValueError(f'Invalid figure: not enough time left!\n{figure.get_name()} requires {figure.get_length()} beats, but there are only {curr_dance.get_time_remaining()} beats left in the phrase.\nTo see a list of useable figures, type "list figures"\nThese figures are currently available:')
                if check_position(figure):
                    add_figure(figure)
                    
                if len(curr_dance.get_figure_list()) == 1:
                    print('To view the figures in your dance, type "see dance".\nOtherwise, select your next figure below.')
                else:
                    print("\nSelect your next figure:")
            
            except ValueError as error:
                print(error)
                list_available_figures()


main()
