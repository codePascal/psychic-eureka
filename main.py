"""
Gets project number from user and runs program.
"""
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('n', help='project number', type=int)
    return list(vars(parser.parse_args()).values())[0]


if __name__ == '__main__':
    args = parse_arguments()
