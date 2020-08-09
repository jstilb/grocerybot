from recipes import *
import random
from selenium import webdriver
from time import sleep





#creates a variable for randomly selected recipe for entrees & salads
salad_suggestion = salad_recipes[random.randint(0, len(salad_recipes) - 1)]
entree_suggestion = entree_recipes[random.randint(0, len(entree_recipes) - 1)]

#grocerybot
class GroceryBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        sleep(10)
        self.driver.get('https://www.kingsoopers.com/signin')
        sleep(5)

        email_in = self.driver.find_element_by_xpath('//*[@id="SignIn-emailInput"]')
        email_in.send_keys(jm_email)
        sleep(5)

        pw_in = self.driver.find_element_by_xpath('//*[@id="SignIn-passwordInput"]')
        pw_in.send_keys(jm_pw)
        sleep(5)

        login_btn = self.driver.find_element_by_xpath('//*[@id="SignIn-submitButton"]')
        login_btn.click()
        sleep(15)

        #escape popup
        escape_btn = self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div/div[1]/div[4]')
        escape_btn.click()
        sleep(5)

    def fillCart(self):
        for ingredient, info in salad_suggestion.items():
            quantity = 0
            specs = []
            for key in info.values():
                if isinstance(key, int):
                    quantity += key
                else:
                    specs.append(key)
            self.driver.get(specs[0])
            sleep(5)
            add_to_cart_btn = self.driver.find_element_by_class_name('kds-Stepper-ctaButton')
            add_to_cart_btn.click()
            sleep(3)
            quantity_input = self.driver.find_element_by_class_name('kds-Stepper-input')
            quantity_input.clear()
            quantity_input.send_keys(str(quantity))
            sleep(5)

        for ingredient, info in entree_suggestion.items():
            quantity = 0
            specs = []
            for key in info.values():
                if isinstance(key, int):
                    quantity += key
                else:
                    specs.append(key)
            self.driver.get(specs[0])
            sleep(5)
            add_to_cart_btn = self.driver.find_element_by_class_name('kds-Stepper-ctaButton')
            add_to_cart_btn.click()
            sleep(3)
            quantity_input = self.driver.find_element_by_class_name('kds-Stepper-input')
            quantity_input.clear()
            quantity_input.send_keys(str(quantity))
            sleep(5)



bot = GroceryBot()
bot.login()
bot.fillCart()
