# The below function doesn't work correctly. It should sum all the numbers at the
# current time. For example, 01:02:03 should return 6. Improve and fix the function,
# and write unit test(s) for it. Use any testing framework you're familiar with.


# [TODO]: fix the function
def sum_current_time(time_str: str) -> int:
    """Expects data in the format HH:MM:SS"""
    valid_input = check_valid_input(time_str)
    if valid_input:
        sum_of_nums = 0
        list_of_nums = time_str.split(":")
        for num in list_of_nums:
            sum_of_nums += int(num)
        return sum_of_nums


def check_valid_input(time_str):
    if not isinstance(time_str, str):
        raise TypeError
    if time_str.count(':') != 2:
        raise ValueError
    return True
