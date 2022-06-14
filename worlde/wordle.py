import pygsheets
import random
gc = pygsheets.authorize(service_file=r'C:\Users\luisg\Desktop\worlde\icant.json')
sh = gc.open('wordle')
wks = sh.worksheet_by_title('Sheet1')
wordlist = wks.get_col(1)
def guesser(word,guess):
    result = []
    if guess[0] == word[0]:
        result.append(2)
    elif guess[0] in word:
        result.append(1)
    else:
        result.append(0)
    if guess[1] == word[1]:
        result.append(2)
    elif guess[1] in word:
        result.append(1)
    else:
        result.append(0)
    if guess[2] == word[2]:
        result.append(2)
    elif guess[2] in word:
        result.append(1)
    else:
        result.append(0)
    if guess[3] == word[3]:
        result.append(2)
    elif guess[3] in word:
        result.append(1)
    else:
        result.append(0)
    if guess[4] == word[4]:
        result.append(2)
    elif guess[4] in word:
        result.append(1)
    else:
        result.append(0)
    return result
def solver(letters=[]):
    words = []
    if len(letters) == 1:
        for x in wordlist:
            if letters[0] in x:
                words.append(x)
    elif len(letters) == 2:
        for x in wordlist:
            if letters[0] in x and letters[1] in x:
                words.append(x)
    elif len(letters) == 3:
        for x in wordlist:
            if letters[0] in x and letters[1] in x and letters[2] in x:
                words.append(x)
    elif len(letters) == 4:
        for x in wordlist:
            if letters[0] in x and letters[1] in x and letters[2] in x and letters[3] in x:
                words.append(x)
    elif len(letters) == 5:
        for x in wordlist:
            if letters[0] in x and letters[1] in x and letters[2] in x and letters[3] in x and letters[4] in x:
                words.append(x)
    return words

def filteredSolver(letters,wordbank):
    words = []
    if len(letters) == 1:
        for x in wordbank:
            if letters[0] in x:
                words.append(x)
    elif len(letters) == 2:
        for x in wordbank:
            if letters[0] in x and letters[1] in x:
                words.append(x)
    elif len(letters) == 2:
        for x in wordbank:
            if letters[0] in x and letters[1] in x:
                words.append(x)
    elif len(letters) == 3:
        for x in wordbank:
            if letters[0] in x and letters[1] in x and letters[2] in x:
                words.append(x)
    elif len(letters) == 4:
        for x in wordbank:
            if letters[0] in x and letters[1] in x and letters[2] in x and letters[3] in x:
                words.append(x)
    elif len(letters) == 5:
        for x in wordbank:
            if letters[0] in x and letters[1] in x and letters[2] in x and letters[3] in x and letters[4] in x:
                words.append(x)
    return words
def graySolver(letters=[],block=[],wordlists=[]):
    words = []
    if wordlists == []:
        lists = wordlist
    else:
        lists = wordlists
    if len(letters) == 1:
        for x in lists:
            if letters[0] in x:
                if letters[0] == x[block[0]]:
                    lists.remove(x)
    elif len(letters) == 2:
        for x in lists:
            if letters[0] in x or letters[1] in x:
                if letters[0] == x[block[0]] and letters[1] == x[block[1]]:
                    lists.remove(x)
    elif len(letters) == 3:
        for x in lists:
            if letters[0] in x or letters[1] in x or letters[2] in x:
                if letters[0] == x[block[0]] and letters[1] == x[block[1]] and letters[2] == x[block[2]]:
                    lists.remove(x)

    return lists
            

def yellowfilter(words,letters,positions):
    fixed = words


    removed = 0
    for x in words:
        if len(positions) == 1:
            if x[positions[0]] == letters[0]:
                
                removed += 1
                fixed.remove(x)
        elif len(positions) == 2:
            if x[positions[0]] == letters[0] or x[positions[1]] == letters[1]:
                
                removed += 1
                fixed.remove(x)
        elif len(positions) == 3:
            if x[positions[0]] == letters[0] or x[positions[1]] == letters[1] or x[positions[2]] == letters[2]:
                
                removed += 1
                fixed.remove(x)
        elif len(positions) == 4:
            if x[positions[0]] == letters[0] or x[positions[1]] == letters[1] or x[positions[2]] == letters[2] or x[positions[3]] == letters[3]:
                
                removed += 1
                fixed.remove(x)
        elif len(positions) == 5:
            if x[positions[0]] == letters[0] or x[positions[1]] == letters[1] or x[positions[2]] == letters[2] or x[positions[3]] == letters[3] or x[positions[4]] == letters[4]:
                
                removed += 1

                fixed.remove(x)


    return fixed,removed
def greenfilter(words,letters,positions):
    removed = 0
    for x in words:
        for y in range(len(positions)):
            if x[positions[y]] != letters[y]:
                removed += 1
                words.remove(x)
                break
    return words,removed
def giveGuess(result,word,wordlists=[]):
    blockedchar = []
    blockedpos = []
    yellowchar = []
    greenchar = []
    yellowpos = []
    greenpos = []
    word1 = 'salet'

    #r1 = guesser('beast',word1)
    if wordlists == []:
        for x in range(len(result)):
            if result[x] == 0:
                blockedchar.append(word[x])
                blockedpos.append(x)
            elif result[x] == 1:
                yellowchar.append(word[x])
                yellowpos.append(x)
            else:
                greenchar.append(word[x])
                greenpos.append(x)
        
        if len(yellowchar+greenchar) != 0:
            words = solver(yellowchar+greenchar)
            
            if len(blockedchar) > 0:
                print(blockedchar,blockedpos)
                words = graySolver(blockedchar,blockedpos,words)
                print(words)
                
        else:
            words = graySolver(blockedchar,blockedpos)

        
        if 1 in result:
            filtered = yellowfilter(words,yellowchar,yellowpos)
            while filtered[1] != 0:
                filtered = yellowfilter(filtered[0],yellowchar,yellowpos)

        if 2 in result:
            if 1 in result:
                greenfiltered = greenfilter(filtered[0],greenchar,greenpos)
            else:
                greenfiltered = greenfilter(words,greenchar,greenpos)
            while greenfiltered[1] != 0:
                greenfiltered = greenfilter(greenfiltered[0],greenchar,greenpos)

            randomguess = random.randint(0,len(greenfiltered[0])-1)
            
            return greenfiltered[0][randomguess],greenfiltered[0]
        else:
            
            randomguess = random.randint(0,len(words)-1)
            
            return words[randomguess],words
    else:
        for x in range(len(result)):
            if result[x] == 0:
                blockedchar.append(word[x])
                blockedpos.append(x)
            elif result[x] == 1:
                yellowchar.append(word[x])
                yellowpos.append(x)
            else:
                greenchar.append(word[x])
                greenpos.append(x)

        if len(yellowchar+greenchar) != 0:
            
            words = filteredSolver(greenchar+yellowchar,wordlists)
            
            if len(blockedchar) > 0:
                words = graySolver(blockedchar,blockedpos,wordlists)
                print(words)
                
                
        else:
            words = graySolver(blockedchar,blockedpos)
        randomguess = random.randint(0,len(words)-1)
        return words[randomguess],words
        
    
    
if __name__ == '__main__':
    guess,wordBank = giveGuess([0,1,1,0,0],'salet')
    print(guess)
    for x in wordBank:
        if 's' in x or 'e' in x or 't' in x:
            print(x)