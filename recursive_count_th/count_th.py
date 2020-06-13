'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

def count_th(word, count=0):
    if len(word) >= 2:
        if word[0:2] == 'th':
            count += 1
        segment = word[1:]
    else:
        return count
    
    return count_th(segment, count)


if __name__ == "__main__":
    print(count_th("they'retherightthen"))
        
    