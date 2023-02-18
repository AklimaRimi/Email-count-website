
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import pandas as pd
import time


# driver = webdriver.Chrome()
# driver.maximize_window()

# driver.get('https://fichier-entreprises.com/index.html#')
# # driver.execute_script("window.scrollTo(0, window.scrollY-500);")
# # time.sleep(15)
# container = driver.find_element(By.XPATH,'//*[@id="wa-comphtml-j6rpfoox567934"]').find_element(By.TAG_NAME,'iframe') #.value_of_css_property('::before')
# driver.switch_to.frame(container)
# # "return window.getComputedStyle(document.querySelector('body>p.el'),':after').getPropertyValue('content')"
# dept = driver.find_element(By.XPATH,'//*[@id="criteres_de_selections"]/div/div[2]/div[4]/span/span[1]').click()


# onecol = driver.find_element(By.XPATH,'/html/body/span/span/span')
# time.sleep(5)

# data = []
# cats = driver.find_elements(By.CLASS_NAME,'select2-results__option')

    
# for i in range(0,50):
#     print(i)
#     cat = driver.find_elements(By.CLASS_NAME,'select2-results__option')
#     select = cat[i].click()
    
#     time.sleep(3)
#     email_count = driver.find_element(By.XPATH,'//*[@id="resultat_recherche"]/div[1]/span[1]/h4')
#     print(email_count.text)
#     try:
#         price = driver.find_element(By.XPATH,'//*[@id="resultat_recherche"]/div[1]/span[2]/small/span/h4/b').text
#         print(price)
#     except:
#         price = 0
    
#     data.append(['Selection',email_count.text,price])
#     uncheck = driver.find_element(By.XPATH,'//*[@id="criteres_de_selections"]/div/div[2]/div[4]/span/span[1]/span/ul/li[1]').find_element(By.XPATH,'//*[@id="criteres_de_selections"]/div/div[2]/div[4]/span/span[1]/span/ul/li[1]/span').click()
# data = pd.DataFrame(data,columns=['Type','Email_count','Price'])
# data.to_csv('selection1.csv',index=False)



# for i in range(50,100):
#     print(i)
#     cat = driver.find_elements(By.CLASS_NAME,'select2-results__option')
#     select = cat[i].click()
    
#     time.sleep(3)
#     email_count = driver.find_element(By.XPATH,'//*[@id="resultat_recherche"]/div[1]/span[1]/h4')
#     print(email_count.text)
#     try:
#         price = driver.find_element(By.XPATH,'//*[@id="resultat_recherche"]/div[1]/span[2]/small/span/h4/b').text
#         print(price)
#     except:
#         price = 0
    
#     data.append(['Selection',email_count.text,price])
#     uncheck = driver.find_element(By.XPATH,'//*[@id="criteres_de_selections"]/div/div[2]/div[4]/span/span[1]/span/ul/li[1]').find_element(By.XPATH,'//*[@id="criteres_de_selections"]/div/div[2]/div[4]/span/span[1]/span/ul/li[1]/span').click()
# data = pd.DataFrame(data,columns=['Type','Email_count','Price'])
# data.to_csv('selection2.csv',index=False)

# for i in range(100,150):
#     print(i)
#     cat = driver.find_elements(By.CLASS_NAME,'select2-results__option')
#     select = cat[i].click()
    
#     time.sleep(3)
#     email_count = driver.find_element(By.XPATH,'//*[@id="resultat_recherche"]/div[1]/span[1]/h4')
#     print(email_count.text)
#     try:
#         price = driver.find_element(By.XPATH,'//*[@id="resultat_recherche"]/div[1]/span[2]/small/span/h4/b').text
#         print(price)
#     except:
#         price = 0
    
#     data.append(['Selection',email_count.text,price])
#     uncheck = driver.find_element(By.XPATH,'//*[@id="criteres_de_selections"]/div/div[2]/div[4]/span/span[1]/span/ul/li[1]').find_element(By.XPATH,'//*[@id="criteres_de_selections"]/div/div[2]/div[4]/span/span[1]/span/ul/li[1]/span').click()
# data = pd.DataFrame(data,columns=['Type','Email_count','Price'])
# data.to_csv('selection3.csv',index=False)

# for i in range(150,200):
#     print(i)
#     cat = driver.find_elements(By.CLASS_NAME,'select2-results__option')
#     select = cat[i].click()
    
#     time.sleep(3)
#     email_count = driver.find_element(By.XPATH,'//*[@id="resultat_recherche"]/div[1]/span[1]/h4')
#     print(email_count.text)
#     try:
#         price = driver.find_element(By.XPATH,'//*[@id="resultat_recherche"]/div[1]/span[2]/small/span/h4/b').text
#         print(price)
#     except:
#         price = 0
    
#     data.append(['Selection',email_count.text,price])
#     uncheck = driver.find_element(By.XPATH,'//*[@id="criteres_de_selections"]/div/div[2]/div[4]/span/span[1]/span/ul/li[1]').find_element(By.XPATH,'//*[@id="criteres_de_selections"]/div/div[2]/div[4]/span/span[1]/span/ul/li[1]/span').click()
# data = pd.DataFrame(data,columns=['Type','Email_count','Price'])
# data.to_csv('selection4.csv',index=False)

# for i in range(200,250):
#     print(i)
#     cat = driver.find_elements(By.CLASS_NAME,'select2-results__option')
#     select = cat[i].click()
    
#     time.sleep(3)
#     email_count = driver.find_element(By.XPATH,'//*[@id="resultat_recherche"]/div[1]/span[1]/h4')
#     print(email_count.text)
#     try:
#         price = driver.find_element(By.XPATH,'//*[@id="resultat_recherche"]/div[1]/span[2]/small/span/h4/b').text
#         print(price)
#     except:
#         price = 0
    
#     data.append(['Selection',email_count.text,price])
#     uncheck = driver.find_element(By.XPATH,'//*[@id="criteres_de_selections"]/div/div[2]/div[4]/span/span[1]/span/ul/li[1]').find_element(By.XPATH,'//*[@id="criteres_de_selections"]/div/div[2]/div[4]/span/span[1]/span/ul/li[1]/span').click()
# data = pd.DataFrame(data,columns=['Type','Email_count','Price'])
# data.to_csv('selection5.csv',index=False)



# for i in range(250,300):
#     print(i)
#     cat = driver.find_elements(By.CLASS_NAME,'select2-results__option')
#     select = cat[i].click()
    
#     time.sleep(3)
#     email_count = driver.find_element(By.XPATH,'//*[@id="resultat_recherche"]/div[1]/span[1]/h4')
#     print(email_count.text)
#     try:
#         price = driver.find_element(By.XPATH,'//*[@id="resultat_recherche"]/div[1]/span[2]/small/span/h4/b').text
#         print(price)
#     except:
#         price = 0
    
#     data.append(['Selection',email_count.text,price])
#     uncheck = driver.find_element(By.XPATH,'//*[@id="criteres_de_selections"]/div/div[2]/div[4]/span/span[1]/span/ul/li[1]').find_element(By.XPATH,'//*[@id="criteres_de_selections"]/div/div[2]/div[4]/span/span[1]/span/ul/li[1]/span').click()
# data = pd.DataFrame(data,columns=['Type','Email_count','Price'])
# data.to_csv('selection6.csv',index=False)



# for i in range(300,350):
#     print(i)
#     if i != 344:
#         cat = driver.find_elements(By.CLASS_NAME,'select2-results__option')
#         select = cat[i].click()
        
#         time.sleep(3)
    
#         try:
#             email_count = driver.find_element(By.XPATH,'//*[@id="resultat_recherche"]/div[1]/span[1]/h4')
#             print(email_count.text)
#             price = driver.find_element(By.XPATH,'//*[@id="resultat_recherche"]/div[1]/span[2]/small/span/h4/b').text
#             print(price)
#         except:
#             email = None
#             price = 0
        
#         data.append(['Selection',email_count.text,price])
#         uncheck = driver.find_element(By.XPATH,'//*[@id="criteres_de_selections"]/div/div[2]/div[4]/span/span[1]/span/ul/li[1]').find_element(By.XPATH,'//*[@id="criteres_de_selections"]/div/div[2]/div[4]/span/span[1]/span/ul/li[1]/span').click()

# data = pd.DataFrame(data,columns=['Type','Email_count','Price'])
# data.to_csv('selection7.csv',index=False)

# for i in range(350,400):
#     print(i)
#     cat = driver.find_elements(By.CLASS_NAME,'select2-results__option')
#     select = cat[i].click()
    
#     time.sleep(3)
#     email_count = driver.find_element(By.XPATH,'//*[@id="resultat_recherche"]/div[1]/span[1]/h4')
#     print(email_count.text)
#     try:
#         price = driver.find_element(By.XPATH,'//*[@id="resultat_recherche"]/div[1]/span[2]/small/span/h4/b').text
#         print(price)
#     except:
#         price = 0
    
#     data.append(['Selection',email_count.text,price])
#     uncheck = driver.find_element(By.XPATH,'//*[@id="criteres_de_selections"]/div/div[2]/div[4]/span/span[1]/span/ul/li[1]').find_element(By.XPATH,'//*[@id="criteres_de_selections"]/div/div[2]/div[4]/span/span[1]/span/ul/li[1]/span').click()
# data = pd.DataFrame(data,columns=['Type','Email_count','Price'])
# data.to_csv('selection8.csv',index=False)

# for i in range(400,450):
#     print(i)
#     cat = driver.find_elements(By.CLASS_NAME,'select2-results__option')
#     select = cat[i].click()
    
#     time.sleep(3)
#     email_count = driver.find_element(By.XPATH,'//*[@id="resultat_recherche"]/div[1]/span[1]/h4')
#     print(email_count.text)
#     try:
#         price = driver.find_element(By.XPATH,'//*[@id="resultat_recherche"]/div[1]/span[2]/small/span/h4/b').text
#         print(price)
#     except:
#         price = 0
    
#     data.append(['Selection',email_count.text,price])
#     uncheck = driver.find_element(By.XPATH,'//*[@id="criteres_de_selections"]/div/div[2]/div[4]/span/span[1]/span/ul/li[1]').find_element(By.XPATH,'//*[@id="criteres_de_selections"]/div/div[2]/div[4]/span/span[1]/span/ul/li[1]/span').click()
# data = pd.DataFrame(data,columns=['Type','Email_count','Price'])
# data.to_csv('selection9.csv',index=False)

# for i in range(450,500):
#     print(i)
#     cat = driver.find_elements(By.CLASS_NAME,'select2-results__option')
#     select = cat[i].click()
    
#     time.sleep(3)
#     email_count = driver.find_element(By.XPATH,'//*[@id="resultat_recherche"]/div[1]/span[1]/h4')
#     print(email_count.text)
#     try:
#         price = driver.find_element(By.XPATH,'//*[@id="resultat_recherche"]/div[1]/span[2]/small/span/h4/b').text
#         print(price)
#     except:
#         price = 0
    
#     data.append(['Selection',email_count.text,price])
#     uncheck = driver.find_element(By.XPATH,'//*[@id="criteres_de_selections"]/div/div[2]/div[4]/span/span[1]/span/ul/li[1]').find_element(By.XPATH,'//*[@id="criteres_de_selections"]/div/div[2]/div[4]/span/span[1]/span/ul/li[1]/span').click()
# data = pd.DataFrame(data,columns=['Type','Email_count','Price'])
# data.to_csv('selection10.csv',index=False)

# for i in range(500,550):
#     print(i)
#     if i != 527:
#         cat = driver.find_elements(By.CLASS_NAME,'select2-results__option')
#         select = cat[i].click()
        
#         time.sleep(3)
#         email_count = driver.find_element(By.XPATH,'//*[@id="resultat_recherche"]/div[1]/span[1]/h4')
#         print(email_count.text)
#         try:
#             price = driver.find_element(By.XPATH,'//*[@id="resultat_recherche"]/div[1]/span[2]/small/span/h4/b').text
#             print(price)
#         except:
#             price = 0
        
#         data.append(['Selection',email_count.text,price])
#         uncheck = driver.find_element(By.XPATH,'//*[@id="criteres_de_selections"]/div/div[2]/div[4]/span/span[1]/span/ul/li[1]').find_element(By.XPATH,'//*[@id="criteres_de_selections"]/div/div[2]/div[4]/span/span[1]/span/ul/li[1]/span').click()
# data = pd.DataFrame(data,columns=['Type','Email_count','Price'])
# data.to_csv('selection11.csv',index=False)

# for i in range(550,600):
#     print(i)
#     cat = driver.find_elements(By.CLASS_NAME,'select2-results__option')
#     select = cat[i].click()
    
#     time.sleep(3)
#     email_count = driver.find_element(By.XPATH,'//*[@id="resultat_recherche"]/div[1]/span[1]/h4')
#     print(email_count.text)
#     try:
#         price = driver.find_element(By.XPATH,'//*[@id="resultat_recherche"]/div[1]/span[2]/small/span/h4/b').text
#         print(price)
#     except:
#         price = 0
    
#     data.append(['Selection',email_count.text,price])
#     uncheck = driver.find_element(By.XPATH,'//*[@id="criteres_de_selections"]/div/div[2]/div[4]/span/span[1]/span/ul/li[1]').find_element(By.XPATH,'//*[@id="criteres_de_selections"]/div/div[2]/div[4]/span/span[1]/span/ul/li[1]/span').click()
# data = pd.DataFrame(data,columns=['Type','Email_count','Price'])
# data.to_csv('selection12.csv',index=False)

# for i in range(600,650):
#     print(i)
#     cat = driver.find_elements(By.CLASS_NAME,'select2-results__option')
#     select = cat[i].click()
    
#     time.sleep(3)
#     email_count = driver.find_element(By.XPATH,'//*[@id="resultat_recherche"]/div[1]/span[1]/h4')
#     print(email_count.text)
#     try:
#         price = driver.find_element(By.XPATH,'//*[@id="resultat_recherche"]/div[1]/span[2]/small/span/h4/b').text
#         print(price)
#     except:
#         price = 0
    
#     data.append(['Selection',email_count.text,price])
#     uncheck = driver.find_element(By.XPATH,'//*[@id="criteres_de_selections"]/div/div[2]/div[4]/span/span[1]/span/ul/li[1]').find_element(By.XPATH,'//*[@id="criteres_de_selections"]/div/div[2]/div[4]/span/span[1]/span/ul/li[1]/span').click()
# data = pd.DataFrame(data,columns=['Type','Email_count','Price'])
# data.to_csv('selection13.csv',index=False)

# for i in range(650,700):
#     print(i)
#     cat = driver.find_elements(By.CLASS_NAME,'select2-results__option')
#     select = cat[i].click()
    
#     time.sleep(3)
#     email_count = driver.find_element(By.XPATH,'//*[@id="resultat_recherche"]/div[1]/span[1]/h4')
#     print(email_count.text)
#     try:
#         price = driver.find_element(By.XPATH,'//*[@id="resultat_recherche"]/div[1]/span[2]/small/span/h4/b').text
#         print(price)
#     except:
#         price = 0
    
#     data.append(['Selection',email_count.text,price])
#     uncheck = driver.find_element(By.XPATH,'//*[@id="criteres_de_selections"]/div/div[2]/div[4]/span/span[1]/span/ul/li[1]').find_element(By.XPATH,'//*[@id="criteres_de_selections"]/div/div[2]/div[4]/span/span[1]/span/ul/li[1]/span').click()
# data = pd.DataFrame(data,columns=['Type','Email_count','Price'])
# data.to_csv('selection14.csv',index=False)


# for i in range(700,750):
#     print(i)
#     cat = driver.find_elements(By.CLASS_NAME,'select2-results__option')
#     select = cat[i].click()
    
#     time.sleep(3)
#     email_count = driver.find_element(By.XPATH,'//*[@id="resultat_recherche"]/div[1]/span[1]/h4')
#     print(email_count.text)
#     try:
#         price = driver.find_element(By.XPATH,'//*[@id="resultat_recherche"]/div[1]/span[2]/small/span/h4/b').text
#         print(price)
#     except:
#         price = 0
    
#     data.append(['Selection',email_count.text,price])
#     uncheck = driver.find_element(By.XPATH,'//*[@id="criteres_de_selections"]/div/div[2]/div[4]/span/span[1]/span/ul/li[1]').find_element(By.XPATH,'//*[@id="criteres_de_selections"]/div/div[2]/div[4]/span/span[1]/span/ul/li[1]/span').click()
# data = pd.DataFrame(data,columns=['Type','Email_count','Price'])
# data.to_csv('selection15.csv',index=False)

# for i in range(750,800):
#     print(i)
#     cat = driver.find_elements(By.CLASS_NAME,'select2-results__option')
#     select = cat[i].click()
    
#     time.sleep(3)
#     email_count = driver.find_element(By.XPATH,'//*[@id="resultat_recherche"]/div[1]/span[1]/h4')
#     print(email_count.text)
#     try:
#         price = driver.find_element(By.XPATH,'//*[@id="resultat_recherche"]/div[1]/span[2]/small/span/h4/b').text
#         print(price)
#     except:
#         price = 0
    
#     data.append(['Selection',email_count.text,price])
#     uncheck = driver.find_element(By.XPATH,'//*[@id="criteres_de_selections"]/div/div[2]/div[4]/span/span[1]/span/ul/li[1]').find_element(By.XPATH,'//*[@id="criteres_de_selections"]/div/div[2]/div[4]/span/span[1]/span/ul/li[1]/span').click()
# data = pd.DataFrame(data,columns=['Type','Email_count','Price'])
# data.to_csv('selection16.csv',index=False)

# for i in range(800,850):
#     print(i)
#     if i != 804:
#         cat = driver.find_elements(By.CLASS_NAME,'select2-results__option')
#         select = cat[i].click()
        
#         time.sleep(3)
#         email_count = driver.find_element(By.XPATH,'//*[@id="resultat_recherche"]/div[1]/span[1]/h4')
#         print(email_count.text)
#         try:
#             price = driver.find_element(By.XPATH,'//*[@id="resultat_recherche"]/div[1]/span[2]/small/span/h4/b').text
#             print(price)
#         except:
#             price = 0
        
#         data.append(['Selection',email_count.text,price])
#         uncheck = driver.find_element(By.XPATH,'//*[@id="criteres_de_selections"]/div/div[2]/div[4]/span/span[1]/span/ul/li[1]').find_element(By.XPATH,'//*[@id="criteres_de_selections"]/div/div[2]/div[4]/span/span[1]/span/ul/li[1]/span').click()
# data = pd.DataFrame(data,columns=['Type','Email_count','Price'])
# data.to_csv('selection17.csv',index=False)

# for i in range(850,900):
#     print(i)
#     cat = driver.find_elements(By.CLASS_NAME,'select2-results__option')
#     select = cat[i].click()
    
#     time.sleep(3)
#     email_count = driver.find_element(By.XPATH,'//*[@id="resultat_recherche"]/div[1]/span[1]/h4')
#     print(email_count.text)
#     try:
#         price = driver.find_element(By.XPATH,'//*[@id="resultat_recherche"]/div[1]/span[2]/small/span/h4/b').text
#         print(price)
#     except:
#         price = 0
    
#     data.append(['Selection',email_count.text,price])
#     uncheck = driver.find_element(By.XPATH,'//*[@id="criteres_de_selections"]/div/div[2]/div[4]/span/span[1]/span/ul/li[1]').find_element(By.XPATH,'//*[@id="criteres_de_selections"]/div/div[2]/div[4]/span/span[1]/span/ul/li[1]/span').click()
# data = pd.DataFrame(data,columns=['Type','Email_count','Price'])
# data.to_csv('selection18.csv',index=False)

# for i in range(900,950):
#     print(i)
#     cat = driver.find_elements(By.CLASS_NAME,'select2-results__option')
#     select = cat[i].click()
    
#     time.sleep(3)
#     email_count = driver.find_element(By.XPATH,'//*[@id="resultat_recherche"]/div[1]/span[1]/h4')
#     print(email_count.text)
#     try:
#         price = driver.find_element(By.XPATH,'//*[@id="resultat_recherche"]/div[1]/span[2]/small/span/h4/b').text
#         print(price)
#     except:
#         price = 0
    
#     data.append(['Selection',email_count.text,price])
#     uncheck = driver.find_element(By.XPATH,'//*[@id="criteres_de_selections"]/div/div[2]/div[4]/span/span[1]/span/ul/li[1]').find_element(By.XPATH,'//*[@id="criteres_de_selections"]/div/div[2]/div[4]/span/span[1]/span/ul/li[1]/span').click()
# data = pd.DataFrame(data,columns=['Type','Email_count','Price'])
# data.to_csv('selection19.csv',index=False)

# for i in range(950,1000):
#     print(i)
#     cat = driver.find_elements(By.CLASS_NAME,'select2-results__option')
#     select = cat[i].click()
    
#     time.sleep(3)
#     email_count = driver.find_element(By.XPATH,'//*[@id="resultat_recherche"]/div[1]/span[1]/h4')
#     print(email_count.text)
#     try:
#         price = driver.find_element(By.XPATH,'//*[@id="resultat_recherche"]/div[1]/span[2]/small/span/h4/b').text
#         print(price)
#     except:
#         price = 0
    
#     data.append(['Selection',email_count.text,price])
#     uncheck = driver.find_element(By.XPATH,'//*[@id="criteres_de_selections"]/div/div[2]/div[4]/span/span[1]/span/ul/li[1]').find_element(By.XPATH,'//*[@id="criteres_de_selections"]/div/div[2]/div[4]/span/span[1]/span/ul/li[1]/span').click()
# data = pd.DataFrame(data,columns=['Type','Email_count','Price'])
# data.to_csv('selection20.csv',index=False)

# for i in range(1002,1079):
#     print(i)
#     if i != 1024:
#         cat = driver.find_elements(By.CLASS_NAME,'select2-results__option')
#         select = cat[i].click()
        
#         time.sleep(3)
#         email_count = driver.find_element(By.XPATH,'//*[@id="resultat_recherche"]/div[1]/span[1]/h4')
#         print(email_count.text)
#         try:
#             price = driver.find_element(By.XPATH,'//*[@id="resultat_recherche"]/div[1]/span[2]/small/span/h4/b').text
#             print(price)
#         except:
#             price = 0
        
#         data.append(['Selection',email_count.text,price])
#         uncheck = driver.find_element(By.XPATH,'//*[@id="criteres_de_selections"]/div/div[2]/div[4]/span/span[1]/span/ul/li[1]').find_element(By.XPATH,'//*[@id="criteres_de_selections"]/div/div[2]/div[4]/span/span[1]/span/ul/li[1]/span').click()


# data = pd.DataFrame(data,columns=['Type','Email_count','Price'])
# data.to_csv('selection21.csv',index=False)



# cat = driver.find_elements(By.CLASS_NAME,'select2-results__option')
# data =[]
# for i in cat:
#     data.append(i.text)

# data = pd.DataFrame(data,columns=['Cat'])
# data.to_csv('activities.csv',index=False)
# driver.close()

lists = ['selection1.csv',
         'selection2.csv',
         'selection3.csv',
         'selection4.csv',
         'selection5.csv',
         'selection6.csv',
         'selection7.csv',
         'selection8.csv',
         'selection9.csv',
         'selection10.csv',
         'selection11.csv',
         'selection12.csv',
         'selection13.csv',
         'selection14.csv',
         'selection15.csv',
         'selection16.csv',
         'selection17.csv',
         'selection18.csv',
         'selection19.csv',
         'selection20.csv',
         'selection21.csv',
         ]
data =[]
for list in lists:
    x = pd.read_csv(list)
    data.append(x)

activity = pd.concat(data)
activities = pd.read_csv('activities.csv')['Cat'].values.tolist()

activity['Cat']=activities
activity['Type'] = activity['Type'].apply(lambda x: 'Activity')
activity.to_csv('Activity.csv',index = False)
print(activity.head(5))