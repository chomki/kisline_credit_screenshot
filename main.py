from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time




driver= webdriver.Chrome()

driver.get('https://www.kisline.com/cm/CM0100M00GE00.nice') # 로그인 필요

list_a= ['1208147521','1058727606', 	'1298621106', 	'3568800968', 	'2218800605', 	'1448135088', 	'1448135088', 	'2158762176']
# 사업자등록번호 예시

for i in list_a:
    search=driver.find_element_by_name('searchValue') #검색창 입력
    search.click()
    search.send_keys(Keys.CONTROL+"a") #전체선택
    search.send_keys(Keys.DELETE) #삭제
    search.send_keys(i) # 사업자등록번호 입력
    time.sleep(0.5)
    search.send_keys(Keys.ENTER)
    time.sleep(1)
    name=driver.find_element_by_name('overViewOpen').text #사업자명
    driver.find_element_by_name('overViewOpen').click() #맨 위에있는 사업자 명 클릭
    driver.find_element_by_css_selector('div[class="overview_area03"]').click() # 신용도조회있는 table 클릭
    driver.maximize_window() #스크린샷 찍기 전 전체화면
    driver.save_screenshot(f"{name}_{i}.png") #회사명+사업자등록번호.png로 스크린샷 저장
    time.sleep(1.5)

    
    
