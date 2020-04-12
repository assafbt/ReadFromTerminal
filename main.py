import getopt, sys

def task_vowels(strSentence):
    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
    countVowels = 0
    strSentence = strSentence.casefold()
    for letter in strSentence:
        for vowl in vowels:
            if (letter == vowl):
                countVowels += 1
                continue
    return countVowels


def main(argv):
    strArgs = ""
    strTask = ""

    try:
        opts, args = getopt.getopt(argv, "ht:a:", ["task=", "arg="])
    except getopt.GetoptError:
        print('except: main.py --task= <action> --arg= <arguments>')
        sys.exit()
    for opt, arg in opts:
        if opt == '-h':
            print('help: main.py --task= <action> --arg= <arguments>')
            sys.exit()
        elif opt in ("--task", "--task="):
            strTask = arg
        elif opt in ("--arg", "--arg="):
            strArgs = arg

    print('Task = ' + strTask)
    print('Args = ' + strArgs)
    result = 0
    if (strTask == "vowels"):
         result = task_vowels(strArgs)
    elif (strTask == "perfect"):
        result = 'Task = ' + strTask + ' Args = ' + strArgs
    elif (strTask == "lazy"):
        result = 'Task = ' + strTask + ' Args = ' + strArgs

    print (result)

if __name__ == "__main__":
    main(sys.argv[1:])
