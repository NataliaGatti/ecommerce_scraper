from selenium.webdriver.common.by import By
from .base_page import BasePage

class CartPage(BasePage):
  def place_order(self):
    order_button = (By.XPATH, '//*[@id="page-wrapper"]/div/div[2]/button') 
    self.click(order_button)
