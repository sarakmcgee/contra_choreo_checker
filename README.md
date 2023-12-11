# Final Project Report

* Student Name: Sara McGee
* Github Username: sarakmcgee
* Semester: Fall 23
* Course: CS 5001



## Description 
This tool builds a contra dance from a set of choreography figures  via user input and verifies that the length of those figures fits the timing of each phrase and that the final position of each dancer allows both couples to progress through the set and interact with a new pair. 

## Key Features
This program tracks time remaining and dancer position as attributes of the Contra Dance and Dancer classes respectively. Throughout the run of the program, the figure's length and positional shift is verified against these values to ensure the dance is compliant with contra's structural requirements.

## Guide
This program can be run from the command line with no arguments. The default user flow directly initiates dance-building, eliciting user input to select figures, During this process, the user may also list acceptable figures by typing "list" or "list figures", see the dancers' current position by typing "dancers position" or "dancers" or "positions", or remove the most recently added figure by typing "remove" or "delete". Futhermore, the user may leave the program using "exit" or "quit", or consult additional info by typing "help".

Please note, this program must be run with the terminal navigated to the folder which contains the figure descriptions text file, in order to preserve the relative path by which it will be accessed.

## Installation Instructions
No major requirements, just clone the repository. You will need the program itself (contra_choreo_checker.py), the Contra_Dance, Figure, and Dancer class files and the figure_description text file.

## Code Review
This program is controlled from the user input loop in main.
```while True:
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
```

Several of those commands trigger print output to the screen: "help" displays the help text, "see dance" prints the figures added to the dance so far from the stack in the Contra_Dance object,
```elif cmd == 'see dance':
            print()
            curr_dance.dump()
```
"positions" loops through each dancer and prints their current position,
```for dancer in minor_set:
                print(f"{dancer} in position {dancer.get_position()}")
```
 and "list" checks phrase timing and prints the figures that can successfully be added.
```for figure_key in figure_dict:
        figure = figure_dict[figure_key]
        if check_timing(figure):
            print("\t" + figure.get_name())
```
 Beyond that, "remove" and the figure names can modify the dance. When a figure name is input, the program searches for a match in the dictionary of figures, disambiguating as needed, and, if none are found, surfaces the appropriate error message and repeats the loop.
 ```    for figure in figure_dict:
        if cmd == figure_dict[figure].get_name().casefold() or cmd in figure_dict[figure].get_aliases():
            return figure_dict[figure]

        elif cmd == "allemande" or cmd == "star":
            orient = input("By the right or the left?\n").strip().casefold()
            while True:
                if orient == "right" or orient == "left":
                    return figure_dict[cmd + "_" + orient]
                else:
                    orient = input(
                        'Please type either "right" or "left".\n').strip().casefold()

        elif cmd == "hey":
            hey_length = input("Half or Full Hey?\n").strip().casefold()
            while True:
                if hey_length == "full" or "full hey":
                    return figure_dict["full_hey"]
                elif hey_length == "half" or "half hey":
                    return figure_dict["half_hey"]
                else:
                    hey_length == input(
                        'Please type either "half hey" or "full hey".\n').strip().casefold()

    raise ValueError(
        "That figure is not yet available. Please choose from the figures below or type “help” for more options")
 ```
 
 If a figure is successfully identified, then its length is compared to the time remaining in the dance's phrase to ensure the dance can accommodate that figure. If there is not enough time left in the phrase, then the program prompts the user for another choice and preemptively all the figures that are suitable to be selected.
 ```
 if check_timing(figure):
                    set_dancers(figure)
                else:
                    raise ValueError(
                        f'\nInvalid figure: not enough time left!\n{figure.get_name()} requires {figure.get_length()} beats, but there are only {curr_dance.get_time_remaining()} beats left in the phrase.\n\tTo see a list of useable figures, type "list figures"\nThese figures are currently available:')
 ```

 Then, if the timing is acceptable, the user is prompted to set the active dancers that will be executing the figure, which allows the program to evaluate the dancer's final position after the figure is completed.
 ```pos_shift = figure.get_pos_shift()
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
 ```

 Throughout most of the dance, the figure is added, and the dancers' positions and time remaining are updated to reflect that. However, if the dance is almost complete, this final position is compared against the final position necessary to progress, and if congruent, the figure is added and the dance is completed. Otherwise, the figure is rejected and the user is returned to the input loop to choose a different figure that meets requirements.
```if curr_dance.get_phrase_counter() == 4 and curr_dance.get_time_remaining() - figure.get_length() == 0:
                    if check_final_position(figure):
                        add_figure(figure)
                        print("\nDance Complete!\n")
                        curr_dance.dump()
                        print()
                        break
                    else:
                        print("\tInvalid final figure!")
 ```
 
 Since the user may need to make changes earlier in the dance when they find their next selection incompatible, the current dance can be modified by removing the most recently added figure from the top of the stack. Then the user is returned loop to select a new figure, or make further removals.
 ```dance = curr_dance.get_figure_list()
    figure = dance[-1]
    update_position(figure)
    curr_dance.set_time_remaining(
        curr_dance.get_time_remaining() + figure.get_length())
    print(f"\t{figure.get_name()} removed from dance!")
    curr_dance.pop()
 ```

### Major Challenges
Position tracking and management was a significant challenge for this project. In order to update positions throughout the dance, each figure was categorized into a system of position shifts, dependent on which subset(s) of active dancers were executing the move. Positions were evaluated for proposed figures by updating position as if the figure were selected, looping through each dancer's positions attribute to verify against the required final position, and then resetting the attribute to the original value to avoid extraneous modification, in case the figure was not acceptable, or duplicate updates, when positions were updated as part of adding the figure to the dance. Because the update function changes all positions at once, the order of the evaluation loop required some finesse to avoid updating multiple times. However, since this set of figures currently includes only swap transformations, it was conveniently efficient to undo this process with the same function.

## Example Runs
Test_run.txt provides the output of a successful dance composition, demonstrating all major functionality, including input validation, error messaging, and recovery.

## Testing
This project was primarily tested iteratively within the development process. A few test run outputs are included in this repository to demonstrate all major functions.


## Missing Features / What's Next
This project would benefit from expanded validation, including position checking for figure directionality (i.e. chains, heys, etc should only occur across the set, not up or down the hall). These requirements and other similar conventions could be supported by restricting active dancer selection, only surfacing valid active subsets as prompted options and acceptable inputs.

It would also be valuable to support common fractional figure such as allemande 1.5, or circle 3/4. This flexibility would accommodate a wider variety of positional offsets, rather than exact swaps.

Additionally, it would be great to be able to load in an existing set of figures and save off the completed dance in an output file.

## Final Reflection
This course has expanded my base of knowledge, synthesizing previous tech-adjacent experience with foundational concepts to build out more comprehensive competency. The second half of the semester introduced more coordination between components (files, logic, data structures, etc) including defining a recursive relationship within the same function. These next-level considerations allow us to tackle more complex challenges and interact more with the inputs, outputs and errors of the real world.

This project was a fascinating opportunity to see these concepts play out in design decisions. Although I made every mistake in the book at least once, it was exciting to see all the pieces come together and feed information smoothly form one function to another to cover an entire problem space. Of course, the more you consider, the more there is to improve. This attempt was a real lesson in scope and scale, and I'm still trying to figure out how to chunk out effort to incrementally handle increasing complexity.

At this point, I think thorough practice will support my learning and highlight any gaps. I hope to be more proactive next semester, spending less time in "survival mode" and giving myself the time to experiment with each concept. It's gratifying to begin connecting more of the dots and I hope to continue building out that foundation.
