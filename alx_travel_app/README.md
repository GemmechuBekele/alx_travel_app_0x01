# ALX Travel App 0x01

This is a Django REST API project that provides endpoints to manage travel **Listings** and **Bookings**. It uses Django REST Framework (DRF) and is documented with Swagger (drf-yasg).

---

## 🚀 Features

- CRUD API for Listings
- CRUD API for Bookings
- RESTful endpoints using DRF ViewSets and Routers
- Swagger UI for API documentation

---

## 📁 Project Structure
alx_travel_app_0x01/
├── alx_travel_app/
│   ├── alx_travel_app/
│   └── listings/
├── manage.py
└── venv/


---

## 📦 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/alx_travel_app_0x01.git
cd alx_travel_app_0x01

---

### 2. Create and activate a virtual environment

python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

---

### 3. Install dependencies
pip install -r requirements.txt

---

### 4. Apply migrations and Run the server
python manage.py migrate
python manage.py runserver

