import pygsheets
import random
gc = pygsheets.authorize(service_file=r'C:\Users\luisg\Desktop\worlde\icant.json')
sh = gc.open('wordle')
wks = sh.worksheet_by_title('Sheet1')
wordlist = wks.get_col(1)
def grayFilter(word,result,wordBank=[],position=[0,1,2,3,4]):
    checked = 0
    greenwords = []
    yellowwords = []
    graywords = []
    green = []
    yellow = []
    gray = []
    if wordBank == []:
        wordList = wordlist
    else:
        wordList = wordBank
        print(wordList)
    for x in range(len(result)):
        if result[x] == 2:
            green.append(position[x])
        elif result[x] == 1:
            yellow.append(position[x])
        else:
            gray.append(position[x])


    if len(green) > 0:
        for x in wordList:
            if len(green) == 1:
                if x[green[0]] == word[green[0]]:
                    greenwords.append(x)
            elif len(green) == 2:
                if x[green[0]] == word[green[0]] and x[green[1]] == word[green[1]]:
                    greenwords.append(x)
            elif len(green) == 3:
                if x[green[0]] == word[green[0]] and x[green[1]] == word[green[1]] and x[green[2]] == word[green[2]]:
                    greenwords.append(x)
            elif len(green) == 4:
                if x[green[0]] == word[green[0]] and x[green[1]] == word[green[1]] and x[green[2]] == word[green[2]] and x[green[3]] == word[green[3]]:
                    greenwords.append(x)
    if len(yellow) > 0:
        if len(green) > 0:
            for x in greenwords:
                if len(yellow) == 1:
                    if word[yellow[0]] in x:
                        if word[yellow[0]] != x[yellow[0]]:
                            yellowwords.append(x)
                if len(yellow) == 2:
                    if word[yellow[0]] in x and word[yellow[1]] in x:
                        if word[yellow[0]] != x[yellow[0]] and word[yellow[1]] != x[yellow[1]]:
                            yellowwords.append(x)
                if len(yellow) == 3:
                    if word[yellow[0]] in x and word[yellow[1]] in x and word[yellow[2]] in x:
                        if word[yellow[0]] != x[yellow[0]] and word[yellow[1]] != x[yellow[1]] and word[yellow[2]] != x[yellow[2]]:
                            yellowwords.append(x)
                if len(yellow) == 4:
                    if word[yellow[0]] in x and word[yellow[1]] in x and word[yellow[2]] in x and word[yellow[3]] in x:
                        if word[yellow[0]] != x[yellow[0]] and word[yellow[1]] != x[yellow[1]] and word[yellow[2]] != x[yellow[2]] and word[yellow[3]] != x[yellow[3]]:
                            yellowwords.append(x)
        else:
            for x in wordList:
                if len(yellow) == 1:
                    if word[yellow[0]] in x:
                        if word[yellow[0]] != x[yellow[0]]:
                            yellowwords.append(x)
                if len(yellow) == 2:
                    if word[yellow[0]] in x and word[yellow[1]] in x:
                        if word[yellow[0]] != x[yellow[0]] and word[yellow[1]] != x[yellow[1]]:
                            yellowwords.append(x)
                if len(yellow) == 3:
                    if word[yellow[0]] in x and word[yellow[1]] in x and word[yellow[2]] in x:
                        if word[yellow[0]] != x[yellow[0]] and word[yellow[1]] != x[yellow[1]] and word[yellow[2]] != x[yellow[2]]:
                            yellowwords.append(x)
                if len(yellow) == 4:
                    if word[yellow[0]] in x and word[yellow[1]] in x and word[yellow[2]] in x and word[yellow[3]] in x:
                        if word[yellow[0]] != x[yellow[0]] and word[yellow[1]] != x[yellow[1]] and word[yellow[2]] != x[yellow[2]] and word[yellow[3]] != x[yellow[3]]:
                            yellowwords.append(x)

    if len(gray) > 0:
        if len(green) > 0 and len(yellow) == 0:
            for x in greenwords:
                if len(gray) == 1:
                    if word[gray[0]] not in x:
                        graywords.append(x)
                    else:
                        if word[gray[0]] != x[gray[0]]:
                            graywords.append(x)
                if len(gray) == 2:
                    if word[gray[0]] not in x and word[gray[1]] not in x:
                        graywords.append(x)
                    else:
                        if word[gray[0]] != x[gray[0]] and word[gray[1]] != x[gray[1]]:
                            graywords.append(x)
                if len(gray) == 3:
                    if word[gray[0]] not in x and word[gray[1]] not in x and word[gray[2]] not in x:
                        graywords.append(x)
                    else:
                        if word[gray[0]] != x[gray[0]] and word[gray[1]] != x[gray[1]] and word[gray[2]] != x[gray[2]]:
                            graywords.append(x)
                if len(gray) == 4:
                    if word[gray[0]] not in x and word[gray[1]] not in x and word[gray[2]] not in x and word[gray[3]] not in x:
                        graywords.append(x)
        elif len(green) > 0 and len(yellow) > 0:
            for x in yellowwords:
                if len(gray) == 1:
                    if word[gray[0]] not in x:
                        graywords.append(x)
                    else:
                        if word[gray[0]] != x[gray[0]]:
                            graywords.append(x)
                if len(gray) == 2:
                    if word[gray[0]] not in x and word[gray[1]] not in x:
                        graywords.append(x)
                    else:
                        if word[gray[0]] != x[gray[0]] and word[gray[1]] != x[gray[1]]:
                            graywords.append(x)
                if len(gray) == 3:
                    if word[gray[0]] not in x and word[gray[1]] not in x and word[gray[2]] not in x:
                        graywords.append(x)
                    else:
                        if word[gray[0]] != x[gray[0]] and word[gray[1]] != x[gray[1]] and word[gray[2]] != x[gray[2]]:
                            graywords.append(x)
        elif len(yellow) > 0 and len(green) == 0:
            for x in yellowwords:
                if len(gray) == 1:
                    if word[gray[0]] not in x:
                        graywords.append(x)
                    else:
                        if word[gray[0]] != x[gray[0]]:
                            graywords.append(x)
                if len(gray) == 2:
                    if word[gray[0]] not in x and word[gray[1]] not in x:
                        graywords.append(x)
                    else:
                        if word[gray[0]] != x[gray[0]] and word[gray[1]] != x[gray[1]]:
                            graywords.append(x)
                if len(gray) == 3:
                    if word[gray[0]] not in x and word[gray[1]] not in x and word[gray[2]] not in x:
                        graywords.append(x)
                    else:
                        if word[gray[0]] != x[gray[0]] and word[gray[1]] != x[gray[1]] and word[gray[2]] != x[gray[2]]:
                            graywords.append(x)
                if len(gray) == 4:
                    if word[gray[0]] not in x and word[gray[1]] not in x and word[gray[2]] not in x and word[gray[3]] not in x:
                        graywords.append(x)                   
        else:
            for x in wordList:
                if word[0] not in x and word[1] not in x and word[2] not in x and word[3] not in x and word[4] not in x:
                    graywords.append(x)
    if len(graywords) > 0:
        print('graywprds > 0')
        guessIndex = random.randint(0,len(graywords)-1)
        guess = graywords[guessIndex]
        bank = graywords
        return guess,bank
    elif len(yellowwords) > 0:
        print('yellowwords > 0')
        guessIndex = random.randint(0,len(yellowwords)-1)
        guess = yellowwords[guessIndex]
        bank = yellowwords
        return guess,bank
    else:
        print(graywords,yellowwords)
if __name__ == '__main__':
    guess,bank = grayFilter('salet',[0,1,0,0,0,])
    print(guess)
    print(bank)
    guess1,bank1 = grayFilter('furca',[0,2,0,0,2],bank)
    print(guess1)
    print(bank1)