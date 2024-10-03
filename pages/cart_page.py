from selenium.webdriver.common.by import By
from .base_page import BasePage

class CartPage(BasePage):
  def place_order(self):
    order_button = (By.XPATH, '//*[@id="page-wrapper"]/div/div[2]/button') 
    self.click(order_button)
    
  def remove_product_from_cart(self):
    delete_link = (By.LINK_TEXT, 'Delete')
    self.click(delete_link)
    
  def get_cart_products(self):
    products_in_cart = self.driver.find_elements(By.CSS_SELECTOR, '.success')
    return products_in_cart
