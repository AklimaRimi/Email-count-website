from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time


driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://fichier-entreprises.com/index.html#')

container = driver.find_element(By.XPATH,'//*[@id="wa-comphtml-j6rpfoox567934"]').find_element(By.TAG_NAME,'iframe') #.value_of_css_property('::before')
driver.switch_to.frame(container)

sliders = driver.find_element(By.XPATH,'//*[@id="criteres_de_selections"]/div/div[2]/div[11]').click()
left_slider = driver.find_element(By.XPATH,'//*[@id="criteres_de_selections"]/div/div[2]/div[11]/div/div[2]/div/div[5]')
right_slider = driver.find_element(By.XPATH,'//div[contains(@class,"slider-handle max-slider-handle round")]')

time.sleep(10)
# date_left =  driver.find_element(By.XPATH,'//*[@id="criteres_de_selections"]/div/div[2]/div[13]/div/div[2]/div/div[5]').location
# date_right = driver.find_element(By.XPATH,'//*[@id="criteres_de_selections"]/div/div[2]/div[13]/div/div[2]/div/div[6]').location

x = left_slider.location
print(x)
# y =right_slider.location


# # ActionChains(driver).drag_and_drop_by_offset(left_slider, 25,0).perform()
ActionChains(driver).click_and_hold(driver.find_element(By.XPATH,'//*[@id="criteres_de_selections"]/div/div[2]/div[11]/div/div[2]/div/div[5]')).pause(2).move_by_offset(10,0).release().perform()
# ActionChains(driver).move_to_element(left_slider).pause(1).click_and_hold(left_slider).move_by_offset(10,0).release().perform()
# time.sleep(5)
print(left_slider = driver.find_element(By.XPATH,'//div[contains(@class,"slider-handle min-slider-handle round")]').location)
# # print(date_left,date_right)

# time.sleep(10)


driver.close()