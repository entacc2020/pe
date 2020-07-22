from selenium import webdriver
import constants  
from os import path
import time
driver = webdriver.Chrome()

f = open('output.txt','w')

def browse(sector):   
    driver.get(sector)
    time.sleep(2)
    sector_name = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[2]/div/div[1]/div/h6').text
    sector_pe = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[2]/div/div[1]/div/a/div').text
    sector_value = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/span[1]').text
    print(sector_name,":" ,sector_pe,"Index :",sector_value, file= f)
    print(sector_name,":" ,sector_pe,"Index :",sector_value)


browse(constants.NIFTY50LINK)
browse(constants.NIFTYNEXT50)
browse(constants.NIFTYBANKLINK)
browse(constants.NIFTYITLINK)



#inputfile = 'title.py'
# file1 = open(inputfile, 'r')
# Lines = file1.readlines()
# for line in Lines:
#     print(line)


driver.close()

 

