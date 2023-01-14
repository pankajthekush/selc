# selc
Take full page screenshot from selenium driver

Take screenshot of the given page and  return base64 string png image, this app does not add/remove/delete/hide elements or even resizes the size of your window, you are responsible to maximize/resize hide elements, I have to keep it very simple.


```python
from selenium import webdriver
from selc.selc import take_screenshot,convert_64_img

def load_page():
    driver = webdriver.Chrome()
    driver.get('https://www.brendangregg.com/')
    base_64 = take_screenshot(driver=driver)
    image_file_path = convert_64_img(base_64_str=base_64) 
    print(image_file_path)
```
output
```sh
(env) pankaj:selc$ python locdev.py 
/tmp/tmp6c2ix031.png
(env) pankaj:selc$ 
```
[![Run time sample](example.gif)]
