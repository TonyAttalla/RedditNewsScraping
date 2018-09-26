from tkinter import *
import requests
import re
import openpyxl
#writing to excel sheet eventually^
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time
import os
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui
import selenium.webdriver.support.expected_conditions as EC
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')  
#options.add_argument("--headless")  
options.add_argument('--ignore-ssl-errors')
dir_path = os.path.dirname(os.path.realpath(__file__))
chromedriver = dir_path + "/chromedriver"
os.environ["webdriver.chrome.driver"]= chromedriver
def grab_news():
	news = []
	news2 = []
	driver = webdriver.Chrome(chrome_options=options,executable_path=chromedriver)

	driver.get("https://www.old.reddit.com/r/news/")

	a = driver.find_elements_by_xpath("//a[@data-event-action='title']")
	#remove the ad
	a= a[1:]
	for element in a:
		
		print(element.text)
grab_news()