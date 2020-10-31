import pytest

class Test_ABC:
   # 测试类级开始
   def setup_class(self):
       print("------->setup_class")
   # 测试类级结束
   def teardown_class(self):
       print("------->teardown_class")
   def test_a(self):
       print("------->test_a")
       assert 1
   def test_b(self):
       print("------->test_b")