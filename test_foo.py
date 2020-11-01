import pytest

class Test_ABC:

   def setup_class(self):
       print("------->setup_class")

   def teardown_class(self):
       print("------->teardown_class")

   def test_a(self):
       print("------->test_a")
       assert 1

   def test_b(self):
       print("------->test_b")

   def test_c(self):
       print("------->test_c")

   def test_d(self):
       print("------->test_d")