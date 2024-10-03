import pytest
from pages.cart_page import CartPage
from pages.product_page import ProductPage
import time

from pages.purchase_page import PurchasePage

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
  
def test_buy_product(setup_driver):
  # Step 1: Navigate to the products page
  product_page = ProductPage(setup_driver)
  
  # Step 2: Select a product and go to its page
  product_page.select_product() 

  # Step 3: Add the selected product to the cart
  product_page.add_product_to_cart()
  
  # Step 4: Close the confirmation modal
  time.sleep(2)
  alert = setup_driver.switch_to.alert
  alert.accept()
  
  # Step 5: Navigate to the cart and proceed to checkout
  product_page.navigate_to_products_cart()
  cart_page = CartPage(setup_driver)
  cart_page.place_order()

  # Step 6: Fill out the purchase form
  purchase_page = PurchasePage(setup_driver)
  purchase_page.fill_purchase_form(
      name='Juan Perez',
      country='Argentina',
      city='Buenos Aires',
      card='1234 5678 9012 3456',
      month='12',
      year='2024'
  )
  
  # Step 7: Verify the confirmation message
  confirmation_text = purchase_page.get_confirmation_text()
  assert 'Thank you for your purchase!' in confirmation_text
  