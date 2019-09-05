def getLongestPath(string):
    levels = [0] * 100
    maxLen = -1
    currLen = 0
    levelLen = 0
    levelString = ""
    longestString = [None] * 100
    returnString = ""

    level = 0
    currLevel = 0
    incrLevel = False
    fileLevel = False
    for ch in string:
        if incrLevel:
            if ch == "\t":
                currLevel += 1
                continue
            else:
                incrLevel = False
                if currLevel < level:
                    level = currLevel
                    currLen = 0
                    for i in range(level):
                        currLen += levels[i]
                else:
                    level = currLevel
                currLevel = 0
        elif ch == "\n":
            incrLevel = True
            if fileLevel:
                fileLevel = False
                if currLen > maxLen:
                    returnString = ""
                    maxLen = currLen
                    for i in range(level):
                        returnString += longestString[i] + "/"
                    returnString += levelString
            else:
                longestString[level] = levelString
                levels[level] = levelLen
            levelLen = 0
            levelString = ""
            continue
        elif ch == ".":
            fileLevel = True

        levelString += ch
        levelLen += 1
        currLen += 1

    if fileLevel:
        fileLevel = False
        if currLen > maxLen:
            returnString = ""
            maxLen = currLen
            for i in range(level):
                returnString += longestString[i] + "/"
            returnString += levelString

    return returnString


if __name__ == '__main__':

    inp_string = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
    print(getLongestPath(inp_string))
