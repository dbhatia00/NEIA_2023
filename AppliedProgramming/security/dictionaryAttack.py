# A small program to demonstrate what dictionary-attacking a sha-1 hash could look like

import hashlib

def sha1Hash(inputStr):
    # Computes the sha1 hash of a given input string
    return hashlib.sha1(inputStr.encode('ascii')).hexdigest()

def crack(passFileName, shadowFileName):
    shadowFile = open(shadowFileName, 'r')

    # get each hash in the shadow file
    for hash in shadowFile:
        passFile = open(passFileName, 'r')
        hash = hash.strip()
        found = False
        
        # iterate over every common password in dict, hash it, check against current hash
        for line in passFile:
            if hash == sha1Hash(line.strip()):
                print('HASH ' + hash + ' is ' + line.strip())
                found = True
        
        if found == False:
            print('ERR - ' + hash + ' NOT IN PASSWORD LIST')
        

def main():
    passFile = 'passwordlist.txt'
    shadowFile = 'SHADOW.txt'
    if len(passFile) == 0 or len(shadowFile) == 0 :
        print('Both shadow file and password list are necessary to run program')
    crack(passFile, shadowFile)

if __name__ == "__main__":
    main()