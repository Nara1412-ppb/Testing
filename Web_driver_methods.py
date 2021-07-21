from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe",options=options)
driver.maximize_window()
#get method used to open the webpage
driver.get("https://jalatechnologies.com/")

# current_url method to capture the url of the page
print("Url of the web page is : ",driver.current_url)

#get url method to capture the title of the page
print("title of the web page is : ",driver.title)


source = driver.page_source
#get source code of the page using the source_code
#print("Source code of the web page is at: ", source)



#Find Element  by xpath attribute
driver.find_element(By.XPATH,"//*[@id='banner']/div/div/div/div/div[2]/a[1]").click()



driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
elements = driver.find_elements(By.CLASS_NAME,"text_field")
print(len(elements))





driver.get("http://demo.automationtesting.in/Register.html")
text_box = driver.find_element_by_xpath('//*[@id="basicBootstrapForm"]/div[1]/div[1]/input')
print("text box enebled: ", text_box.is_enabled())
print("text box displayed: ", text_box.is_displayed())
print("tag name: ", text_box.tag_name)
text_box.send_keys('Narasimha Rao')

'''button = driver.find_elements_by_css_selector("input[value=Male]")
print("Is Radio button selected: ", button.is_selected())'''

driver.get("http://demo.automationtesting.in/Windows.html")
driver.back()
driver.forward()
driver.refresh()

driver.get("http://demo.automationtesting.in/Windows.html")
text = driver.find_element_by_xpath("//*[@id='header']/nav/div/div[2]/ul/li[2]/a")
print('.text method:  ',text.text)
print(text.get_attribute('href'))
click_box = driver.find_element_by_xpath("//*[@id='Tabbed']/a/button")
click_box.click()
print(driver.current_window_handle)

handles = driver.window_handles
for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)


time.sleep(4)
driver.close()
driver.quit()