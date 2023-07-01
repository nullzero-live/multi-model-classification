# Tests

import unittest
from app import gc_auth, process_data
from aorc import acc_aorc


class TestAppFunctions(unittest.TestCase):
    
        def test_gc_auth(self):
            try:
                gc_auth()
            except Exception:
                self.fail(f"test_gc_auth raised an exception")
            

        def test_process_data(self):
            try:
                process_data(df=gc_auth())
            except Exception:
                self.fail(f"process_data raised an exception")

if __name__ == '__main__':
    unittest.main()
        
            