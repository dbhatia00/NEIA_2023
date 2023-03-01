# A small program to demonstrate what brute forcing a sha-1 hash could look like
import hashlib
from itertools import chain, product
import string

charset = list("abcdefghijklmnopqrstuvwxyz1234567890")

def bruteforce(maxlength):
    # Returns a list of all possible permutations of the charset, limited by the maxlength param
    # Repeats elements from the 'iterable' list a variable number of times
    return (''.join(candidate)
        for candidate in chain.from_iterable(product(charset, repeat=i)
        for i in range(1, maxlength + 1)))

def sha1Hash(inputStr):
    # Computes the sha1 hash of a given input string
    return hashlib.sha1(inputStr.encode('ascii')).hexdigest()

def crack(shadowFileName):
    # get massive list of permutations
    for attempt in bruteforce(4):

        shadowFile = open(shadowFileName, 'r')

        # see if current permutation matches any of our hashes
        for hash in shadowFile:
            if hash.strip() == sha1Hash(attempt):
                print('Hash ' + hash + ' is ' + attempt)
    

def main():
    shadowFile = 'SHADOW.txt'
    if len(shadowFile) == 0:
        print("Error, no file provided")
    else:
        crack(shadowFile)

if __name__ == "__main__":
    main()