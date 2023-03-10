# Unit tests to check your answer
# Feel free to add more!

import unittest
import random
import math
from avl_tree import AVLTree

# Seeds make random number generators return numbers "deterministically"
# In other words, you get the same random numbers each time you run the program!
random.seed(0)


class TestAVLTree(unittest.TestCase):
    def compare_tree_expected(self, values: list):
        """
        Helper function that sorts the given list and compares the result to
        an inorder traversal of the AVL.
        """
        expected = sorted(values)
        tree = AVLTree(values)
        # Check correctness
        actual = tree.traverse()
        self.assertEqual(expected, actual)
        # Check height is within 2 of expected (base 2 log)
        expected_height = math.ceil(math.log2(len(expected))) if expected else 0
        self.assertAlmostEqual(expected_height, tree._get_height(tree.root), delta=2)
        # Check balance is within 2
        self.assertAlmostEqual(0, tree._get_balance(tree.root), delta=1)

    def test_empty_tree(self):
        """Test an empty tree"""
        self.compare_tree_expected([])

    def test_one_item_tree(self):
        """Test a tree with one item"""
        self.compare_tree_expected([5])

    def test_small_trees_ordered(self):
        """Small Ascending Ordered Trees"""
        self.compare_tree_expected([0, 1, 2])
        self.compare_tree_expected([2, 5, 10])
        self.compare_tree_expected([100, 101, 102])

    def test_small_trees_reversed(self):
        """Small Reverse Order Trees"""
        self.compare_tree_expected([2, 1, 0])
        self.compare_tree_expected([102, 101, 100])

    def test_small_trees_jumbled(self):
        """Small Jumbled Trees"""
        self.compare_tree_expected([100, 50, 75])
        self.compare_tree_expected([1, 3, 2])
        self.compare_tree_expected([2, 1, 3])
        self.compare_tree_expected([3, 1, 2])

    def test_big_trees_jumbled_duplicates(self):
        """Bigger Tree with no duplicates"""
        self.compare_tree_expected(
            [16, 29, 12, 22, 28, 5, 21, 26, 13, 1, 14, 20, 18, 24, 27, 7, 9, 19, 11, 6, 2, 0, 8, 23, 4, 3, 10, 15, 25,
             17])

    def test_big_trees_jumbled_uniques(self):
        """Bigger Tree with duplicates"""
        self.compare_tree_expected([1, 5, 3, 4, 5, 6, 7, 3, 2, 4, 5, 6, 4, 4, 5, 6, 4, 5, 6, 4, 6, 5, 5, 4, 5, 6, 7])

    def test_big_tree_ordered(self):
        """Bigger Tree in Order"""
        self.compare_tree_expected(
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24])

    def test_massive_random_tree1(self):
        """1000 Element Tree with Numbers from 0-10"""
        self.compare_tree_expected([random.randint(0, 10) for _ in range(1000)])

    def test_massive_random_tree2(self):
        """10000 Element Tree with Numbers from 0-10"""
        self.compare_tree_expected([random.randint(0, 10) for _ in range(10000)])

    def test_massive_random_tree3(self):
        """10000 Element Tree with Numbers from -100000 to 100000"""
        self.compare_tree_expected([random.randint(-100000, 100000) for _ in range(10000)])

    def test_many_same_then_left(self):
        """Small Tree from 5, 5, 5, 5, 4"""
        self.compare_tree_expected([5, 5, 5, 5, 4])

    def test_many_same_then_right(self):
        """Small Tree from 5, 5, 5, 5, 6"""
        self.compare_tree_expected([5, 5, 5, 5, 6])


if __name__ == "__main__":
    unittest.main()