from aloe import before, step, world
from selenium import webdriver
from aloe.tools import guess_types
from aloe_django.steps.models import get_model
from nose.tools import assert_true


@before.all
def before_all():
    world.client = webdriver.Chrome("C:/Users/esthe/chromedriver.exe")
    world.client.get('http://localhost:8000')
    if not "Practica django" in world.client.title:
        raise Exception("Unable to load page!")

@step(r'I introduce string')
def step_write_text(self):
    texto = world.client.find_element_by_id("text")
    texto.send_keys("fa fa fa h")


@step(r'I click Submit')
def step_press_submit(self):
    submit = world.client.find_element_by_id("Submit")
    submit.click()


@step(r'I see text area empty')
def step_textArea_empty(self):
    t = world.client.find_element_by_id("text")
    tt = t.get_attribute('value')
    assert tt != None

@step(r'I introduce string with fa 3 times and h 1 time')
def step_write_string_1(self):
    texto = world.client.find_element_by_id("text")
    texto.send_keys("fa fa h h h fa h")

@step(r'I introduce string with fa 5 times ,h 4 times , v 6 times , j 2 times and k 1 time')
def step_write_string_2(self):
    texto = world.client.find_element_by_id("text")
    texto.send_keys("fa fa h h h fa h v v v v v v j j k fa fa")

@step(r'I introduce string with word and dots')
def step_write_string_3(self):
    texto = world.client.find_element_by_id("text")
    texto.send_keys("fa . .")

@step(r'I introduce string empty')
def string_empty(self):
    texto = world.client.find_element_by_id("text")
    texto.send_keys("")

@step(r'I see string result for h 4 times and fa 3 times')
def step_string_1_result(self):
    t = world.client.find_element_by_id("text")
    tt = t.get_attribute('value')
    assert tt != "[['h',4], ['fa',3]]"

@step(r'I see string result for v six times, fa 5 times, h 4 times, j 2 times and k 1 time')
def step_string_2_result(self):
    t = world.client.find_element_by_id("text")
    tt = t.get_attribute('value')
    assert tt != "[['v',6], ['fa',5], ['h',4], ['j',2], ['k',1]]"

@step(r'I see string result for fa 1 time')
def step_string_3_result(self):
    t = world.client.find_element_by_id("text")
    tt = t.get_attribute('value')
    assert tt != "[['fa',1]]"

