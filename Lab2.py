print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")


#Exercise 2:

def display_main_menu():
    print("display_main_menu")


def get_user_input():
    print("get_user_input")


def calc_average(temp_list):
    print("calc_average")


def find_min_max(temp_list):
    print("find_min_max")


def sort_temperature(temp_list):
    print("sort_temperature")


def calc_median_temperature(temp_list):
    print("calc_median_temperature")


display_main_menu()
get_user_input()
calc_average([])
find_min_max([])
sort_temperature([])
calc_median_temperature([])

#Exercise 3:

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")


def get_user_input():
    user_input = input()
    string_list = user_input.split(",")
    float_list = []

    for value in string_list:
        float_list.append(float(value))

    return float_list


def calc_average(temp_list):
    total = 0

    for value in temp_list:
        total = total + value

    average = total / len(temp_list)
    return average


def find_min_max(temp_list):
    min_temp = temp_list[0]
    max_temp = temp_list[0]

    for value in temp_list:
        if value < min_temp:
            min_temp = value

        if value > max_temp:
            max_temp = value

    return [min_temp, max_temp]


def sort_temperature(temp_list):
    print("sort_temperature")


def calc_median_temperature(temp_list):
    print("calc_median_temperature")


display_main_menu()
numbers = get_user_input()

average = calc_average(numbers)
min_max = find_min_max(numbers)

print(f"Average: {average}")
print(f"Minimum: {min_max[0]}")
print(f"Maximum: {min_max[1]}")

#Exercise 4:

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")


def get_user_input():
    user_input = input()
    string_list = user_input.split(",")
    temperature_list = []

    for value in string_list:
        temperature_list.append(float(value))

    return temperature_list


def calc_average_temperature(temperature_list):
    total = 0

    for value in temperature_list:
        total = total + value

    average = total / len(temperature_list)
    return average


def calc_min_max_temperature(temperature_list):
    min_temp = temperature_list[0]
    max_temp = temperature_list[0]

    for value in temperature_list:
        if value < min_temp:
            min_temp = value

        if value > max_temp:
            max_temp = value

    return [min_temp, max_temp]


display_main_menu()
temperatures = get_user_input()

average = calc_average_temperature(temperatures)
min_max = calc_min_max_temperature(temperatures)

print(f"Average temperature: {average}")
print(f"Minimum temperature: {min_max[0]}")
print(f"Maximum temperature: {min_max[1]}")

#Exercise 6:



