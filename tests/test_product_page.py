import pytest
from pages.product_page import ProductPage
import time
import pdb

URL = "https://www.demoblaze.com/"

@pytest.fixture
def setup_driver(driver):
  driver.get(URL)
  yield driver
  driver.quit()

def test_scrape_products(setup_driver):
  time.sleep(10)
  product_page = ProductPage(setup_driver)
  
  all_products = []
  total_products = 0

  for _ in range(2):
      products = product_page.get_products()
      total_products += len(products)
      all_products.extend(products)
      
      if _ < 1:
          product_page.click_next_button()
          time.sleep(10)

  # Build the txt
  with open("output/products_info.txt", "w") as f:
      for product in all_products:
          f.write(f"Name: {product['name']}\n")
          f.write(f"Price: {product['price']}\n")
          f.write(f"Link: {product['link']}\n")
          f.write("\n")

  assert len(all_products) > 0, "No products were found"
  assert len(all_products) == total_products, "Missing products"
  