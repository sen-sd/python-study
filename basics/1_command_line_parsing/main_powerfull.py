# This is a sample Python script for parsing command line effectively
# If we use sys then we can get with sys. But for complex argument this will be dificuly
# So it is preferred to use argparse

import argparse

# Sample command line - Vpython main_powerfull.py --count 10 data.txt
if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Demo command-line arguments.")
    parser.add_argument("filename", help="Input file name")
    parser.add_argument("--count", type=int, default=1, required=True, help="Number of times to print")

    args = parser.parse_args()

    print(f"File name = {args.filename}")
    print(f"Count = {args.count}")

