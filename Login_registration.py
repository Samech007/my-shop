# 2 задание

# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# my_account = driver.find_element_by_link_text("My Account").click()
# email = driver.find_element_by_xpath("//input[@id='reg_email']")
# email.send_keys("ionov.nikita@ro.ru")
# password = driver.find_element_by_xpath("//input[@id='reg_password']")
# password.send_keys("RomeoSaintP2023!@&")
# register = driver.find_element_by_xpath("//input[@name='register']").click()
# driver.quit()

# 3 задание

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# my_account = driver.find_element_by_link_text("My Account").click()
# email = driver.find_element_by_id("username")
# email.send_keys("ionov.nikita@ro.ru")
# password = driver.find_element_by_id("password")
# password.send_keys("RomeoSaintP2023!@&")
# login_btn = driver.find_element_by_name("login").click()
# logout_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".woocommerce-MyAccount-navigation-link.woocommerce-MyAccount-navigation-link--customer-logout")))
# if logout_element.text == "Logout":
#     print("Элемент 'Logout' найден:", logout_element.text)
# else:
#     print("Элемент 'Logout' не найден. Фактический текст:", logout_element.text)
# driver.quit()


