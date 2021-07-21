from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe",options=options)
driver.maximize_window()
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

#scr = driver.find_element_by_xpath("//*[@id='content']/div[2]/div[2]/table[1]/tbody/tr[86]/td[1]/img")
#driver.execute_script("arguments[0].scrollIntoView();",scr)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
print("done")
