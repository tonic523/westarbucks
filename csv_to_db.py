import csv
from products.models import *

### 사용 설명 ###
# 1. scrap_to_csv 를 먼저 실행해서 스타벅스 음료들을 csv에 저장합니다.
# 2. menus 테이블에 음료는 담겨있어야 합니다.
# 3. 실행하면 원래 있던 products, nutritions의 db는 삭제되고 scrap한 내용들이 db에 저장됩니다.

### 추가 구현할 내용 ###
# image, allergy db 추가
# nutrition 의 size column 추가

######## 카테고리 db 추가 #########
CATEGORIES = ['콜드 브루 커피', '브루드 커피', '에스프레소', '프라푸치노', '블렌디드', '스타벅스 피지오', '티(티바나)', '기타 제조 음료', '스타벅스 주스(병음료)']
for idx, category in enumerate(CATEGORIES):
    Category.objects.create(name = category, menu = Menu.objects.get(name = "음료"), id = idx+ 1)
###################################
    
# db 초기화
Product.objects.all().delete()
Nutrition.objects.all().delete()
# Allergies_products.objects.all().delete()
# Allergy.objects.all().delete()


hand = open('csv/products.csv')
products = list(csv.reader(hand))
# 카테고리 = row[0], product 정보 = {ko_name:row[1],en_name:row[2], description:row[3]}
# nutrition 정보 =  {one_serving_kcal:float(row[4]), sodium_mg:float(row[5]), saturated_fat_g:float(row[6]), sugars_g:float(row[7]), protein_g:float(row[8]), caffeine_mg:float(row[9])}


for row in products[1:]:
    Product.objects.create(ko_name=row[1],en_name=row[2], description=row[3], category=Category.objects.get(name = row[0]))
    Nutrition.objects.create(product_name=row[1], one_serving_kcal=float(row[4]), sodium_mg=float(row[5]), saturated_fat_g=float(row[6]), sugars_g=float(row[7]), protein_g=float(row[8]), caffeine_mg=float(row[9]))
    p_obj = Product.objects.get(ko_name = row[1])
    # try:
    #     p_obj.allergy.add(Allergy.objects.get(name = row[13]))
    # except:
    #     pass
    p_obj.nutrition = Nutrition.objects.get(product_name = row[1])
    p_obj.save()
