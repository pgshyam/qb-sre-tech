import unittest
from generate import Generate
import shutil, tempfile
from os import path

class TestGenerator(unittest.TestCase):
  def setUp(self):
      # Create a temporary directory
      self.test_dir = tempfile.mkdtemp()

  def tearDown(self):
      # Remove the directory after the test
      shutil.rmtree(self.test_dir)

  def test_generated_string_is_random(self):
        s1 = Generate.str_generator()
        s2 = Generate.str_generator()
        self.assertNotEqual(s1, s2)
  def test_generated_string_len_is_valid(self):
        s2 = Generate.str_generator(65)
        self.assertTrue(len(s2) > 1 and len(s2) <= 65)

  def test_generated_only_5th_file_contains_String(self):
        Generate.dirpath = self.test_dir
        Generate.filename_prefix = "file" 
        file_5_addition = "Test String!"
        #test to check if 5th file contains the Test String!   
        filename = Generate.filename(5)
        Generate.generate(5, file_5_addition)
        with open(filename) as fh:
          content = fh.read()
        self.assertTrue(file_5_addition in content)

        #test to check if non 5th file contains the Test String!   
        filename = Generate.filename(3)
        with open(filename) as fh:
          content = fh.read()
        self.assertTrue(file_5_addition not in content)   


  def test_generated_7th_file_is_aggregate(self):
        Generate.dirpath = self.test_dir
        Generate.filename_prefix = "file" 
        Generate.generate(7, "Hello")
        file_7_size = path.getsize(Generate.filename(7))
        expected_size = 0
        for i in range(6):
          filename = Generate.filename(i+1)
          expected_size += path.getsize(filename)
        
        self.assertEquals(expected_size, file_7_size)     

def main():
    unittest.main()

if __name__ == "__main__":
    main()
