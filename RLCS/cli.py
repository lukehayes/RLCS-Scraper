import argparse

parser = argparse.ArgumentParser(description="Print the Raylib documentation in the command line.")

parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

parser.add_argument('--search',
                    help='Search for a specific function name.')


args = parser.parse_args()

if args.search:
    print("Searching")
