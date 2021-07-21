from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select,WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe",options=options)
driver.maximize_window()

driver.get("http://demo.automationtesting.in/Register.html")


##Section One Working With the TextBoxes

text_box1 = driver.find_element_by_xpath("//*[@id='basicBootstrapForm']/div[1]/div[1]/input")
text_box2 = driver.find_element(By.XPATH,"//*[@id='basicBootstrapForm']/div[1]/div[2]/input")
text_box1.send_keys("Narasimha Rao")#typing the text inside the text box
text_box2.send_keys("Nandikonda")
time.sleep(2)
print("get the placeholder value: ",text_box1.get_attribute("placeholder")) # using get atatribute method to get the placeholder value
print("is text box enebled: ", text_box1.is_enabled())# checking the text box is enebled or not
text_box1.clear() # clearing the data from the text box
time.sleep(1)
text_box2.send_keys(Keys.CONTROL, 'a')# deleting the text from the textbox
text_box2.send_keys(Keys.DELETE)

#Section Two Working with Radio Button / Check Box
radio_button = driver.find_elements(By.NAME,"radiooptions")
print("No of Radio Buttons : ",len(radio_button))# counting the no of elements in the radio button group

for value in radio_button:
    print("value of the radiobutton",value.get_attribute("value"))#values of the radio buttons using getattribute method
male_radio_button = driver.find_element_by_xpath("//*[@id='basicBootstrapForm']/div[5]/div/label[1]/input")
print("is radio button enabled :", male_radio_button.is_enabled())#checking wether the radiobutton is enebled or not
print("Is radio button selected",male_radio_button.is_selected())#checking wether the radiobutton is selected or not
male_radio_button.click()
time.sleep(1)
print("Is radio button selected",male_radio_button.is_selected())#checking wether the radiobutton is selected or not
check_box = driver.find_element_by_xpath("//*[@id='basicBootstrapForm']/div[6]/div/div[1]/label")
print("check box label text: ", check_box.text)# lebel text of the check button

#Working with the Dropdown/List Box/Combo Box

drop_down = driver.find_element_by_xpath("//*[@id='basicBootstrapForm']/div[11]/div[2]/select")
drp = Select(drop_down)
print(len(drp.options))# no of options available in the drop down
all_options = drp.options
for option in all_options:
    print("first selected option :", option.text)# text of the all drop down options
drp.select_by_value("January")# selecting the option by value
time.sleep(1)
drp.select_by_index(2)# selecting the option by index
time.sleep(1)
drp.select_by_visible_text("March")# selecting the option by visible text


#Working with the web links

links = driver.find_elements(By.TAG_NAME,"a")
print("No of links in the web page :",len(links))# counting the all links available in the web page
#printing all the links available in the web page
for link in links:
    if link.get_attribute('href') is not None:
        print(link.get_attribute('href'))
driver.find_element(By.PARTIAL_LINK_TEXT,"Reg").click()#clicking the link by partial link text
driver.find_element(By.LINK_TEXT,"Register").click()# clicking the text by link text

wait = WebDriverWait(driver,20)
image_link = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='header']/div/div/div/div[1]/a/img")))
image_link.click()

time.sleep(5)
driver.quit()