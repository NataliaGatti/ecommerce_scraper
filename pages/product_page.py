from selenium.webdriver.common.by import By
from .base_page import BasePage


class ProductPage(BasePage):
  # Get products from the webpage
  def get_products(self):
    # Initialize a list to keep the data of each product
    products = []
    # Get all the products´ names
    names = self.driver.find_elements(By.CSS_SELECTOR, '.card-title a')
    # Get all the products´ prices
    prices = self.driver.find_elements(By.CSS_SELECTOR, '.card-block h5')
    
    # Iteration over all the products (from names and prices), build a dictionary with the requiered data and push them to products
    for name, price in zip(names, prices):
      product_data = {
        'name': name.text,
        'price': price.text,
        'link': name.get_attribute('href')
      }
      products.append(product_data)
    return products
      
  # Need to get to second page by click "Next" button
  def click_next_button(self):
    next_button = (By.CSS_SELECTOR, '#next2')
    self.click(next_button)
