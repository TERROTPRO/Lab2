import Lab2

print("Test_Lab2")


def test_find_min_max():
    input_list = [5, 67, 32, 10, 88]
    expected_result = [5, 88]

    result = Lab2.find_min_max(input_list)

    assert result == expected_result


def test_calc_average():
    input_list = [5, 67, 32]
    expected_result = 34.666666666666664

    result = Lab2.calc_average(input_list)

    assert result == expected_result


def test_calc_average_with_negative_values():
    input_list = [-10, 0, 10]
    expected_result = 0

    result = Lab2.calc_average(input_list)

    assert result == expected_result


def test_calc_median_temperature_odd_number_of_values():
    input_list = [5, 67, 32]
    expected_result = 32

    result = Lab2.calc_median_temperature(input_list)

    assert result == expected_result


def test_calc_median_temperature_even_number_of_values():
    input_list = [5, 67, 32, 10]
    expected_result = 21

    result = Lab2.calc_median_temperature(input_list)

    assert result == expected_result