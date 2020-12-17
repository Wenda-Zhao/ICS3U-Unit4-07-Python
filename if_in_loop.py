#!/usr/bin/env python3

# Created by: Wenda Zhao
# Created on: Dec 2020
# This program for if_in_loop


def main():
    # this function for if_in_loop

    # process & output
    for model_number in range(1000, 2000 + 1):
        if model_number % 1 == 0 and model_number % 5 != 4:
            print("{0} ".format(model_number), end="")
        else:
            print("{0}".format(model_number))


if __name__ == "__main__":
    main()
