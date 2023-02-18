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

button = driver.find_element(By.XPATH,'//*[@id="headingTwo"]/h4/span').click()
time.sleep(3)

input = driver.find_element(By.XPATH,'//*[@id="collapseTwo"]/div/div/span/span[1]/span/ul/li/input').click()
time.sleep(3)

uls = driver.find_elements(By.XPATH,'//ul[contains(@class,"select2-results__options") and contains(@class, "select2-results__options--nested")]')
print(len(uls))

lis = []

for ul in uls:
    li = ul.find_elements(By.TAG_NAME,'li')
    for i in li:
        lis.append(i)

i = 0
data =[]
for i in range(0,14):
    print(i)
    uls = driver.find_elements(By.XPATH,'//ul[contains(@class,"select2-results__options") and contains(@class, "select2-results__options--nested")]')[i]
    lis = uls.find_elements(By.TAG_NAME,'li')
    for li in range(0,len(lis)):
        lis = driver.find_elements(By.XPATH,'//ul[contains(@class,"select2-results__options") and contains(@class, "select2-results__options--nested")]')[i].find_elements(By.TAG_NAME,'li')[li]
        text = lis.text
        select = lis.click()
        time.sleep(2)
        email_count = driver.find_element(By.XPATH,'//*[@id="resultat_recherche"]/div[1]/span[1]/h4/b')
        print(email_count.text)
        price = driver.find_element(By.XPATH,'//*[@id="resultat_recherche"]/div[1]/span[2]/small/span/h4/b').text
        print(price)
        
        data.append(['Region',text,email_count.text,price])

        
        time.sleep(2)
        uncheck = driver.find_element(By.XPATH,'//*[@id="collapseTwo"]/div/div/span/span[1]/span/ul/li[1]/span').click()
data = pd.DataFrame(data,columns=['Type','Cat','Email_count','Price'])
data.to_csv('region.csv',index=False)
driver.close()