import getopt
import sys


def main(argv):
    strArgs = ""
    strTask = ""

    try:
        opts, args = getopt.getopt(argv, "ht:a:", ["task=", "arg="])
    except getopt.GetoptError:
        print('except: main.py --task= <action> --arg= <arguments>')
        # print('except !')
        sys.exit()
    for opt, arg in opts:
        if opt == '-h':
            print('help: main.py --task= <action> --arg= <arguments>')
            # print('help ')
            sys.exit()
        elif opt in ("--task", "--task="):
            strTask = arg
        elif opt in ("--arg", "--arg="):
            strArgs = arg

    print('Task = ' + strTask)
    print('Args = ' + strArgs)
    result = 0
    if (strTask == "vowels"):
         result = 'Task = ' + strTask + ' Args = ' + strArgs
    elif (strTask == "perfect"):
        result = 'Task = ' + strTask + ' Args = ' + strArgs
    elif (strTask == "lazy"):
        result = 'Task = ' + strTask + ' Args = ' + strArgs

    print (result)

if __name__ == "__main__":
    main(sys.argv[1:])
