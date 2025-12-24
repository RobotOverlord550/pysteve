import unittest
import logging


logging.basicConfig(level=logging.INFO)


class AbstractTest(unittest.TestCase):
    def setUp(self): 
        logging.info("Starting test: %s", self.id())

    def tearDown(self): 
        logging.info("Finished test: %s", self.id())
