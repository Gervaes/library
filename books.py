import time
from selenium import webdriver

###### Renewing books from library ######
#Make sure you have selenium installed and geckodriver in your PATH /usr/bin or /usr/local/bin
#http://selenium-python.readthedocs.io/installation.html
#~$ python3 books.py

CPF = 
Password = 
URL = 'http://www.athena.biblioteca.unesp.br/'
Sleep = 3

#Open browser and access URL
firefox	= webdriver.Firefox()
firefox.get(URL)
time.sleep(Sleep)

#Access login page
temp = firefox.find_elements_by_xpath('html/body/table[1]/tbody/tr[2]/td[2]/a')
temp[0].click()
time.sleep(Sleep)

#Form and login
firefox.find_element_by_id('pat_id').send_keys(CPF)
firefox.find_element_by_id('pat_password').send_keys(Password)
temp = firefox.find_elements_by_xpath('html/body/form/table/tbody/tr[3]/td/input')
temp[0].click()
time.sleep(Sleep)

#Acess books page
temp = firefox.find_elements_by_xpath('html/body/table[2]/tbody/tr/td[1]/table[1]/tbody/tr[1]/td[2]/a')
temp[0].click()
time.sleep(Sleep)

#Renewing all books
temp = firefox.find_elements_by_xpath('html/body/table[2]/tbody/tr/td[12]/a')
temp[0].click()
time.sleep(10)

#Close browser
firefox.close()
