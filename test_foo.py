import pytest
import allure

@allure.epic('My Epic')
@allure.feature('My Feature')
class Test_ABC:

    def setup_class(self):
        print("------->setup_class")

    def teardown_class(self):
        print("------->teardown_class")

    @allure.story('Test A')
    @allure.severity('blocker')
    def test_a(self):
        print("------->test_a")
        assert 1

    @allure.story('Test B')
    @allure.severity('major')
    def test_b(self):
        print("------->test_b")

    @allure.story('Test C')
    @allure.severity('normal')
    def test_c(self):
        print("------->test_c")

    @allure.story('Test D')
    @allure.severity('minor')
    def test_d(self):
        print("------->test_d")
    
    @allure.story('Test E')
    @allure.severity('minor')
    def test_e(self):
        print("------->test_e")