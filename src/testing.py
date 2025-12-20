"""Unit tests for the Terraria clone game.

This module contains test suites for verifying the functionality of game
components including constants initialization and 1D-as-2D array operations.
"""

import unittest
import logging
import const
import pygame
import arr1d_as_2d


logging.basicConfig(level=logging.INFO)


class AbstractTest(unittest.TestCase):
    """Base test class providing logging functionality.

    Provides setUp and tearDown methods to log test execution.
    """

    def setUp(self):
        """Log the start of a test."""    
        logging.info("Starting test: %s", self.id())

    def tearDown(self):
        """Log the completion of a test."""   
        logging.info("Finished test: %s", self.id())

class TestConstants(AbstractTest):
    """Test suite for Constants class initialization."""

    def test_const_init_for_interp_err(self):
        """Test that Constants class initializes correctly with Pygame."""      
        pygame.init()
        test_constants = const.Constants()
        self.assertIsInstance(test_constants, const.Constants)

class Test1DArrayAs2d(AbstractTest):
    """Test suite for 1D-as-2D array functionality."""

    def test_1d_as_2d_np(self):
        """Test numpy-based 1D-as-2D array creation, access, and modification."""     
        test_np = arr1d_as_2d.create_1d_as_2d_np(1000, 1000)
        self.assertIsNotNone(test_np)
        self.assertEqual(arr1d_as_2d.get_1d_as_2d_np(test_np, 500, 500), 0)
        test_np = arr1d_as_2d.set_1d_as_2d_np(test_np, 79, 500, 500)
        self.assertEqual(arr1d_as_2d.get_1d_as_2d_np(test_np, 500, 500), 79)

    def test_1d_as_2d_ls(self):
        """Test list-based 1D-as-2D array creation, access, and modification."""  
        test_str = "Hello World!"
        test_ls = arr1d_as_2d.create_1d_as_2d_ls(1000, 1000)
        self.assertIsNotNone(test_ls)
        self.assertEqual(arr1d_as_2d.get_1d_as_2d_ls(test_ls, 500, 500), None)
        test_ls = arr1d_as_2d.set_1d_as_2d_ls(test_ls, test_str, 500, 500)
        self.assertEqual(arr1d_as_2d.get_1d_as_2d_ls(
            test_ls, 500, 500), test_str)
