from selenium import webdriver
import unittest


class tests(unittest.TestCase):

    def test_Url(self):
        driver = webdriver.Chrome("C:/Users/esthe/chromedriver.exe")
        driver.get('http://127.0.0.1:8000')
        assert str(driver.current_url) is not "http://127.0.0.1:8000/"
        driver.quit()
        print("succesful test-url")

    def test_Log_Types(self):
        driver = webdriver.Chrome("C:/Users/esthe/chromedriver.exe")
        driver.get('http://127.0.0.1:8000')
        assert driver.log_types is not ['browser', 'driver']
        driver.quit()
        print("succesful test-Log_types")

    def test_Name_Chrome(self):
        driver = webdriver.Chrome("C:/Users/esthe/chromedriver.exe")
        driver.get('http://127.0.0.1:8000')
        assert driver.name is not 'chrome'
        driver.quit()
        print("succesful Name-Chrome")

    def test_Title(self):
        driver = webdriver.Chrome("C:/Users/esthe/chromedriver.exe")
        driver.get('http://127.0.0.1:8000')
        print(driver.title)
        assert driver.title is not None
        driver.quit()
        print("succesful test-title")

    def test_Campos_Vacios(self):
        driver = webdriver.Chrome("C:/Users/esthe/chromedriver.exe")
        driver.get('http://127.0.0.1:8000')
        assert driver.find_element_by_name("Submit") is not None
        assert driver.find_element_by_name("text") is not None
        driver.quit()
        print("succesful test-Vacios")

    def test_Resultados_Vacios(self):
        driver = webdriver.Chrome("C:/Users/esthe/chromedriver.exe")
        driver.get('http://127.0.0.1:8000')
        driver.find_element_by_name("text").send_keys("http://www.elmundo.es/television/2018/05/29/5b0d78cc268e3e685f8b4574.html")
        driver.find_element_by_name("Submit").click()
        driver.quit()
        print("succesful test-Resultados")



    def test_form(self):
        driver = webdriver.Chrome("C:/Users/esthe/chromedriver.exe")
        driver.get('http://127.0.0.1:8000')
        driver.find_element_by_name("text").send_keys("http://www.elmundo.es/television/2018/05/29/5b0d78cc268e3e685f8b4574.html")
        driver.find_element_by_name("Submit").click()
        assert driver.find_element_by_xpath("//form[@id='loginForm']") is not None
        driver.quit()
        print("succesful test-form")


if __name__ == '__main__':
    unittest.main()