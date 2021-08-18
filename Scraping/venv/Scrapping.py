from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
from lxml import html
from selenium.common.exceptions import NoSuchElementException
import csv


options = webdriver.ChromeOptions()
options.headless = True
# options.add_argument()
options.add_argument("--incognito")
options.add_argument("no-sandbox")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.implicitly_wait(10)
driver.get('https://idbop.mylicense.com/verification/')
driver.implicitly_wait(10)
inp = driver.find_element_by_id("t_web_lookup__last_name")
inp.send_keys('L')
accept_button = driver.find_element_by_id("sch_button")
accept_button.click()
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
with open("a.csv", 'w') as csvfile:
    fieldnames = ['First Name', 'Middle Name', 'Last Name', 'License Type', 'License Number', 'Status', 'Issue Date', 'Expiry Date']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    while a < 43:
        det = driver.find_element_by_id("datagrid_results__ctl" + str(a) + "_name").get_attribute("href")
        new = driver.get(det)
        driver.implicitly_wait(10)
        driver.get_screenshot_as_file("filename.png")

    # fname = driver.find_element_by_id("_ctl27__ctl1_first_name")
    # fname = driver.find_element(By.XPATH("//*[contains(@id, '_first_name')]"))
    # fname1 =driver.find_element(By.XPATH("//*[contains(@id, '_first_name')]"))
        try:
            fname = driver.find_element_by_xpath("//*[contains(@id, '_first_name')]")
            middle= driver.find_element_by_xpath("//*[contains(@id, '_m_name')]")
            lname = driver.find_element_by_xpath("//*[contains(@id, 'last_name')]")
            lic = driver.find_element_by_xpath("//*[contains(@id, 'license_no')]")
            lictype = driver.find_element_by_xpath("//*[contains(@id, '_license_type')]")
            status = driver.find_element_by_xpath("//*[contains(@id, '_status') and @maxlength='50']")
            issuedate = driver.find_element_by_xpath("//*[contains(@id, '_issue_date') and @maxlength='50']")
            expdate = driver.find_element_by_xpath("//*[contains(@id, '_expiry') and @maxlength='50']")

    # print(fname1)
            writer.writerow({'First Name': fname.text, 'Middle Name': middle.text, 'Last Name': lname.text, 'License Type': lictype.text, 'License Number': lic.text, 'Status':status.text, 'Issue Date': issuedate.text, 'Expiry Date': expdate.text})
            print(fname.text)
            print(" ")
            del_but = driver.find_element_by_id("btn_close")
            del_but.click()
        except NoSuchElementException:
            pass
    # OPEN THE ORIGINAL PAGE AGAIN
        driver.get('https://idbop.mylicense.com/verification/')
        driver.implicitly_wait(10)
        inp = driver.find_element_by_id("t_web_lookup__last_name")
        inp.send_keys('L')
        accept_button = driver.find_element_by_id("sch_button")
        accept_button.click()
    # driver.implicitly_wait(10)
        a+=1


    b = 2
    while b < 3:
        a=3
        while a<43:
            accept_button = driver.find_element_by_xpath(".//a[contains(text(), '" + str(b) + "')]")
            accept_button.click()
            driver.get_screenshot_as_file("filename.png")
            det = driver.find_element_by_id("datagrid_results__ctl" + str(a) + "_name").get_attribute("href")
            new = driver.get(det)
            driver.implicitly_wait(10)
            driver.get_screenshot_as_file("filename.png")

    # fname = driver.find_element_by_id("_ctl27__ctl1_first_name")
    # fname = driver.find_element(By.XPATH("//*[contains(@id, '_first_name')]"))
    # fname1 =driver.find_element(By.XPATH("//*[contains(@id, '_first_name')]"))
            try:
                fname = driver.find_element_by_xpath("//*[contains(@id, '_first_name')]")
                middle = driver.find_element_by_xpath("//*[contains(@id, '_m_name')]")
                lname = driver.find_element_by_xpath("//*[contains(@id, 'last_name')]")
                lic = driver.find_element_by_xpath("//*[contains(@id, 'license_no')]")
                lictype = driver.find_element_by_xpath("//*[contains(@id, '_license_type')]")
                status = driver.find_element_by_xpath("//*[contains(@id, '_status') and @maxlength='50']")
                issuedate = driver.find_element_by_xpath("//*[contains(@id, '_issue_date') and @maxlength='50']")
                expdate = driver.find_element_by_xpath("//*[contains(@id, '_expiry') and @maxlength='50']")

        # print(fname1)
                writer.writerow({'First Name': fname.text, 'Middle Name': middle.text, 'Last Name': lname.text,
                                'License Type': lictype.text, 'License Number': lic.text, 'Status': status.text,
                                'Issue Date': issuedate.text, 'Expiry Date': expdate.text})
                print(fname.text)
                print(" ")
                del_but = driver.find_element_by_id("btn_close")
                del_but.click()
            except NoSuchElementException:
                pass
    # OPEN THE ORIGINAL PAGE AGAIN
            driver.get('https://idbop.mylicense.com/verification/')
            driver.implicitly_wait(10)
            inp = driver.find_element_by_id("t_web_lookup__last_name")
            inp.send_keys('L')
            accept_button = driver.find_element_by_id("sch_button")
            accept_button.click()
            a+=1
        b+=1
