import unittest, logging, const, pygame, arr1d_as_2d, numpy


logging.basicConfig(level=logging.INFO)



class AbstractTest(unittest.TestCase):
    def setUp(self):
        logging.info("Starting test: %s", self.id())
        
        
    def tearDown(self):
        logging.info("Finished test: %s", self.id())



class TestConstants(AbstractTest):
    def test_const_init_for_interp_err(self):
        pygame.init()
        test_constants = const.Constants()
        self.assertIsInstance(test_constants, const.Constants)
        
        
        
        
class Test1DArrayAs2d(AbstractTest):
    def test_1d_as_2d_np_small(self):
        test_np = arr1d_as_2d.create_1d_as_2d_np(1000, 1000)
        self.assertIs(test_np, )
    