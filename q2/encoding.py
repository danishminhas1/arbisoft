import sys

#Read command line arguments
input_file = sys.argv[1]
with open(input_file) as f:
    chars = str(f.readline()).replace("\n", "")
    mode = int(f.readline())
    s = str(f.readline()).replace("\n", "")
chars = list(eval(chars))

#Construct dictionary mapping letters to codes
def make_word_to_code_dict(chars):
    char_dict = {}
    i = 1
    for item in chars:
        pos = 1
        for char in item:
            char_dict[char] = str(i) * pos
            pos += 1
        i+=1
    return char_dict

#Construct dictionary mapping codes to letters
def make_code_to_word_dict(chars):
    code_dict = {}
    i = 1
    for item in chars:
        pos = 1
        for char in item:
            code_dict[str(i) * pos] = char
            code_dict["0" + (str(i) * pos)] = char.upper()
            pos += 1
        i += 1
    return code_dict 

#Use char_dict dictionary to convert word to code
def word_to_code(chars, s, char_dict):
    final_string = ""
    for element in s:
        if element.lower() not in char_dict.keys():
            #return error if not present in dictionary
            return 'Error'
        if 65 <= ord(element) <= 90:
            #append 0 for an uppercase letter
            final_string += "0"
        final_string += char_dict[element.lower()]
        #add separator
        final_string += "0"
    return final_string

#Use code_dict dictionary to convert code to word
def code_to_word(chars, s, code_dict):
    code_list = s.split("0")
    for i in range(len(code_list)-1):
        if code_list[i] == '':
            code_list[i+1] = "0" + code_list[i+1]
    final_list = list()
    for i in code_list:
        if i:
            final_list.append(i)
    #initialize final string to return
    final_string = ""
    for element in final_list:
        if element not in code_dict.keys():
            #return error if not present in dictionary
            return 'Error'
        final_string += code_dict[element]
    return final_string

#Make the two dictionaries for faster access
char_dict = make_word_to_code_dict(chars)
code_dict = make_code_to_word_dict(chars)

#Check for the mode and call appropriate method
if mode == 1:
    print(word_to_code(chars, s, char_dict))
elif mode == 2:
    print(code_to_word(chars, s, code_dict))
