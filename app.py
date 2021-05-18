from selenium import webdriver
import time
from selenium.webdriver.common.alert import Alert

driver=webdriver.Chrome("/Users/goyoonjae/Desktop/jaga-auto/chromedriver")
url = "https://hcs.eduro.go.kr/#/loginWithUserInfo"

driver.get(url)
driver.find_element_by_css_selector('#btnConfirm2').click()
print('자가진단 참여하기 버튼 클릭 성공')
name=['고윤재','박정휴','김태훈','동현우']
pswd=['0612','0914','0408','0316']
bd=['040612','040914','040526','040603']

for i in range(len(name)):
    
    time.sleep(2) 
    # driver.find_element_by_css_selector('#btnConfirm2').click()
    # print('자가진단 참여하기 버튼 클릭 성공')
    time.sleep(1)
    driver.find_element_by_css_selector('#WriteInfoForm > table > tbody > tr:nth-child(1) > td > button').click()
    print('검색버튼 클릭 완료')
    
    driver.find_element_by_css_selector('#sidolabel > option:nth-child(10)').click()
    print('경기도 선택')

    driver.find_element_by_css_selector('#crseScCode > option:nth-child(5)').click()
    print('고등학교 선택')
    time.sleep(0.1)

    driver.find_element_by_css_selector('#orgname').send_keys('한국디지털미디어고등학교')
    print('디미고 입력')

    driver.find_element_by_css_selector('#softBoardListLayer > div.layerContentsWrap > div.layerSchoolSelectWrap > table > tbody > tr:nth-child(3) > td:nth-child(3) > button').click()

    print('학교 검색버튼 클릭')
    time.sleep(1)

    driver.find_element_by_css_selector('#softBoardListLayer > div.layerContentsWrap > div.layerSchoolSelectWrap > ul > li > a > p > a > em').click()

    driver.find_element_by_css_selector('#softBoardListLayer > div.layerContentsWrap > div.layerBtnWrap > input').click()

    driver.find_element_by_css_selector('#user_name_input').send_keys(name[i])

    driver.find_element_by_css_selector('#birthday_input').send_keys(bd[i])

    driver.find_element_by_css_selector('#btnConfirm').click()
    time.sleep(0.5)

    driver.find_element_by_css_selector('#WriteInfoForm > table > tbody > tr > td > input').send_keys(pswd[i])

    driver.find_element_by_css_selector('#btnConfirm').click()
    time.sleep(1)

    driver.find_element_by_css_selector('#container > div > section.memberWrap > div:nth-child(2) > ul > li > a > span.name').click()
    time.sleep(1)

    driver.find_element_by_css_selector('#survey_q1a1').click()
    print('설문1 완료')

    driver.find_element_by_css_selector('#survey_q2a1').click()
    print('설문2 완료')

    driver.find_element_by_css_selector('#survey_q3a1').click()
    print('설문3 완료')

    driver.find_element_by_css_selector('#btnConfirm').click()
    print('자가진단 완료')

    driver.find_element_by_css_selector('#topMenuBtn').click()
    print('메뉴 버튼 클릭 완료')
    time.sleep(1)

    driver.find_element_by_css_selector('#topMenuWrap > ul > li:nth-child(4) > button').click()
    print('로그아웃 완료')

    alert = driver.switch_to.alert
    alert.accept()
    time.sleep(3)

    driver.find_element_by_css_selector('body > app-root > div > div.secondary_pw > div > button').click()
    print('다른계정으로 로그인')
    
    alert = driver.switch_to.alert
    alert.accept()
    time.sleep(2)
    driver.get(url)
    
driver.quit()
