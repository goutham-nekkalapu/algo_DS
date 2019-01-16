
# to store the generated words 
output = []

"""
fun to find all permutations of words of length 'k', given a list of string of length'n' 

input_list      = input string of whose characters will be used to create new strings 
output_word     = an intermediate string, which in process of making 
input_length    = length of the input 
k               = length of output string desired 
"""
def print_all_permutations(input_list, output_word, input_length, k):
    # base case 
    if k == 0 :
        #print(output_word)
        global output
        output.append(output_word)
        return
    
    # adding all the char in 'input_list' and calling recursively 'k' times
    for i in range(input_length):
        new_word = output_word + input_list[i]  # adding next character of input 
        print_all_permutations(input_list, new_word, input_length, k-1) # k is decreased as we have added a new character 


def print_all_possible_words(input_list, output_words_length):
    n = len(input_list)
    print_all_permutations(input_list, "", n, output_words_length)


if __name__ == "__main__":
   
    print ("enter the string whose characters you want to use to generate new words")
    input_list = input()
    # extracting only the unique characters  
    l1 = set(input_list)
    input_list = list(l1) 
    
    print ("enter the length of the words, you wish to generate")
    output_word_length = int(input())
    print_all_possible_words(input_list, output_word_length)
    print ("the generated words are : ")
    print(output)

