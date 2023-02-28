# A small program to demonstrate what brute forcing a sha-1 hash could look like
import hashlib
from itertools import chain, product
import string

charset = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

def bruteforce(maxlength):
    # Returns a list of all possible permutations of the charset, limited by the maxlength param
    # Repeats elements from the 'iterable' list a variable number of times
    return (''.join(candidate)
        for candidate in chain.from_iterable(product(charset, repeat=i)
        for i in range(1, maxlength + 1)))

def sha1Hash(inputStr):
    return hashlib.sha1(inputStr.encode('ascii')).hexdigest()

def crack(hash):
    for attempt in bruteforce(5):
        # match it against your password
        if hash == sha1Hash(attempt):
            return attempt
    
    return "ERR - Hash not found, password too long"

def main():
    hashToCrack = "9d601766d652c523a194941d89e419686e987fb6"
    if len(hashToCrack) == 0:
        print("Error, no hash provided")
    else:
        print("The password is - " + crack(hashToCrack))

if __name__ == "__main__":
    main()