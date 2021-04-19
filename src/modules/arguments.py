import argparse


def get_console_arguments():
    # Parse console arguments
    parser = argparse.ArgumentParser(description='Memory Maneuver Puzzle')
    parser.add_argument('--s', dest='chosen_strategy', type=int, choices=[1, 2], default=1, required=False,
                        help='Chosen strategy to solve this puzzle')

    parser.add_argument('--im', dest='input_mode', type=str, choices=["cmd", "file"], default="cmd",
                        required=False, help="Input mode")

    parser.add_argument("--f", dest='file_path', type=str, required=False, default="input.txt",
                        help='Path to input file if the input source if from file')

    parser.add_argument("--l", dest='numbers_lists', nargs="+", required=False, default=[], action='append',
                        help='Input data as list of numbers if the input source is from cmd')

    return parser.parse_args()
