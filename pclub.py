from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd 
import time

driver = webdriver.Chrome(executable_path="F:\chromedriver_win32\chromedriver.exe")
driver.implicitly_wait(30)
driver.maximize_window()
driver.get("https://summerofcode.withgoogle.com/programs/2022/organizations")
fields = driver.find_elements(by= By.XPATH, value= "//mat-chip")
types=[]
names=[]
topics= []
technologies=[]
 
for field in fields:
    if(field.text == "All"): 
        continue
    driver.execute_script("window.scrollTo(0, 0)")
    time.sleep(3)
    field.click()
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, 900)")
    time.sleep(3)



    driver.find_element(by=By.XPATH, value = "//div[@class='mat-form-field-flex ng-tns-c87-2']").click()
    numbers= driver.find_element(by= By.XPATH, value = "//mat-option[@id='mat-option-3']").click()
    orgs = driver.find_elements(by= By.XPATH, value = "//div[@class='name']")
    links=driver.find_elements(by=By.XPATH, value = "//a[@class='content']")

    i = 0
    h=850

    for org in orgs:
        names.append(org.text)
        if (i%3==0) and (i!=0) :
            h+=290 
            driver.execute_script("window.scrollTo(0, "+str(h)+")")
            time.sleep(0.5)

        if (i==66):
            h-=150
            driver.execute_script("window.scrollTo(0, "+str(h)+")")
            time.sleep(1)

        types.append(field.text)
        
        
        links[i].click()
        window2=driver.window_handles[1]
        window1=driver.window_handles[0]
        driver.switch_to.window(window2)
        TechContent = driver.find_element(by= By.XPATH, value = "//div[@class='tech__content']")
        topic = driver.find_element(by= By.XPATH, value = "//div[@class='topics__content']")
        topics.append(topic.text)
        technologies.append(TechContent.text)
        driver.close()
        driver.switch_to.window(window1)
        i+=1
time.sleep(5)
driver.close()

print(len(types))
print(len(names))
   
df = pd.DataFrame({'Field': types, 'Name of organisation':names, 'Tech Stack':technologies, 'Topics':topics})
df.to_csv('GSOC.csv', index=False)
print(df)

