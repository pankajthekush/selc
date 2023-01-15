
import logging, base64, io,tempfile
from PIL import Image
import time
"""
    take screenshot of full page , user have to ensure the 
    > elements are visible/deleted
    > page is fully loaded
    selc will assume everything is ready and will take screenshot
"""

logger = logging.getLogger('selc')
logger.setLevel(logging.DEBUG)


class ScPage():
    """
        take screenshot 
    """
    def __init__(self,driver,max_pages=30) -> None:
        self._max_page = max_pages
        self._driver = driver
        self._all_screens = list()
        self._inner_height = 0
        self.total_height = driver.execute_script("return document.body.parentNode.scrollHeight")
        if self._max_page > 30:
            logger.warn('max pages count is too big %s',self._max_page)

        self._gather()


    def _scroll(self,sleep_t):
        page_end = False
        bscroll_top = int(self._driver.execute_script('return document.body.scrollTop '))
        if bscroll_top == 0:
            bscroll_top = int(self._driver.execute_script('return window.scrollY'))

        self._driver.execute_script(f'document.documentElement.scrollTo(0,{self._inner_height})')
        self._inner_height += int(self._driver.execute_script('return window.innerHeight'))


        ascroll_top = int(self._driver.execute_script('return document.body.scrollTop '))
        if ascroll_top == 0:
            ascroll_top = int(self._driver.execute_script('return window.scrollY'))

        if bscroll_top == ascroll_top:
            page_end = True
        
        time.sleep(sleep_t)
        return page_end

    def _gather(self):
        """" gather all the screenshots as base64 """
        for i in range(self._max_page):
            self._scroll(sleep_t=0.5)
            screen_base64 = self._driver.get_screenshot_as_base64()
            screen_binary = base64.b64decode(screen_base64)
            screenshot = Image.open(io.BytesIO(screen_binary))
            #screenshot.save(f'{i}.png')
            page_end = self._all_screens.append(screenshot)
            if page_end is True:
                break

    def generate_64(self):
        """ combine all base64 imaages
        """
        im_width = max(img.width for img in self._all_screens)
        im_height = sum(img.height for img in self._all_screens)
        result = Image.new("RGB", (im_width, im_height))

        n_height = 0
        for img in self._all_screens:
            result.paste(img,(0,n_height))
            n_height += img.height
        
        buffered = io.BytesIO()
        result.save(buffered,format='PNG')
        base_64_string = base64.b64encode(buffered.getvalue()).decode("ascii")
        return base_64_string

def take_screenshot(driver,max_page=30):
    scr = ScPage(driver=driver,max_pages=max_page)
    base_64 = scr.generate_64()
    return base_64

def convert_64_img(base_64_str):
    with tempfile.NamedTemporaryFile(mode='wb',suffix='.png',delete=False) as f:
        f.write(base64.b64decode(base_64_str))
    return f.name






