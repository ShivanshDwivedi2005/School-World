# School-World

**School-World** is a platform designed to manage and organize various school activities for multiple schools from a single system.
It helps schools handle administrative and academic operations such as student management, attendance tracking, fee management, and other essential school processes efficiently.

The goal of this project is to provide a **centralized system where multiple schools can manage their daily operations in a structured and scalable way.**

---

# Features

* Manage multiple schools on a single platform
* Student management system
* Attendance tracking
* Fee management
* Administrative management
* Organized backend structure for scalability
* REST API based architecture

---

# Tech Stack

* **Python**
* **FastAPI**
* **PostgreSQL**
* **Neon Database**
* **Docker**
* **Pydantic**
* **SQLAlchemy**

---

# Project Structure

```
School-World/
│
├── app/
│   ├── main.py
│   ├── routers/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   └── database/
│
├── tests/
│
├── requirements.txt
├── Dockerfile
└── README.md
```

---

# Installation

### 1. Clone the Repository

```
git clone https://github.com/ShivanshDwivedi2005/School-World.git
```

### 2. Navigate to the Project Directory

```
cd School-World
```

### 3. Create a Virtual Environment

```
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows**

```
venv\Scripts\activate
```

**Linux / Mac**

```
source venv/bin/activate
```

### 5. Install Dependencies

```
pip install -r requirements.txt
```

---

# Running the Application

Start the FastAPI server using:

```
uvicorn app.main:app --reload
```

The server will run at:

```
http://127.0.0.1:8000
```

---

# API Documentation

FastAPI automatically generates API documentation.

Swagger UI:

```
http://127.0.0.1:8000/docs
```

ReDoc:

```
http://127.0.0.1:8000/redoc
```

---

# Example Functionalities

* Register and manage schools
* Manage students and staff records
* Track student attendance
* Manage fee records and payments
* Administrative controls for school management

---

# Future Improvements

* Role-based authentication (Admin, Teacher, Student)
* Dashboard analytics
* Notifications system
* Parent portal
* Mobile application integration

---

# Contributing

Contributions are welcome.

1. Fork the repository
2. Create a new branch

```
git checkout -b feature-name
```

3. Commit your changes

```
git commit -m "Add new feature"
```

4. Push the branch

```
git push origin feature-name
```
