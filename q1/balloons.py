import sys

#Read command line arguments
input_file = sys.argv[1]
with open(input_file) as f:
    #Pattern to be made
    pattern = str(f.readline()).replace('\n', "")

    #Start index
    start = int(f.readline())

    #End index
    end = int(f.readline())

def calculate_balloons(pattern, start, end):

    #Handle the edge cases
    if len(pattern) > 15 or len(pattern) < 4 or end <= start or start < 0 or end > 100000000:
        return 

    #Calculating length of the pattern
    length_of_pattern = len(pattern)

    #Determining the starting character's position in the pattern
    start_char = start % len(pattern)

    #Dictionary to keep track of the number of ballons of each color used
    colors_dict = {
        "b": 0,
        "o": 0,
        "w": 0
    }

    # Traversing from start to end
    for i in range(start, end + 1):

        #Adding the numb to the colors dictionary
        colors_dict[str(pattern[start_char % len(pattern)])] += 1

        #Moving one character ahead in the sequence
        start_char += 1

    # Initializing the final string to return
    final_string = ""

    #Traversing our color dictionary
    for key, value in colors_dict.items():
        final_string += str(key)
        final_string += str(value)
    return final_string

#Return final string
print(calculate_balloons(pattern, start, end))