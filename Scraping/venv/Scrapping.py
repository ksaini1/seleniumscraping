from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
from lxml import html
options = webdriver.ChromeOptions()
options.headless = True
# options.add_argument()
options.add_argument("--incognito")
options.add_argument("no-sandbox");
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.implicitly_wait(10)
driver.get('https://idbop.mylicense.com/verification/')
driver.implicitly_wait(10)
inp = driver.find_element_by_id("t_web_lookup__last_name")
inp.send_keys('L')
# id="t_web_lookup__last_name"
accept_button = driver.find_element_by_id("sch_button")
accept_button.click()
# print(driver.title)
# driver.get_screenshot_as_file("filename.png")
# df = pd.DataFrame(columns=["First_Name", "Middle_Name", "Last_Name", "License#", "Type", "Status"])
# df.to_csv("Lastname.csv", index= False)
# gets the table
#Flip through all of the records and save them
# li = []
# a = 3
# for tr in driver.find_elements_by_xpath('//*[@id="datagrid_results"]/tbody//tr'):
#     tds = tr.find_elements_by_tag_name('td')
#     li.append([td.text for td in tds])
#     det = driver.find_element_by_id("datagrid_results__ctl"+str(a)+"_name")
#     det.click()
#     print(driver.title)
#     driver.close()
#     a+=1
# # print(li)
# fin = []
# for i in range(len(li)):
#     if len(li[i])>2:
#         fin.append(li[i])
# print(fin)
a = 3
# OPENING EACH SEARCH RECORDS
while a < 43:
    det = driver.find_element_by_id("datagrid_results__ctl" + str(a) + "_name").get_attribute("href")
    new = driver.get(det)
    driver.implicitly_wait(10)
    driver.get_screenshot_as_file("filename.png")

    # fname = driver.find_element_by_id("_ctl27__ctl1_first_name")
    fname = driver.find_element_by_xpath("//*[contains(@id, '_first_name')]")
    middle= driver.find_element_by_xpath("//*[contains(@id, '_m_name')]")
    lname = driver.find_element_by_xpath("//*[contains(@id, 'last_name')]")
    lic = driver.find_element_by_xpath("//*[contains(@id, 'license_no')]")
    lictype = driver.find_element_by_xpath("//*[contains(@id, '_license_type')]")
    status = driver.find_element_by_xpath("//*[contains(@id, '_status') and @maxlength='50']")
    issuedate = driver.find_element_by_xpath("//*[contains(@id, '_issue_date') and @maxlength='50']")
    expdate = driver.find_element_by_xpath("//*[contains(@id, '_expiry') and @maxlength='50']")

    print(fname.text)
    print(middle.text)
    print(lname.text)
    print(lic.text)
    print(lictype.text)
    print(status.text)
    print(issuedate.text)
    print(expdate.text)
    print(" ")
    del_but = driver.find_element_by_id("btn_close")
    del_but.click()
    # OPEN THE ORIGINAL PAGE AGAIN
    driver.get('https://idbop.mylicense.com/verification/')
    driver.implicitly_wait(10)
    inp = driver.find_element_by_id("t_web_lookup__last_name")
    inp.send_keys('L')
    accept_button = driver.find_element_by_id("sch_button")
    accept_button.click()
    driver.implicitly_wait(10)
    a+=1


# driver.close()