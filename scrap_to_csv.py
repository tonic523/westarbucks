from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.implicitly_wait(3)
driver.get('https://www.starbucks.co.kr/menu/drink_list.do')

## 카테고리 종류 
CATEGORIES = ['콜드 브루 커피', '브루드 커피', '에스프레소', '프라푸치노', '블렌디드', '스타벅스 피지오', '티(티바나)', '기타 제조 음료', '스타벅스 주스(병음료)']

################ 스타벅스 스크래핑 #########################################
data_row = []
data = []
for idx, category in enumerate(CATEGORIES):
    n = 1
    while True:
        try:
            product = driver.find_element_by_xpath(f"/html/body/div[3]/div[7]/div[2]/div[2]/div/dl/dd[1]/div[1]/dl/dd[{idx+1}]/ul/li[{n}]/dl/dt/a/img")
            ko_name = driver.find_element_by_xpath(f"/html/body/div[3]/div[7]/div[2]/div[2]/div/dl/dd[1]/div[1]/dl/dd[{idx+1}]/ul/li[{n}]/dl/dd").text ## 한글 이름
        except:
            break
        product.click() ## 스타벅스 음료 페이지에서 음료를 하나씩 클릭
        en_name = driver.find_element_by_xpath("/html/body/div[3]/div[7]/div[2]/div[1]/div[2]/div[1]/h4/span").text ## 영어 이름
        description = driver.find_element_by_xpath("/html/body/div[3]/div[7]/div[2]/div[1]/div[2]/div[1]/p").text ## 설명
        kcal = driver.find_element_by_xpath("/html/body/div[3]/div[7]/div[2]/div[1]/div[2]/form/fieldset/div/div[2]/ul[1]/li[1]/dl/dd").text ## 칼로리
        sodium = driver.find_element_by_xpath("/html/body/div[3]/div[7]/div[2]/div[1]/div[2]/form/fieldset/div/div[2]/ul[2]/li[1]/dl/dd").text ## 소금
        fat = driver.find_element_by_xpath("/html/body/div[3]/div[7]/div[2]/div[1]/div[2]/form/fieldset/div/div[2]/ul[1]/li[2]/dl/dd").text ## 지방
        sugar = driver.find_element_by_xpath("/html/body/div[3]/div[7]/div[2]/div[1]/div[2]/form/fieldset/div/div[2]/ul[2]/li[2]/dl/dd").text ## 당
        protein = driver.find_element_by_xpath("/html/body/div[3]/div[7]/div[2]/div[1]/div[2]/form/fieldset/div/div[2]/ul[1]/li[3]/dl/dd").text ## 단백질
        caffeine = driver.find_element_by_xpath("/html/body/div[3]/div[7]/div[2]/div[1]/div[2]/form/fieldset/div/div[2]/ul[2]/li[3]/dl/dd").text ## 카페인
        try:
            allergy = driver.find_element_by_xpath("/html/body/div[3]/div[7]/div[2]/div[1]/div[2]/form/fieldset/div/div[3]/p").text.split(':')[1][1:] ## 알러지, 없다면 null값으로
        except:
            allergy = None
        data_row = [category, ko_name, en_name, description, kcal, sodium, fat, sugar, protein, caffeine, allergy] ## 음료 상품 하나의 레코드
        data.append(data_row) ## 모든 레코드 저장
        print(data_row)
        driver.back() ## 스타벅스 음료 페이지로
    
        n+=1
#####################################################################
## 저장된 레코드를 csv파일로 이동
filename = "products.csv"
f = open(f"csv/{filename}", "w")
f.close()

dataFrame = pd.DataFrame(data, columns = ['category', 'ko_name', 'en_name', 'description', 'kcal', 'sodium', 'fat', 'sugar', 'protein', 'caffeine', 'allergy'])
dataFrame.to_csv(f"csv/{filename}", index=False)
