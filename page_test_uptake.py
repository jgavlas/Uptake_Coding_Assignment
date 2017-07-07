import unittest
from selenium import webdriver
import Uptake_page
class UptakeNavigationTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://uptake.com")
    def test_Navigation(self):
         #Tests navigation between the homepage and Approach page of Uptake.com
        main_page = Uptake_page.MainPage(self.driver)
        print(main_page)
        assert main_page.currenturl() == "https://uptake.com/" , "URL doesn't match."
        main_page.search_text_element = "Approach"
        main_page.click_button()
        careers_page = Uptake_page.MainPage(self.driver)
        #Verify navigation to Approach
        assert careers_page.currenturl() == "https://uptake.com/approach" , "URL doesn't match."
        
    def tearDown(self):
            self.driver.close()
if __name__ == "__main__":
    unittest.main()
