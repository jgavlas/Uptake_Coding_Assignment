from Uptake_elements import BasePageElement
from Uptake_locators import MainPageLocators

class SearchTextElement(BasePageElement):
    locator = 'Approach'

  
class BasePage(object):
    #Base class to intialize base page
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):
    #Variable to be searched and action methods
    search_text_element= SearchTextElement() #Variable that will contained the selected text
    def click_button(self):
        element = self.driver.find_element(*MainPageLocators.BUTTON)
        element.click()
    def currenturl(self):
        return self.driver.current_url
