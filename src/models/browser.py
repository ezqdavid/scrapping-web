from random import randint
from selenium.webdriver import Edge
from selenium.webdriver.edge.options import Options
import subprocess
import time
import faker
from selenium.webdriver.common.by import By
#import wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

proxys = ['http://190.103.177.131:80', 'http://200.71.237.238:23500' ]

class Browser:
    def __init__(self, proxy='http://190.103.177.131:80',port=9222):
        self.proxy = proxy
        self.crear_driver(proxy, port)

    def crear_driver(self, proxy, port=9222):
        fake = faker.Faker()
        self.port = port
        edge_options = Options()
        edge_options.add_experimental_option("debuggerAddress", f"127.0.0.1:{port}")
        #self.edge_options.add_argument("--headless")
        edge_options.add_argument(f"user-agent={fake.user_agent()}")
        #self.edge_options.add_argument("--no-sandbox")
        edge_options.add_argument("--disable-dev-shm-usage")
        #self.edge_options.add_argument("--disable-gpu")
        edge_options.add_argument("--disable-extensions")
        edge_options.add_argument("--disable-infobars")
        edge_options.add_argument("--disable-popup-blocking")
        edge_options.add_argument("--disable-web-security")
        edge_options.add_argument("--disable-site-isolation-trials")
        edge_options.add_argument("--ignore-certificate-errors")
        edge_options.add_argument("--ignore-ssl-errors")
        edge_options.add_argument("--allow-running-insecure-content")
        edge_options.add_argument("--disable-notifications")
        edge_options.add_argument("--no-first-run")
        if proxy:
            edge_options.add_argument(f"--proxy-server={proxy}")
        self.driver = Edge(options=edge_options)

    def get(self, url, timeout=30, max_retries=3):
        """Method to navigate to a URL with timeout and retry mechanism."""
        for attempt in range(max_retries):
            try:
                self.driver.get(url)
                time.sleep(randint(1, 3))
                WebDriverWait(self.driver, timeout).until(
                    EC.presence_of_element_located((By.TAG_NAME, "body"))
                )
                # find <title>Just a moment...</title>
                if ";</span>Just a moment...<span " in self.driver.page_source:
                    print("Just a moment... page detected")
                    raise TimeoutException("Just a moment... page detected")
                self.page_source = self.driver.page_source
                return  # Successfully loaded the page
            except TimeoutException:
                print(f"Attempt {attempt + 1} timed out. Retrying...")
                if attempt < max_retries - 1:
                    self.__reinstantiate_driver()
                else:
                    raise TimeoutException(f"Failed to load {url} after {max_retries} attempts")
                
    def __reinstantiate_driver(self):
        self.driver.quit()
        if self.proxy:
            proxy_usar = [proxy for proxy in proxys if proxy != self.proxy][0]
        else:
            proxy_usar = proxys[0]
        self.proxy = proxy_usar
        self.crear_driver(self.proxy)



if __name__ == '__main__':
    navegadores = []
    for proxy in proxys:
        navegador = Browser(proxy)
        navegadores.append(navegador)
    
    for navegador in navegadores:
        navegador.get('http://httpbin.io/ip')
        time.sleep(3)
        #check if the proxy is being used
        print(navegador.driver.find_element(By.TAG_NAME, "body").text)
        navegador.driver.quit()


    