from selenium.webdriver.common.by import By
from .base_page import BasePage

class PurchasePage(BasePage):
  def fill_purchase_form(self, name, country, city, card, month, year):
    name_input = (By.ID, 'name')
    self.send_keys(name_input, name)
    country_input = (By.ID, 'country')
    self.send_keys(country_input, country)
    city_input = (By.ID, 'city')
    self.send_keys(city_input, city)
    credit_card_input = (By.ID, 'card')
    self.send_keys(credit_card_input, card)
    month_input = (By.ID, 'month')
    self.send_keys(month_input, month)
    year_input = (By.ID, 'year')
    self.send_keys(year_input, year)
    purchase_button = (By.XPATH, '//*[@id="orderModal"]/div/div/div[3]/button[2]')
    self.click(purchase_button)

  def get_confirmation_text(self):
    success_text = (By.XPATH, '/html/body/div[10]/h2')
    return self.get_text(success_text)
