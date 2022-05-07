from selenium import webdriver
from selenium.webdriver.common.by import By

def getDescByLink( url ):
  driver = webdriver.Chrome()
  driver.get(url)

  driver.find_element(By.CLASS_NAME, 'ant-modal-close-x').click()

  metas = driver.find_elements(By.TAG_NAME, 'meta')
  data = {}
  for meta in metas:
    if meta.get_attribute('property') == 'og:url':
      data['url'] = meta.get_attribute('content')
    if meta.get_attribute('property') == 'og:description':
      data['desc'] = meta.get_attribute('content')
    if meta.get_attribute('property') == 'og:title':
      data['title'] = meta.get_attribute('content')

  driver.quit()
  return data
