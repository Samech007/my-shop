# 4 задание

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
# shop = driver.find_element_by_link_text("Shop").click()
# driver.execute_script("window.scrollBy(0, 200);")
# book = driver.find_element_by_css_selector("img[title='Mastering HTML5 Forms']").click()
# html_5_forms = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".product_title.entry-title")))
# if html_5_forms == html_5_forms :
#     print("Заголовок книги HTML 5 forms")
# else:
#     print("Заголовок книги не HTML 5 forms")
# driver.quit()

# 5 задание

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
# shop = driver.find_element_by_link_text("Shop").click()
# html = driver.find_element_by_link_text("HTML").click()
# books = driver.find_elements_by_css_selector(".type-product")
# if len(books) == 3:
#     print("В разделе 3 книги")
# else:
#     print("Ошибка. В разделе другое количество книг")
# driver.quit()

# 6 задача

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
# shop = driver.find_element_by_link_text("Shop").click()
# items_selector = driver.find_element_by_name("orderby")
# items_selector_default = items_selector.get_attribute("value")
# if items_selector_default == "menu_order" :
#     print("Вариант сортировки по умолчанию выбран")
# else:
#     print("Вариант сортировки по умолчанию не выбран")

# 7 задание


# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# my_account = driver.find_element_by_link_text("My Account").click()
# email = driver.find_element_by_id("username")
# email.send_keys("ionov.nikita@ro.ru")
# password = driver.find_element_by_id("password")
# password.send_keys("RomeoSaintP2023!@&")
# login_btn = driver.find_element_by_name("login").click()
# shop = driver.find_element_by_link_text("Shop").click()
# android_quick_star_book = driver.find_element_by_css_selector(".post-169").click()
# book_old_price = driver.find_element_by_css_selector(".price > del > span")
# book_old_price_text = book_old_price.text
# book_new_price = driver.find_element_by_css_selector(".price > ins > span")
# book_new_price_text = book_new_price.text
# assert book_old_price_text == "₹600.00"
# assert book_new_price_text == "₹450.00"
# book_cover = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".images"))).click()
# book_close = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close"))).click()
# driver.quit()

# 8 задание


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
my_account = driver.find_element_by_link_text("My Account").click()
email = driver.find_element_by_id("username")
email.send_keys("ionov.nikita@ro.ru")
password = driver.find_element_by_id("password")
password.send_keys("RomeoSaintP2023!@&")
login_btn = driver.find_element_by_name("login").click()
shop = driver.find_element_by_link_text("Shop").click()
add_to_basket = driver.find_element_by_xpath("//a[@href='/shop/?add-to-cart=182']")
add_to_basket.click()
basket_1 = driver.find_element_by_css_selector(".cartcontents")
basket_1_text = basket_1.text
price = driver.find_element_by_css_selector(".amount")
price_text = price.text
assert basket_1_text == "1 Item"
assert price_text == "₹180.00"
basket = driver.find_element_by_id("wpmenucartli").click()


