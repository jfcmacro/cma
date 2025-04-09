# Tests
import unittest
import pytest
from parameterized import parameterized
from cont_mem_algos import best_fit
from utils.utils import print_memory_map,read_reqs_file,read_memmap_file

class TestBasicFirstFit(unittest.TestCase):
    MEMMAP = read_memmap_file("resources/memmap/memmap_2.txt")
    REQS = read_reqs_file("resources/reqs/reqs_2.txt")
    
    @parameterized.expand([(1,0x0FA000,0x14000),
                           (2,0x04B000,0x01E000),
                           (3,0x000000,0x046000),
                           (4,0x07d000,0x03e800),
                           ])
    def test_request(self,max_req,expected_base,expected_limit):
        work_memory = self.MEMMAP.copy()
        reqs = self.REQS.copy()[0:max_req]
        index = 0
            
        for req in reqs:
            work_memory,base,limit,index = best_fit(work_memory, req, index)
            
        self.assertEqual(base, expected_base)
        self.assertEqual(limit, expected_limit)

    @parameterized.expand([(1,(0x10e000,0x5000)),
                           (2,(0x069000,0x014000)),
                           (3,(0x046000,0x005000)),
                           #(4,(0x03e800,0x00c800)),
                           ])
    def test_wm_request(self,max_req,expected_memmap):
        work_memory = self.MEMMAP.copy()
        reqs = self.REQS.copy()[0:max_req]
        index = 0

        for req in reqs:
            work_memory,base,limit,index = best_fit(work_memory, req, index)
            
        self.assertEqual(work_memory[index], expected_memmap)

if __name__ == '__main__':
    unittest.main()

