import unittest

from tests_practice.homework import (common_between_two_lists,
                                     count_character,
                                     is_power_of_three,
                                     add_until_single_digit,
                                     push_zeros_to_end,
                                     is_arithmetic_progression,
                                     isnt_occur_twice,
                                     find_missing_num,
                                     count_until_tuple,
                                     reverse_str)


class Test10Functions(unittest.TestCase):

    def test_task_1(self):
        self.assertEqual(
            common_between_two_lists([1, 2, 3], [1, 2, 4]), [1, 2])
        self.assertEqual(
            common_between_two_lists([1, 2, 2], [0, 0, 0]), [])

    def test_task_2(self):
        self.assertEqual(
            count_character("I am a good developer. I am also a writer", 'a'),
            5)

    def test_task_3_true(self):
        self.assertTrue(is_power_of_three(9))
        self.assertTrue(is_power_of_three(3))
        self.assertTrue(is_power_of_three(729))

    def test_task_3_false(self):
        self.assertFalse(is_power_of_three(-3))
        self.assertFalse(is_power_of_three(0))
        self.assertFalse(is_power_of_three(1000))

    def test_task_4(self):
        self.assertEqual(add_until_single_digit(59), 5)
        self.assertEqual(add_until_single_digit(100), 1)

    def test_task_5(self):
        self.assertEqual(
            push_zeros_to_end([0, 2, 3, 4, 6, 7, 10]), [2, 3, 4, 6, 7, 10, 0])
        self.assertEqual(
            push_zeros_to_end([0, 0, 0, 1, 1, 1]), [1, 1, 1, 0, 0, 0])

    def test_task_6_true(self):
        self.assertTrue(is_arithmetic_progression([5, 7, 9, 11]))
        self.assertTrue(is_arithmetic_progression([1, 2, 3, 4]))

    def test_task_6_false(self):
        self.assertFalse(is_arithmetic_progression([5, 7, 9, 9]))
        self.assertFalse(is_arithmetic_progression([1, 2, 3, 5]))
        self.assertFalse(is_arithmetic_progression([0, 1]))

    def test_task_7(self):
        self.assertEqual(isnt_occur_twice([5, 3, 4, 3, 4]), 5)

    def test_task_8(self):
        self.assertEqual(find_missing_num([1, 2, 3, 4, 6, 7, 8]), 5)

    def test_task_9(self):
        self.assertEqual(count_until_tuple([1, 2, 3, (1, 2), 3]), 3)
        self.assertEqual(count_until_tuple([1, (1, 2), 3]), 1)

    def test_task_10(self):
        self.assertEqual(
            reverse_str("Hello World and Coders"), "sredoC dna dlroW olleH")


if __name__ == '__main__':
    unittest.main()
