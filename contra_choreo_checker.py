"""This program builds a contra dance from a set of choreography figures and verifies that timing and final dancer position for the figures in this dance uphold the structure of a contra.
"""

from Contra_Dance import Contra_Dance
from Dancer import Dancer
from Figure import Figure

figure_descriptions = {}
figure_dict = {}

partner_aliases = ["partner", "partners", "p"]
neighbor_aliases = ["neighbor", "neighbors", "neighbour", "neighbours", "n"]
lark_aliases = ["lark", "larks", "l", "gents", "men"]
raven_aliases = ["raven", "ravens", "r", "ladies", "women"]

raven_1 = Dancer('raven', 1, 1)
lark_1 = Dancer('lark', 1, 2)
raven_2 = Dancer('raven', 2, 3)
lark_2 = Dancer('lark', 2, 4)

minor_set = (raven_1, lark_1, raven_2, lark_2)
req_final_pos = {raven_1: 4, lark_1: 3, raven_2: 2, lark_2: 1}

curr_dance = Contra_Dance()

help_text = '\nThis contra choreography aid checks the timing of figures to ensure the dance can be neatly divided into four phrases containing 32 beats each.\n\n\tTo see a list of available figures to select, type "list" or "list figures"\n\n\tTo see the figures in the dance so far, type "see dance"\n\n\tTo see the dancers\' current position, type "dancers position" or "dancers" or "positions"\n\n\tTo remove the most recent figure added to the dance, type "remove" or "delete"\n\n\tTo leave the program, type "exit" or "quit"'

def access_figure_descriptions(file_path: str) -> None:
    """Reads in the text file where the description of each figure is stored and adds them to the figure_descriptions dictionary global variable

    Args:
        file_path (str): path of the figure descriptions text file to be read in
    """
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
    """Builds a global variable dictionary of Figure objects for each of the figures that can be added to the dance
    """
    access_figure_descriptions("figure_descriptions.txt")
    figure_dict['allemande_left'] = Figure("Allemande Left", 8, 0, figure_descriptions["allemande"], [], "partners", "left")
    figure_dict['allemande_right'] = Figure("Allemande Right", 8, 0, figure_descriptions["allemande"], [], "partners", "right")
    figure_dict['balance'] = Figure("Balance", 4, 0, figure_descriptions["balance"], [], "partners")
    figure_dict['box_the_gnat'] = Figure("Box the Gnat", 4, "swap", figure_descriptions["box_the_gnat"], ["box gnat"], "partners")
    figure_dict['cali_twirl'] = Figure("California Twirl", 4, "swap", figure_descriptions["cali_twirl"], ["cali twirl", "ca twirl"], "partners")
    figure_dict['circle_left'] = Figure("Circle Left", 4, 0, figure_descriptions["circle"], ["circle"], "all", "left")
    figure_dict['do_si_do'] = Figure("Do-si-do", 8, 0, figure_descriptions["do_si_do"], ["do si do", "dosido"], "partners")
    figure_dict['eye_turn'] = Figure("Eye Turn", 8, 0, figure_descriptions["eye_turn"], ["gypsy", "right shoulder round"], "partners")
    figure_dict['half_hey'] = Figure("Half Hey", 8, "c_swap", figure_descriptions["half_hey"], ["hey across"], "all")
    figure_dict['full_hey'] = Figure("Hey for Four/Full Hey", 16, 0, figure_descriptions["full_hey"], ["hey for four", "full hey"], "all")
    figure_dict['chain'] = Figure("Raven's Chain", 8, "swap", figure_descriptions["chain"], ["chain", "ladies chain", "ladies' chain", "ravens chain"], "ravens")
    figure_dict['long_lines'] = Figure("Long Lines, Forward and Back", 8, 0, figure_descriptions["long_lines"], ["long lines"], "all")
    figure_dict['mad_robin'] = Figure("Mad Robin", 8, 0, figure_descriptions["mad_robin"], ["sashay round"], "all")
    figure_dict['pass_through'] = Figure("Pass Through", 8, "swap", figure_descriptions["pass_through"], [], "partners")
    figure_dict['petronella'] = Figure("Petronella", 8, "c_swap", figure_descriptions["petronella"], [], "all")
    # note petronella results in a swapped position between couples although progression occurs counterclockwise around the edge of the set
    figure_dict['promenade'] = Figure("Promenade", 8, "c_swap", figure_descriptions["promenade"], [], "all")
    figure_dict['pull_by'] = Figure("Pull By", 4, "swap", figure_descriptions["pull_by"], [], "partners")
    figure_dict['right_left_through'] = Figure("Right and Left Through", 8, "c_swap", figure_descriptions["right_left_through"], ["right and left", "right left through", "right left"], "all")
    figure_dict['star_left'] = Figure("Left Hand Star", 8, 0, figure_descriptions["star"], ["star by the left", "star left"], "all", "left")
    figure_dict['star_right'] = Figure("Right Hand Star", 8, 0, figure_descriptions["star"], ["star by the right", "star right"], "all", "right")
    figure_dict['swing'] = Figure("Swing", 8, 0, figure_descriptions["swing"], [], "partners")


def list_available_figures() -> None:
    """Prints a list of all figures valid to be added to the dance, checking timing remaining in the phrase.
    """
    print('Available Figures:')
    for figure_key in figure_dict:
        figure = figure_dict[figure_key]
        if check_timing(figure):
            print("\t" + figure.get_name())

def check_timing(figure: Figure) -> bool:
    """Checks if there is enough time left in the current phrase to accommodate a given figure

    Args:
        figure (Figure): The selected figure to be checked

    Returns:
        bool: The truth value of whether or not the length of the given figure can fit within the time remaining in the current phrase 
    """
    return (curr_dance.get_time_remaining() - figure.get_length()) >= 0


def update_time_remaining(figure: Figure) -> None:
    """Subtracts the length of a figure from the existing time remaining in the dance

    Args:
        figure (Figure): Figure to be added to the dance
    """
    time_remaining = curr_dance.get_time_remaining()
    curr_dance.set_time_remaining(time_remaining - figure.get_length())
 

def check_phrase() -> None:
    """Transitions between phrases by checking for the end of the current phrase, printing the dance so far, incrementing the phrase counter, and resetting the beats available in the new phrase
    """
    if curr_dance.get_time_remaining() == 0 and curr_dance.get_phrase_counter() < 2:
        print(f'\nPhrase {curr_dance.get_phrase_counter()} complete!')
        print("\nYour dance so far:")
        curr_dance.dump() 
        curr_dance.increment_phrase_counter()
        curr_dance.set_time_remaining(32)
        print(f'\nNow on to Phrase {curr_dance.get_phrase_counter()}!')


def swap_position(dancer_a: Dancer, dancer_b: Dancer) -> None:
    """Swaps the position attribute of two dancers"

    Args:
        dancer_a (Dancer): One of two dancers swapping positions, order is arbitrary
        dancer_b (Dancer): The other of two dancers swapping positions, order is arbitrary
    """
    temp_a = dancer_a.get_position()
    temp_b = dancer_b.get_position()
    dancer_a.set_position(temp_b)
    dancer_b.set_position(temp_a)


def update_position(figure: Figure) -> None:
    """Updates the position of each active dancer engaged in a figure to their final position at the end of that figure.

    Args:
        figure (Figure): The figure to be executed
    """
    pos_shift = figure.get_pos_shift()
    if pos_shift == 0:
        return

    elif pos_shift == "swap":
        dancers = figure.get_dancers()
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

# swaps the positions of an entire couple with the other, by swapping each role individually
    elif pos_shift == "c_swap":
        swap_position(lark_1, lark_2)
        swap_position(raven_1, raven_2)

# increments position clockwise around the set, for non-swapping figures (like circle 3/4) that aren't evenly divisible into swaps (unlike petronella, which results in a swapped position between couples although progression occurs counterclockwise around the edge of the set)
# not currently utilized by the existing figure set, but included for extensibility
    elif type(pos_shift) == int:
        for dancer in minor_set:
            temp = dancer.get_position()
            temp = (temp + pos_shift) % 4
            if temp == 0:
                temp = 1
            dancer.set_position(temp)


def check_final_position(figure: Figure) -> bool:
    """Checks each dancer's final position after executing a given figure against the final position needed to progress to the next minor set

    Args:
        figure (Figure): The figure being compared

    Returns:
        bool: The truth value of whether or not the dancers will be in the appropriate position after executing that figure
    """
    test_counter = 0
    for dancer in minor_set:
        hold = dancer.get_position()
        update_position(figure)
        if dancer.get_position() != req_final_pos[dancer]:
             test_counter += 1
             print(f"{dancer} in position {dancer.get_position()}, not position {req_final_pos[dancer]} to progress")
        dancer.set_position(hold)
    return test_counter == 0


def get_figure(cmd) -> Figure:
    """Retrieves Figure object based on selected figure input, disambiguates common input

    Args:
        cmd (_type_): Typed input from the user selecting a figure to be added to the dance

    Raises:
        ValueError: Occurs when input received does not match any figures in the dictionary

    Returns:
        Figure: The Figure object, making it's associated attributes available to subsequent functions for verification
    """
    for figure in figure_dict:
        if cmd == figure_dict[figure].get_name().casefold() or cmd in figure_dict[figure].get_aliases():
            return figure_dict[figure]
        
        elif cmd == "allemande" or cmd == "star":
            orient = input("By the right or the left?\n").strip().casefold()
            while True:
                if orient == "right" or orient == "left":
                    return figure_dict[cmd + "_" + orient]
                else:
                    orient = input('Please type either "right" or "left".\n').strip().casefold()
            
        elif cmd == "hey":
            hey_length = input("Half or Full Hey?\n").strip().casefold()
            while True:
                if hey_length == "full" or "full hey":
                    return figure_dict["full_hey"]
                elif hey_length == "half" or "half hey":
                    return figure_dict["half_hey"]
                else:
                    hey_length == input('Please type either "half hey" or "full hey".\n').strip().casefold()
    
    raise ValueError("That figure is not yet available. Please choose from the figures below or type “help” for more options")


def normalize_dancer_input(input: str) -> str:
    """Reassigns a few likely input variations for active dancers to a recognizable common value" 

    Args:
        input (str): typed user input to specify which dancers are executing a figure

    Returns:
        str: A string which can be recognized by the program to represent any of these diverse inputs
    """
    if input in partner_aliases:
        input = "partners"
    elif input in neighbor_aliases:
        input = "neighbors"
    elif input in lark_aliases:
        input = "larks"
    elif input in raven_aliases:
        input = "ravens"
    return input
            

def set_dancers(figure: Figure):
    """Elicits from the user the active dancers that will engage in the chosen figure and sets the dancer attribute on the Figure object.

    Args:
        figure (Figure): The selected Figure to be updated
    """
    if figure.get_dancers() != "all":
        if figure.get_name != "Raven's Chain":
            actives = input("Who's dancing together in this figure? partners, neighbors, ravens or larks?\n").strip().casefold()
            if actives in partner_aliases or actives in neighbor_aliases or actives in lark_aliases or actives in raven_aliases:
                actives = normalize_dancer_input(actives)
                figure.set_dancers(actives)
            else:
                print("Please choose from the options listed.")
                set_dancers(figure)


def add_figure(figure: Figure):
    """Adds the selected figure to the dance Stack, and appropriately updates dancer position, beats left in the phrase, and transitions between phrases when relevant

    Args:
        figure (Figure): The Figure to be added to the dance
    """
    curr_dance.push(figure)
    update_time_remaining(figure)
    update_position(figure)
    print(f"\t{figure.get_name()} added to dance!")
    check_phrase()


def remove_figure():
    """Removes the most recently added Figure from the dance Stack, resets dancers to their previous positions, adds back the appropriate length of time to the beats available in the phrase, and prints the updated dance and time remaining.
    """
    dance = curr_dance.get_figure_list()
    figure = dance[-1]
    update_position(figure)
    curr_dance.set_time_remaining(curr_dance.get_time_remaining() + figure.get_length())
    print(f"\t{figure.get_name()} removed from dance!")
    curr_dance.pop()
    print("\nThis dance now contains:")
    curr_dance.dump()
    print(f'\n{str(curr_dance.get_time_remaining())} beats available in the phrase\n')


def main():
    """Main driver of the program, accepts input commands from the user, coordinates dance building, other selections within the main loop.

    Raises:
        ValueError: Occurs when there is insufficient time left in the dance phrase to accommodate the selected figure.
    """
    print("\n\tWelcome to the Contra Choreo Checker!\n\nLet's make a dance! Select a figure and type it below.")
    build_figure_dict()
    while True:
        cmd = input().strip().casefold()
        if cmd == "help":
            print(help_text)
        elif cmd == "exit" or cmd == "quit":
            break
        elif cmd == 'see dance':
            print()
            curr_dance.dump()
            print("\nSelect your next figure:")
        elif cmd == "list figures" or cmd == "list":
            list_available_figures()
        elif cmd == "dancers positions" or cmd == "dancers" or cmd == "dancer positions" or cmd == "dancer" or cmd == "positions":
            print()
            for dancer in minor_set:
                print(f"{dancer} in position {dancer.get_position()}")
        elif cmd == "remove" or cmd == "delete":
            remove_figure()
        else:
            try:
                figure = get_figure(cmd)
                
                if check_timing(figure):
                    set_dancers(figure)
                else:
                    raise ValueError(f'\nInvalid figure: not enough time left!\n{figure.get_name()} requires {figure.get_length()} beats, but there are only {curr_dance.get_time_remaining()} beats left in the phrase.\n\tTo see a list of useable figures, type "list figures"\nThese figures are currently available:')
                
                if curr_dance.get_phrase_counter() == 2 and curr_dance.get_time_remaining() - figure.get_length() == 0:
                    if check_final_position(figure):
                        add_figure(figure)
                        print("\nDance Complete!\n")
                        curr_dance.dump()
                        print()
                        break      
                    else:
                        print("\tInvalid final figure!")
                else:
                    add_figure(figure)
                
                print(f'\n{str(curr_dance.get_time_remaining())} beats available in the phrase\n')
                    
                if len(curr_dance.get_figure_list()) == 1:
                    print('To view the figures in your dance, type "see dance".\nOtherwise, select your next figure below.')
                else:
                    print("\nSelect your next figure:")
            
            except ValueError as error:
                print(error)
                list_available_figures()

if __name__ == "__main__":
    main()
