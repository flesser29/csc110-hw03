"""
Name: Frances Lesser
Peers: (add any collaborators)
References: (anything you checked to solve this)
"""

# imported modules
import statistics # let's us use mean, median, mode

# This is a global variable (seen by all local scopes)
grades = [0,0,0,0,0] # initialized with five zeros

# Task 1:
#  Complete the function "read_five_ints" below:
def read_five_ints():
    """ updates content of grades depending on the user's input

    Updates the values inside the global variable grades (list)
    with each of the user's 5 input ints.
    If the user inputs are not digits, it prints
    "Error in read_five_ints: input string is not for an integer",
    and if the input converted to int is outside of [0,10], prints
    "Error in read_five_ints: input integer outside of range".
    """
    for idx in range ( len(grades) ):
        # for each idx in 0, 1,... 4 do:
        in_str=input("Give me the next grade in [0 to 10]:")
        # check if the input is not a digit print error
        if in_str.isdigit():
            # convert to int
            num = int(in_str)
        else:
            print ("Error in read_five_ints: input string is not for an integer")
            exit()
        # check if the int is not in the interval [0 to 10] print error
        if num < 0 or num > 10:
            print ("Error in read_five_ints: input integer outside of range")
            sys.exit()
        # add the int to grades at index idx
        grades[idx] = num    
        

    #Anything with this indentation is NO LONGER inside the loop


# Task 2:
#  Complete the function "pick_averaging_method" below:
def pick_averaging_method():
    """ returns an average depending on the user's selection

    Obtains an average using either mean, median or mode,
    depending on user input.
    User should pick 'a' for mean, 'b' for median, 'c' for mode.
    Any other input prints
    'Error in pick_averaging_method: incorrect option picked'.
    """
    # Ask for user to choose, mean, median, or mode
    user = input("Pick 'a' for mean, 'b' for median, 'c' for mode: ")
    # If the user picks mean,  print mean
    if user=="a":
        print("picked: Mean")
        avg = statistics.mean(grades)
        return avg
    # If the user picks median pick, print median
    if user=="b":
        print("picked: Median")
        avg = statistics.median(grades)
        return avg
    # If the user picks mode, print mode
    if user=="c":
        print("picked: Mode")
        avg = statistics.mode(grades)
        return avg
    # Print "error" if the user does not pick mean, median, or mode
    else:
        print("Error in pick_averaging_method: incorrect option picked")
        exit()
    

# Task 3:
#  Complete the function "pick_visualization" below:
def pick_visualization(average):
    """ prints the result in a format that depends on the user's selection

    Prints the numeric average or prints in a special way
    depending on user input.
    User should pick '1' for print average, or '2' for plot average.
    Any other input prints
    'Error in pick_visualization: incorrect option picked'.
    """
    # Ask the user to either print average or plot average
    visualization = input ("Pick '1' for print average, or '2' for plot average: ")
    # If the user chooses to print average, print the list and its 4average
    if visualization == "1":
        print_list_and_average(average)
        return()
    # If the user chooses to plot average, plote the average
    if visualization == "2":
        plot_grades(average)
        return()
    # If the user does not choose to print or plot the average, print error
    else:
        print("Error in pick_visualization: incorrect option picked")
        exit()


# ---------------------------------------
# Do not modify anything below this line
# ---------------------------------------

# Do not modify this function
def print_list_and_average(average):
    print(f"The average of {grades} is {average}")

def plot_grades(average):
    print ("Annotated grades: ")
    prev = -1
    for g in grades:
        if prev < average < g:
            print("^", end="")
        if average > g:
            print(" ", end="")
        if average == g:
            print(f"({g})", end="")
        else:
            print(f"{g} ", end="")
        prev = g
    print()

# Do not modify this function
def main ():
    # calls the function and updates the grades
    read_five_ints()
    # this reorders the values in grades in increasing order
    grades.sort()
    print(f"Sorted grades: {grades}")
    # gets avg depending on selection
    avg = pick_averaging_method()
    # prints or 'plots' result
    pick_visualization(avg)
    print("The End")

# Do not modify these two lines
if __name__ == "__main__":
    main()
    
# - [x] you added your name to the top comments of the python file
# - [x] runs without syntax errors (or -50%)
# - [x] adds a few small but informative comments (or -5%)
# - [x] adds docstrings to each function (or -5%)
# - [x] Passes all tests (or lose 15% per missed test). If you do not pass all tests, do not check this box
# - [x] You checked the correct boxes
