'''The module is for summing all the numbers and verifying correct input'''


def sum_current_time(time_str: str) -> int:
    """Expects data in the format HH:MM:SS"""
    valid_input = check_valid_input(time_str)
    if valid_input:
        sum_of_nums = 0
        list_of_nums = time_str.split(":")
        for num in list_of_nums:
            sum_of_nums += int(num)
        return sum_of_nums
    raise NotImplementedError


def check_valid_input(time_str: str) -> True:
    '''Function to check that the input string is valid'''
    if not isinstance(time_str, str):
        raise TypeError
    if time_str.count(':') != 2:
        raise ValueError("Must have two colons in the string")
    if len(time_str) != 8:
        raise ValueError("String must have a length of 8 (including colons)")
    try:
        if int(time_str[0:2]) >= 24 or int(time_str[3:5]) >= 60 or int(time_str[6:8]) >= 60:
            raise ValueError("Must be in format HH:MM:SS")
    except ValueError:
        raise ValueError("Must be in format HH:MM:SS")
    return True
