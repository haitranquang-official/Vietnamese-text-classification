from selenium import webdriver
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome(executable_path="chromedriver.exe")

browser.get("https://vnexpress.net/the-gioi")

txtUser = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input")
txtUser.send_keys("20194857")
# txtPass = browser.find_element_by_id("ctl00_ctl00_contentPane_MainPanel_MainContent_tbPassword_I_CLND")
# wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='ctl00_ctl00_contentPane_MainPanel_MainContent_tbPassword_I_CLND']"))).send_keys("abc@123%$")
txtPass = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/input")
# print("Element is visible? " + str(txtPass.is_displayed()))
txtPass.send_keys("1111111")

sleep(5)

browser.close()