'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # base case if the lenght of the word is less than 2 
        # return 0 
    # check if the left side of the word contains 'th'
        # if so, return 1 + the right side of the work where the 'th' is
    # otherwise 
        # return the other side of the word not containing 'th'
    pass

print(count_th("svhthhellothis"))