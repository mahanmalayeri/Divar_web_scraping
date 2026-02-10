# 🚗 Divar Peugeot 206 Price Tracker (API + Database)

A professional Python project that **scrapes Peugeot 206 car listings from Divar**, stores the data in **SQL Server**, and exposes it through a **FastAPI REST API** for easy access and integration.

---

## 📌 Project Overview

This project is designed as an **end-to-end data pipeline**:

1. **Web scraping** car listings from Divar.ir  
2. **Cleaning and normalizing Persian data**
3. **Persisting data** in Microsoft SQL Server  
4. **Serving data** via a RESTful API  

It is suitable for:
- Price monitoring
- Data analysis
- Backend/API learning
- Real-world scraping + database integration

---

## 📂 Project Files

### 🔹 `2-divar_scraping.py` — Web Scraper
Scrapes Peugeot 206 listings from Divar (Tehran).

**Extracted fields:**
- Car model
- Mileage (function)
- Price
- Location (zone)

**Technologies:**
- `requests`
- `BeautifulSoup`

✅ Outputs raw scraped data (no database interaction)

---

### 🔹 `3-insert_to_sql.py` — Database Insertion Layer
Fetches listings and inserts cleaned data into SQL Server.

**Key features:**
- Persian → English digit conversion
- Price normalization (comma & text removal)
- Direct insertion into `[206cars]` table

**Technologies:**
- `requests`
- `BeautifulSoup`
- `pyodbc`
- Microsoft SQL Server

✅ Responsible for **data persistence**

---

### 🔹 `4-API_car_price.py` — REST API (FastAPI)
Exposes stored data via an HTTP API.

**Endpoint:**
```http
GET /206cars
