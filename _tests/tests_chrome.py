from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selc import take_screenshot,convert_64_img

options = Options()
#options.headless = True
driver = webdriver.Chrome(options=options)

def test_1():
    driver.get('https://www.brendangregg.com/')
    base_64 = take_screenshot(driver=driver)
    image_file_path = convert_64_img(base_64_str=base_64) 
    print(image_file_path)

def test_2():
    driver.get('https://stackoverflow.com/questions/67147412/take-entire-page-screenshot-with-selenium-python')
    base_64 = take_screenshot(driver=driver)
    image_file_path = convert_64_img(base_64_str=base_64) 
    print(image_file_path)

