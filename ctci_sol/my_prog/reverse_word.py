
def reverse_word(word):
    if len(word) == 1:
        return word
    else:
        return word[-1] + reverse_word(word[:-1])

if __name__ == "__main__":
    word = "abcde"
    print(reverse_word(word))
     
