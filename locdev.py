from selenium import webdriver
from selc.selc import take_screenshot,convert_64

def load_page():
    driver = webdriver.Chrome()
    driver.get('https://www.brendangregg.com/')
    base_64 = take_screenshot(driver=driver)
    image_file = convert_64(base_64_str=base_64) 

if __name__ == '__main__':
    load_page()