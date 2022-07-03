import math

def test_filter_result():
    test_list = [7, 1, 6, 4, 2 , 5, 3]
    result_list_more4 = [7, 6, 5]
    result_list_lees4 = [1, 2, 3]
    result_list_is4 = [4]
    assert result_list_more4 == list(filter(lambda x: x > 4, test_list))
    assert result_list_lees4 == list(filter(lambda x: x < 4, test_list))
    assert result_list_is4 == list(filter(lambda x: x == 4, test_list))


def test_map_size():
    test_list = [1, 2, 3, 4, 5, 6, 7]
    assert len(test_list) == len(list(map(lambda x: x * 2, test_list)))


def test_map_result():
    test_list = [1, 2, 3, 4, 5, 6, 7]
    test_list_x2 = [2, 4, 6, 8, 10, 12, 14]
    assert test_list_x2 == list(map(lambda x: x * 2, test_list))


def test_sorted_result():
    test_list_int = [7, 1, 6, 4, 2, 5, 3]
    result_list_int = [1, 2, 3, 4, 5, 6, 7]
    test_list_string = ['f', 'c', 'e', 'd', 'b', 'g', 'a']
    result_list_string = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    assert result_list_int == sorted(test_list_int)
    assert result_list_string == sorted(test_list_string)


def test_math_pi():
    assert math.pi == 3.141592653589793


def test_math_sqrt():
    assert math.sqrt(25) == 5
    assert math.sqrt(36) == 6


def test_math_pow():
    assert math.pow(5, 2) == 25
    assert math.pow(4, 0.5) == 2


def test_math_hypot():
    assert math.hypot(4, 3) == 5


