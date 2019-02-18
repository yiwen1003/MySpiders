#!/usr/bin/env python
# -*- coding:utf-8 -*-

from selenium import webdriver

driver = webdriver.Firefox()
driver.get('https://translate.google.cn/')
#assert "google" in driver.title
input_element = driver.find_element_by_xpath("//*[@id='source']")
print(input_element)
input_element.send_keys("春节")
#output_element = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]")

driver.find_elements_by_id("sugg-item-en")[1].click()
driver.find_elements_by_id("sugg-item-en")[1].click()