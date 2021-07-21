import time
from selenium import webdriver



options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe",options=options)
driver.maximize_window()

driver.get("http://demo.automationtesting.in/Alerts.html")
driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/ul/li[2]/a").click()#Confirmation Alert with Ok and Cancel buttons
alert = driver.find_element_by_xpath("//*[@id='CancelTab']/button")
alert.click()
ok_alart = driver.switch_to.alert
print("ok alert :",ok_alart.text)
time.sleep(1)
ok_alart.accept()#Clicking OK button of the alert using accept()
time.sleep(2)
alert.click()
cancel_alert = driver.switch_to.alert
print("cancel alert message :",cancel_alert.text)
time.sleep(1)
cancel_alert.dismiss()#Clicking Cancel button of the alert using dismiss()

time.sleep(2)
#promptiong the text box alert and sending text to alert box.
driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/ul/li[3]/a").click()#Confirmation Alert with Ok and Cancel buttons
driver.find_element_by_xpath("//*[@id='Textbox']/button").click()
msg_alert = driver.switch_to.alert
msg_alert.send_keys("Narasimha Rao")
time.sleep(1)
msg_alert.accept()


driver.get("http://demo.automationtesting.in/Windows.html")
print("Current window handle :",driver.current_window_handle)# handling the current window using current window handle
driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()
handles = driver.window_handles  #handling the multipl windows using windowhndles
for handle in handles:
    time.sleep(2)
    driver.switch_to.window(handle) # swiching the window using switch to window
    print(driver.title)

#switching the frames using switchto.frame
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
driver.switch_to.frame("packageListFrame")
driver.find_element_by_link_text("org.openqa.selenium").click()
time.sleep(2)
driver.switch_to.default_content()
driver.switch_to.frame("packageFrame")
driver.find_element_by_link_text("WebDriver")
time.sleep(2)
driver.switch_to.default_content()
driver.switch_to.frame("classFrame")
driver.find_element_by_xpath("/html/body/header/nav/div[1]/div[1]/ul/li[6]/a").click()
driver.quit()