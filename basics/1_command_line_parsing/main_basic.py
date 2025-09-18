# This is a sample Python script for parsing command line with basic


import sys

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    args = sys.argv[1:]  # skip script name
    options = {"count": 1}  # default

    i = 0
    while i < len(args):
        if args[i] == "--count" and i + 1 < len(args):
            options["count"] = int(args[i + 1])
            i += 2
        else:
            options["file"] = args[i]
            i += 1

    print(options)