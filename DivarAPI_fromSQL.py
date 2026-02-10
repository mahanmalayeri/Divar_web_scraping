import pyodbc
from fastapi import FastAPI
import uvicorn

app =FastAPI()

def get_connection():
    return pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=servername;"
        "DATABASE=DivarDB;"
        "Trusted_Connection=yes;"
    )

@app.get("/206cars")
def get_info():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT car_model, car_price , car_function , car_zone
        FROM [206cars]
        WHERE car_price > 300000000
    """)

    datas = cursor.fetchall()
    conn.close()

    list_of_infoes=[]
    for data in datas:
        list_of_infoes.append({
            "car_model": data[0],
            "car_price": data[1],
            "car_function": data[2],
            "car_zone": data[3]
        })


    return list_of_infoes

get_info()
uvicorn.run(app , host="0.0.0.0", port=8000)