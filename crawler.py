# Imports libraries
from asyncio.streams import FlowControlMixin
from selenium import webdriver
import time

# Defines the competition, as their name on the link
    # Link names are to be captured manually and input below as strings
competitors = ['twitter', 'facebookapp', 'google', 'apple', 'samsung', 'microsoft', 'lendas_automotivas_yt']

driver = webdriver.Chrome()
# Sets the wait time before wich any element will have appeared and be ready to interact with
driver.implicitly_wait(5) # seconds

# 1) First, logs in so pages are displayed correctly
driver.get('https://www.instagram.com/')

user = 'racing_legends_yt'
password = 'J>F<s_i3.4v>rUY'

# Inputs username and password
text_area = driver.find_element_by_name('username')
text_area.send_keys(user)
text_area = driver.find_element_by_name('password')
text_area.send_keys(password)

# Submits
driver.find_element_by_xpath('//div/div[3]').click()

# Waits for full page processing and load complete
time.sleep(5)

# 2) Now for the actual data collection 
# Cycles through each competitor's instagram page
for company in competitors:
    driver.get('https://www.instagram.com/'+company)
    # Grabs followers and stores the info
    followers = driver.find_element_by_css_selector('.Y8-fY:nth-child(2) .g47SY ').text
    
    # 3) Data treatment
    if 'milhões' in followers:
        string = followers[:-7]
        number = string.replace(',','.')
        print(company+' - '+number+'M followers')
    elif 'mil' in followers:
        string = followers[:-3]
        number = string.replace(',','.')
        print(company+' - '+number+'K followers')
    else:
        print(company+' - '+number+' followers')

driver.quit()