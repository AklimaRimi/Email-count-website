from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import pandas as pd
import time


driver = webdriver.Chrome()

driver.get('https://fichier-entreprises.com/index.html#')
# driver.execute_script("window.scrollTo(0, window.scrollY-500);")
# time.sleep(15)
container = driver.find_element(By.XPATH,'//*[@id="wa-comphtml-j6rpfoox567934"]').find_element(By.TAG_NAME,'iframe') #.value_of_css_property('::before')
driver.switch_to.frame(container)
# "return window.getComputedStyle(document.querySelector('body>p.el'),':after').getPropertyValue('content')"
dept = driver.find_element(By.TAG_NAME,'span').click()

# depts = driver.find_element(By.XPATH,'//*[@id="select_departements"]')
# print(depts.text)

onecol = driver.find_element(By.ID,'collapseOne')
time.sleep(5)

data = []

for i in range(0,101):
    selects = onecol.find_element(By.ID,'select_departements').find_elements(By.TAG_NAME,'option')[i].click()
    text = onecol.find_element(By.ID,'select_departements').find_elements(By.TAG_NAME,'option')[i].text
    time.sleep(2)
    email_count = driver.find_element(By.XPATH,'//*[@id="resultat_recherche"]/div[1]/span[1]/h4')
    print(email_count.text)
    price = driver.find_element(By.XPATH,'//*[@id="resultat_recherche"]/div[1]/span[2]/small/span/h4/b').text
    print(price)
    
    data.append(['Department',Cat,email_count.text,price])
    uncheck = driver.find_element(By.XPATH,'//*[@id="collapseOne"]/div/div/span/span[1]/span/ul').find_element(By.XPATH,'//*[@id="collapseOne"]/div/div/span/span[1]/span/ul/li[1]/span').click()


data = pd.DataFrame(data,columns=['Type','Cat','Email_count','Price'])
data.to_csv('department.csv',index=False)

driver.close()