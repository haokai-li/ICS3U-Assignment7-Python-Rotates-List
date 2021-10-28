#!/usr/bin/env python3

# Created by: Haokai Li
# Created on: Oct 2021
# This Program calculate rotates and list


def calculated_rotates(calculate_user_number, calculate_k_number):
    # This function calculate rotates and list
    number_length = len(calculate_user_number)
    rotates_number = 0
    rotates_number_list = []

    # process
    for loop_number_first in range(calculate_k_number, number_length):
        rotates_number = calculate_user_number[loop_number_first]
        rotates_number_list.append(rotates_number)
    for loop_number_first in range(0, calculate_k_number):
        rotates_number = calculate_user_number[loop_number_first]
        rotates_number_list.append(rotates_number)

    return rotates_number_list


def main():
    # This function calculate rotates
    rotates_list = []
    user_rotates_number = None
    loop_number_first = 0
    loop_number_second = 0

    # output
    print("Please enter 1 integer at a time. Enter -1 to end.")
    print("")

    # input
    user_k_string = input("How many number do you rotate?: ")
    print("")

    try:
        user_k_number = int(user_k_string)
        while user_rotates_number != -1:
            # input
            user_rotates_string = input("What is your integer?: ")

            try:
                user_rotates_number = int(user_rotates_string)
                rotates_list.append(user_rotates_number)

            except Exception:
                # output
                print("You didn't enter an integer.")
    except Exception:
        # output
        print("You didn't enter an integer.")

    # remove -1
    rotates_list.pop()

    # check k length
    if user_k_number >= 0 and user_k_number <= len(rotates_list):
        # call functions
        rotates_number = calculated_rotates(
            rotates_list, calculate_k_number=user_k_number
        )
        # output
        print("")
        print("{}".format(rotates_number))
    else:
        # output
        print("")
        print("You have a error about rotates number.")

    print("\nDone.")


if __name__ == "__main__":
    main()
