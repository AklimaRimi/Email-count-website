from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import pandas as pd
import time


driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://fichier-entreprises.com/index.html#')
# driver.execute_script("window.scrollTo(0, window.scrollY-500);")
# time.sleep(15)
container = driver.find_element(By.XPATH,'//*[@id="wa-comphtml-j6rpfoox567934"]').find_element(By.TAG_NAME,'iframe') #.value_of_css_property('::before')
driver.switch_to.frame(container)
# "return window.getComputedStyle(document.querySelector('body>p.el'),':after').getPropertyValue('content')"
dept = driver.find_element(By.XPATH,'//*[@id="criteres_de_selections"]/div/div[2]/div[10]/div/span/span[1]/span/ul/li/input').click()

data =[]

lists = driver.find_elements(By.XPATH,'//li[contains(@class,"select2-results__option")]')
print(len(lists))
for i in range(0,9):
    print(i)
    lists = driver.find_elements(By.XPATH,'//li[contains(@class,"select2-results__option")]')
    text = lists[i].text
    select = lists[i].click()
    time.sleep(3)
    email_count = driver.find_element(By.XPATH,'//*[@id="resultat_recherche"]/div[1]/span[1]/h4')
    print(email_count.text)
    try:
        price = driver.find_element(By.XPATH,'//*[@id="resultat_recherche"]/div[1]/span[2]/small/span/h4/b').text
        print(price)
    except:
        price = 0
    
    data.append(['Nature of Business',text,email_count.text,price])
    uncheck = driver.find_element(By.XPATH,'//*[@id="criteres_de_selections"]/div/div[2]/div[10]/div/span/span[1]/span/ul/li[1]/span').click()
    
data = pd.DataFrame(data,columns=['Type','Cat','Email_count','Price'])
data.to_csv('nature.csv',index=False)

driver.close()