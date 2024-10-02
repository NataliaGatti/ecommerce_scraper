from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
  def __init__(self, driver):
    self.driver = driver
    
  # wait that the element/locator could be visible before an action
  def wait_for_element(self, locator, timeout=20):
    return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
  
  # Define actions that I need on tests
  def click(self, locator):
    element = self.wait_for_element(locator)
    element.click()
    
  def get_text(self, locator):
    return self.wait_for_element(locator).text
  
  def get_attribute(self, locator, attribute):
    return self.wait_for_element(locator).get_attribute(attribute)