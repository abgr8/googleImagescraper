from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from chromedriver_py import binary_path
import os
import urllib.request
import os
print("made for abbas by abbas")
standard_input = "n"
# clear the terminal on Windows
os.system('cls')

#set chromodriver.exe path
Wants = True
ListofWantedthings = []
while Wants:
    
    Wanted = input("whadda u want:")
    ListofWantedthings.append(Wanted)
    if (input("more y/n:")=="n"):
        print(Wanted + " has been added.")
        Wants = False
   
    
    
options = webdriver.ChromeOptions()
options.binary_location = "C:\Program Files\BraveSoftware\Brave-Browser\Application\\brave.exe"
# brave path: C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe
driver = webdriver.Chrome(executable_path=binary_path, options=options)
# driver.set_page_load_timeout(3)
driver.implicitly_wait(0.1)
#launch URL
#identify search box
#enter search text

for thing in ListofWantedthings:
 driver.get("https://www.google.com/")
 m = driver.find_element("name", "q")
 m.send_keys(thing)
 m.send_keys(Keys.ENTER)
 #  images_tab = driver.find_element_by_xpath("//a[contains(@href,'tbm=isch')]")
 images_tab = driver.find_element("xpath", "//a[contains(@href,'tbm=isch')]")
 images_tab.click()

 # find and click on the topmost image
 #  top_image = driver.find_element_by_xpath("//img[@class='rg_i']")
 top_image = driver.find_element("xpath","/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div[1]/a[1]/div[1]/img")
 top_image.click()
 
 # get the source URL of the image
 image_url = driver.find_element("xpath","/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div[1]/a[1]/div[1]/img")
 image_url = image_url.get_attribute("src")

 # save the image to a file
 urllib.request.urlretrieve(image_url, f"C:/Users/abbas/Code/sel/image/{thing}.png")
 os.system('cls')
 
 #  time.sleep(3)
