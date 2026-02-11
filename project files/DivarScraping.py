import requests
from bs4 import BeautifulSoup



url = "https://divar.ir/s/tehran/car?production-year=1385-1395&q=206"

response = requests.get(url)
page_html = BeautifulSoup(response.text,features="html.parser")

infoes = page_html.find_all("div",class_="kt-post-card__info")
for info in infoes:
    car_model = info.h2.string
    descriptions = info.find_all("div", class_="kt-post-card__description")

    car_function = descriptions[0].string
    car_price = descriptions[1].string
    car_price =car_price.split(" ")[0].strip()
    car_place = info.find("span",class_="kt-post-card__bottom-description").string
    car_zone = car_place.split("در", 1)[1].strip()

    print(car_model,car_function,car_price,car_zone)