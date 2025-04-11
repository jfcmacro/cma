# Tests
import unittest
import pytest
from parameterized import parameterized
from cont_mem_algos import worst_fit
from utils.utils import print_memory_map,read_reqs_file,read_memmap_file

class TestBasicFirstFit(unittest.TestCase):
    MEMMAP = read_memmap_file("resources/memmap/memmap_2.txt")
    REQS = read_reqs_file("resources/reqs/reqs_2.txt")
    
    @parameterized.expand([(1,0x07d000,0x014000),
                           (2,0x091000,0x01E000),
                           (3,0x0af000,0x046000),
                           ])
    def test_request(self,max_req,expected_base,expected_limit):
        work_memory = self.MEMMAP.copy()
        reqs = self.REQS.copy()[0:max_req]
        index = 0
            
        for req in reqs:
            result = worst_fit(work_memory, req, index)
            if result != None:
                work_memory,base,limit,index = result
    
        self.assertEqual(base, expected_base)
        self.assertEqual(limit, expected_limit)

    @parameterized.expand([(1,(0x091000,0x069000)),
                           (2,(0x0af000,0x04b000)),
                           (3,(0x0f5000,0x005000)),
                           (4,(0x03e800,0x0c800)),
                          # (5,(0x043800,0x007800)),
                           ])
    def test_wm_request(self,max_req,expected_memmap):
        work_memory = self.MEMMAP.copy()
        reqs = self.REQS.copy()[0:max_req]
        index = 0

        for req in reqs:
            result = worst_fit(work_memory, req, index)
            if result != None:
                work_memory,base,limit,index = result
            
        self.assertEqual(work_memory[index], expected_memmap)

if __name__ == '__main__':
    unittest.main()
