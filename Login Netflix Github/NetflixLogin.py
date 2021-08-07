from selenium import webdriver
import time
import pyautogui

emailNetflix = input("Email: ")
senhaNetflix = input("Senha: ")
login = webdriver.Chrome()
login.get("https://www.netflix.com/login")
time.sleep(2)
login.find_element_by_xpath('//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/form/div[1]/div[1]/div/label/label').click()
time.sleep(2)
pyautogui.write(f'f{emailNetflix}')
time.sleep(2)
login.find_element_by_xpath('//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/form/div[2]/div/div/label/label').click()
pyautogui.write(f'{senhaNetflix}')
login.find_element_by_xpath('//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/form/button').click()

