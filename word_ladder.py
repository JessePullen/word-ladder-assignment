import re
import os

def same(item, target):
    # finds any words that have matching letters in the same position with the target word and
    # returns the word and number of matches
    return len([c for (c, t) in zip(item, target) if c == t])

def build(pattern, words, seen, list):
    # iterates through the word list and searches for the pattern using a wildcard "." and checks the word has
    # not already been seen.
    return [word for word in words if re.search(pattern, word) and word not in seen.keys() and word not in list]

def find(word, words, seen, target, path, shortFlag):
    # finds the path from the start word to the target word.
    letterList = []
    list = []
    if same(word, target) >= 1:
        # every time this function runs this takes words that have zero matching letters at all out of the list
        for i, b in enumerate(zip(word, target)):
            # enumerate runs a loop with an iterable and compares the zip of the current iterations starting word and
            # the target word for matching letters
            if all(a[0] == b[0] for a in b):
                letterList.append(i)
                # appends to the letterList if the compared indexes have matching letters for the next set of loops
    for i in range(len(word)):
        # gets run on each letter of the starting word for each iteration of this function.
        if i not in letterList:
            # ensures that each positions index is only checked if it has not yet been found.
            list += build(word[:i] + "." + word[i + 1:], words, seen, list)
            # builds a list of variations of the starting word e.g lead becomes .ead, l.ad, le.d, lea.d.
    if len(list) == 0:
        return False
        # returns false if there is no possible path to the target word
    list = sorted([(same(w, target), w) for w in list], reverse=shortFlag)
    # uses the same function to augment the list into having a value for how many matching letters a word in the list
    # has against the target word
    for (match, item) in list:
        # this loop adds a word to the path for any word that has all but one letter different from the last word
        if match == len(target) - 1:
            # checks if this iterations word length is one less than the target word
            path.append(item)
            return True
        seen[item] = True
        # updates the seen dictionary for the currently seen word with a True flag.
    for (match, item) in list:
        # resets the list from being tuples to a list of strings so that it can then be sent back through the find
        # function for the next iteration with a new starting word
        path.append(item)
        # appends the path with a newly found match
        if find(item, words, seen, target, path, shortFlag):
            return True
            # recursively calls itself to run iteratively till the target word is reached.
        path.pop()

def notAllowed(words):
    # this function takes a list of words that are not allowed and removes then from the main word list that
    # was initially entered.
    while True:
        # takes in the values from the file of not allowed words.
        remFile = input("\nEnter the text filename including the file extention\n"
                        "containing the list of words that are not allowed: ")
        if os.path.isfile(remFile) and '.txt' in remFile:
            # checks if the file exists and is a .txt file before continuing.
            fileIn = open(remFile)
            # opens the dictionary file
            exLines = fileIn.readlines()
            # reads lines from the file
            fileIn.close()
            # closes the dictionary file
            break
        else:
            print("\nThat file either does not exist or is not a .txt file. Please try again.")
    exList = []
    for exLine in exLines:
        exWord = exLine.strip().lower()
        exList.append(exWord)
        # creates a list of not allowed words from the file input, strips whitespace and converts to lowercase.
    for remWord in exList:
        if remWord in words:
            words.remove(remWord)
            # if there is a match this loop removes the not allowed words from the list of dictionary words.
    return words

def shortestPath(shortFlag):
    # this function flips a boolean flag on or off depending on if the user wants to get the shortest path from the
    # start word to the target word
    if shortFlag == 'y' or shortFlag == 'yes':
        return True
    elif shortFlag == 'n' or shortFlag == 'no':
        return False
    else:
        print("Answer unclear. Please try again\n")
        shortFlag = None

#start of main program
while True:
    # takes in the values from the dictionary file of words.
    fname = input("Enter dictionary filename (file must be a .txt file): ").lower().strip()
    if os.path.isfile(fname) and '.txt' in fname:
        # checks if the file exists and is a .txt file before continuing.
        file = open(fname)
        # opens the dictionary file
        lines = file.readlines()
        # reads lines from the file
        file.close()
        # closes the dictionary file
        break
    else:
        print("That file does not exist or is not a .txt file. Please try again.")
while True:
    start = input("Enter start word:").lower().strip()
    # takes user input for start word, strips whitespace and converts to lowercase.
    words = []
    for line in lines:
        # creates the initial dictionary list of words from the file input, strips whitespace and converts to lowercase.
        word = line.rstrip().lower()
        if len(word) == len(start):
            words.append(word)
            # checks words in dictionary for length and if they are the same length as the start word they are added to the
            # word list to check against later in the program.
    target = input("Enter target word:").lower().strip()
    # takes user input for target word, strips whitespace and converts to lowercase.
    break
exclusion = None
while exclusion == None:
    exclusion = input("Would you like to provide a list of words that are not allowed Y/N: ").lower().strip()
    # takes user input to see if they want to add a list of words that are not allowed, strips whitespace
    # and converts to lowercase.
    if exclusion == 'y' or exclusion == 'yes':
        words = notAllowed(words)
    elif exclusion == 'n' or exclusion == 'no':
        break
    else:
        exclusion = None
        print("Answer unclear. Please try again\n")
        # loop continues until a valid input is provided by the user.
shortFlag = None
while shortFlag == None:
    shortFlag = input("Would you like the shortest path? Y/N: ").lower().strip()
    # takes user input to see if they want to proceed with the shortest path, strips whitespace
    #  and converts to lowercase.
    shortFlag = shortestPath(shortFlag)
path = [start]
seen = {start: True}
if find(start, words, seen, target, path, shortFlag):
    # sends the starting word, list of stripped words of the same length as the start word, a dictionary of words seen
    # so far, target word and the path list that initially just contains the start word. if the find function returns
    # a true condition it prints what it has found.
    path.append(target)
    print(len(path) - 1, path)
else:
    print("No path found")
    # prints if no path is possible from starting word to target word.