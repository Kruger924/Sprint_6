import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

WAIT_SECONDS = 5


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Получение URL текущей страницы')
    def get_current_url(self):
        '''Получение url текушей страницы.'''
        return self.driver.current_url

    @allure.step('Получение элемента страницы: {locator}')
    def get_element(self, locator):
        '''Получение заданного элемента страницы.'''
        return self.driver.find_element(*locator)

    @allure.step('Клик по элементу: {locator}')
    def click_element(self, locator):
        '''Клик по элементу.'''
        self.get_element(locator).click()

    @allure.step('Ожидание события: {event}, таймаут: {seconds} секунд')
    def wait_for(self, event, seconds=WAIT_SECONDS):
        '''Приостановка работы драйвера.'''
        WebDriverWait(self.driver, seconds).until(event)

    @allure.step('Переключение на окно с URL: {url}')
    def switch_window(self, url):
        '''Переключение на последнее открытое окно (вкладку) браузера.'''
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.wait_for(EC.url_to_be(url))

    @allure.step('Прокрутка страницы до элемента: {locator}')
    def scroll_to_element(self, locator):
        '''Прокрутка экрана до элемента.'''
        self.driver.execute_script(
            'arguments[0].scrollIntoView()', self.get_element(locator)
        )
        self.wait_for(EC.visibility_of_element_located(locator))

    @allure.step('Заполнение поля формы {locator} значением: {value}')
    def fill_form_field(self, locator, *value):
        '''Заполнение поля формы.'''
        self.get_element(locator).send_keys(value)