from selenium import webdriver
from selc.selc import take_screenshot,convert_64_img

def load_page():
    driver = webdriver.Chrome()
    driver.get('https://www.brendangregg.com/')
    base_64 = take_screenshot(driver=driver)
    image_file_path = convert_64_img(base_64_str=base_64) 
    print(image_file_path)
    
if __name__ == '__main__':
    load_page()