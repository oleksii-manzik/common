import pytest
from tests_practice.homework import (convert_to_minutes_seconds,
                                     find_largest_word,
                                     backwards_order_str,
                                     generate_fibonnaci_nums,
                                     even_nums,
                                     add_up_nums,
                                     factorial,
                                     following_letter_capitalize_vowel,
                                     sort_alphabetical_order,
                                     is_num2_greater_num1)


@pytest.mark.parametrize('test_input, expected', [(63, '1:3'), (120, '2:0')])
def test_task_11(test_input, expected):
    assert convert_to_minutes_seconds(test_input) == expected


@pytest.mark.parametrize('test_input, expected',
                         [('fun&!! time', 'time'), ('I love dogs', 'love')])
def test_task_12(test_input, expected):
    assert find_largest_word(test_input) == expected


def test_task_13(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda: 'My name is Michele')

    assert backwards_order_str() == 'Michele is name My'


def test_task_14(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda: '5')

    assert generate_fibonnaci_nums() == [1, 1, 2, 3, 5]


def test_task_15():
    assert even_nums([1, 2, 4, 90, 81]) == [2, 4, 90]


def test_task_16(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda: '10')

    assert add_up_nums() == 55


def test_task_17():
    assert factorial(4) == 24


@pytest.mark.parametrize('test_input, expected',
                         [('abcd', 'bcdE'), ('zza', 'AAb')])
def test_task_18(test_input, expected):
    assert following_letter_capitalize_vowel(test_input) == expected


@pytest.mark.parametrize('test_input, expected',
                         [('edcba', 'abcde'), ('.c.g.pa', 'acgp'), ('.4', '')])
def test_task_19(test_input, expected):
    assert sort_alphabetical_order(test_input) == expected


@pytest.mark.parametrize('test_input1, test_input2, expected',
                         [(1, 2, True), (3, 1, False), (1, 1, '-1')])
def test_task_20(test_input1, test_input2, expected):
    assert is_num2_greater_num1(test_input1, test_input2) == expected
