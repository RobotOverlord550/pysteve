import unittest
import logging
import const
import pygame
import arr1d_as_2d


logging.basicConfig(level=logging.INFO)


class AbstractTest(unittest.TestCase):
    def setUp(self):
        """_summary_
        """        
        logging.info("Starting test: %s", self.id())

    def tearDown(self):
        """_summary_
        """        
        logging.info("Finished test: %s", self.id())


class TestConstants(AbstractTest):
    def test_const_init_for_interp_err(self):
        """_summary_
        """        
        pygame.init()
        test_constants = const.Constants()
        self.assertIsInstance(test_constants, const.Constants)


class Test1DArrayAs2d(AbstractTest):
    def test_1d_as_2d_np(self):
        """_summary_
        """        
        test_np = arr1d_as_2d.create_1d_as_2d_np(1000, 1000)
        self.assertIsNotNone(test_np)
        self.assertEqual(arr1d_as_2d.get_1d_as_2d_np(test_np, 500, 500), 0)
        test_np = arr1d_as_2d.set_1d_as_2d_np(test_np, 79, 500, 500)
        self.assertEqual(arr1d_as_2d.get_1d_as_2d_np(test_np, 500, 500), 79)

    def test_1d_as_2d_ls(self):
        """_summary_
        """        
        test_str = "Hello World!"
        test_ls = arr1d_as_2d.create_1d_as_2d_ls(1000, 1000)
        self.assertIsNotNone(test_ls)
        self.assertEqual(arr1d_as_2d.get_1d_as_2d_ls(test_ls, 500, 500), None)
        test_ls = arr1d_as_2d.set_1d_as_2d_ls(test_ls, test_str, 500, 500)
        self.assertEqual(arr1d_as_2d.get_1d_as_2d_ls(
            test_ls, 500, 500), test_str)
