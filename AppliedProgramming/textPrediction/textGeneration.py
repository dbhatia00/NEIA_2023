#
# ps8pr2.py  (Problem Set 8, Problem 2)
#
# Monte carlo text generation   
#
# devb@bu.edu

import random

def create_dictionary(filename):
    '''
     takes a string representing the name of a 
     text file, and that returns a dictionary of key-value pairs
    '''
    file = open(filename)
    text = file.read()      # read it all in at once!
    file.close()
    words = text.split()
    d = {}
    d['$'] = [words[0]]
    for i in range(len(words) - 1):
        if (words[i][-1] in '!.?') and ('$' not in d):
            d['$'] = [words[i+1]]
        elif (words[i][-1] in '!.?'):
            d['$'] += [words[i+1]]
        else:
            if words[i] not in d:
                d[words[i]] = [words[i+1]]
            else:
                d[words[i]] += [words[i+1]]
    return d


def generate_text(word_dict, num_words):
    '''
    takes as parameters a dictionary of word transitions 
    (generated by the create_dictionary function) named word_dict 
    and a positive integer named num_words. Uses word_dict to generate 
    and print num_words words, with a space after each word
    '''
    current = '$'
    for i in range(num_words):
        wordlist = word_dict[current]
        next_word = random.choice(wordlist)
        print(next_word, end=' ')
        if next_word[-1] in '.!?':
            current = '$'
        else:
            current = next_word
    print()

def main():
    filename = 'test.txt'
    wordlist = create_dictionary(filename)
    generate_text(wordlist, 10)

if __name__ == "__main__":
    main()