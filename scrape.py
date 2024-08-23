from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import csv

driver=webdriver.Firefox()
driver.get("https://www.pesuacademy.com/Academy/")

sleep(15)

srn="PES1"

knowyourclass=driver.find_element(By.ID, "knowClsSection") #find Know Your Class and Section button
knowyourclass.click()

results=[]

for srnunique in range(202400001, 202401000):
    srninput=srn+str(srnunique)


    srnin=driver.find_element(By.ID, "knowClsSectionModalLoginId")
    srnin.send_keys(srninput)

    searchbutton=driver.find_element(By.ID, "knowClsSectionModalSearch") #find search button
    searchbutton.click()

    sleep(1)

    try:
        tbody = driver.find_element(By.ID, "knowClsSectionModalTableDate")
        trows = tbody.find_elements(By.TAG_NAME, "tr")
        
        for row in trows:
            tags = row.find_elements(By.TAG_NAME, "td")
            if tags:
                prn = tags[0].text.strip()
                name = tags[2].text.strip()
                branch = tags[7].text.strip()
            
            results.append([srninput, name, branch])
    except Exception as exc:
        print("No Data for ", srninput)

    srnin.clear()
    
    sleep(1)

with open('pes.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["SRN", "Name", "Branch"]) 
    writer.writerows(results)

driver.quit()


