import unittest, logging, const, pygame


logging.basicConfig(level=logging.INFO)


class TestConstants(unittest.TestCase):
    def setUp(self):
        logging.info("Starting test: %s", self.id())
        
        
    def tearDown(self):
        logging.info("Finished test: %s", self.id())
        
        
    def test_const_init_for_interp_err(self):
        pygame.init()
        test_constants = const.Constants()
        self.assertIsInstance(test_constants, const.Constants)