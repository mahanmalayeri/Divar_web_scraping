import requests
from bs4 import BeautifulSoup
import pyodbc
# -----Turn the persian numbers to English numbers-----
def fa_to_en_number(text):
    fa_digits = "۰۱۲۳۴۵۶۷۸۹"
    en_digits = "0123456789"
    return text.translate(str.maketrans(fa_digits, en_digits))

# -----Your connection string-----
def connection():
    conn_str = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=servername;"
        "DATABASE=DivarDB;"
        "Trusted_Connection=yes;"
    )
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    return conn, cursor
conn, cursor = connection()

# -----Your page url-----
def get_page():
    url = "https://divar.ir/s/tehran/car?production-year=1385-1395&q=206"
    response = requests.get(url)
    return BeautifulSoup(response.text, "html.parser")


# -----Web Scarping main codes-----
def page():
    page_html = get_page()
    infoes = page_html.find_all("div", class_="kt-post-card__info")

    for info in infoes:
        car_model = info.h2.string

        descriptions = info.find_all("div", class_="kt-post-card__description") # Get description info
        car_function = descriptions[0].string 
        car_price = descriptions[1].string

        car_price = car_price.split(" ")[0] # split (تومان) from price
        car_price = fa_to_en_number(car_price) # Use persian to english function
        car_price = car_price.replace(",", "").strip() # Remove ( , ) from price

        car_place = info.find(
            "span", class_="kt-post-card__bottom-description"
        ).string
        car_zone = car_place.split("در", 1)[1].strip() # Find car zone

        cursor.execute(
            "INSERT INTO [206cars] VALUES (?,?,?,?)",
            (car_model, car_function, car_price, car_zone)
        ) # Insert to sql 

page()
conn.commit()
conn.close()

