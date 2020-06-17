'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
     # base case if the lenght of the word is less than 2 
    if len(word) < 2:
        # return 0 
        return 0
    # check if the word after taken away the first two characters'th'
    if word[:2] == "th":
        # if so, return 1 + the right side of the work where the 'th' is. 
        return 1 + count_th(word[2:])
    # otherwise 
    else:
        # return the other side of the word not containing 'th'
        return 0 + count_th(word[1:])

print(count_th("hellothere"))