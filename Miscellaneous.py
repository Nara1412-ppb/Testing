from selenium import webdriver
from selenium.webdriver import ActionChains
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe",options=options)
driver.maximize_window()




#Mouse Hover action
'''driver.get("https://www.orangehrm.com/")
company = driver.find_element_by_xpath("//*[@id='header-navbar']/ul[1]/li[4]/a")
career = driver.find_element_by_xpath("//*[@id='header-navbar']/ul[1]/li[4]/ul/div/div/div/p[5]/a")
actions = ActionChains(driver)
actions.move_to_element(company).move_to_element(career).click().perform()'''



#Double click action
'''driver.get("http://testautomationpractice.blogspot.com/")
dblclk = driver.find_element_by_xpath("//*[@id='HTML10']/div/button")
actions = ActionChains(driver)
actions.double_click(dblclk).perform()'''

#right click button
'''driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
button = driver.find_element_by_xpath("/html/body/div/section/div/div/div/p/span")
actions = ActionChains(driver)
actions.context_click(button).perform()'''


#Drag And Drop 
'''driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
source_element = driver.find_element_by_xpath("//*[@id='box7']")
target_element =driver.find_element_by_xpath("//*[@id='box106']")
actions = ActionChains(driver)
actions.drag_and_drop(source_element,target_element).perform()
'''
#file upload
driver.get("http://testautomationpractice.blogspot.com/")
driver.switch_to.frame(0)

driver.find_element_by_id("RESULT_FileUpload-10").send_keys("D://My_pics/_MG_1922.JPG")


time.sleep(2)
driver.quit()

print("done............!")
