from selenium import webdriver
from selenium.webdriver.common.keys import Keys

desktop_chrome_driver = "C:/Users/user/PycharmProjects/chromedriver.exe"
driver = webdriver.Chrome(executable_path=desktop_chrome_driver)
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
#
# article_count = driver.find_element_by_css_selector("#articlecount a")
# # print(article_count.text)
#
# click_all_portal = driver.find_element_by_link_text("All portals")
# # click_all_portal.click()
#
# search = driver.find_element_by_name("search")
# # search.send_keys("Python")
# # search.send_keys(Keys.ENTER)
#
#
# driver.quit()


#-----Testing 2------#
driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element_by_name("fName")
first_name.send_keys("Ken")
last_name = driver.find_element_by_name("lName")
last_name.send_keys("Wong")
email = driver.find_element_by_name("email")
email.send_keys("kamik@hotmail.com")

submit_btn = driver.find_element_by_class_name("btn")
submit_btn.click()

