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


def tast_perfect_power(number):
    n = int(number)
    v = set()
    v.add(1)

    for i in range(2, n + 1):
        if (i * i <= n):
            j = i * i
            v.add(j)
            while (j * i <= n):
                v.add(j * i)
                j = j * i
    perfectPower = len(v)
    return perfectPower


def main(argv):
    strArgs = ""
    strTask = ""

    try:
        opts, args = getopt.getopt(argv, "ht:a:", ["task=", "arg="])
    except getopt.GetoptError:
        print('wrong input')
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
        result = tast_perfect_power(strArgs)
    elif (strTask == "lazy"):
        result = 'Task = ' + strTask + ' Args = ' + strArgs

    print (result)

if __name__ == "__main__":
    main(sys.argv[1:])
