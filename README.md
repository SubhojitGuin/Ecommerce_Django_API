# E-Commerce Django REST API

This is an E-Commerce API built with Django and Django REST framework. It provides endpoints for managing users and products.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [License](#license)

## Features

- User management (registration, login, etc.)
- Product management (CRUD operations)
- API documentation with Swagger UI and ReDoc

## Installation

### Prerequisites

- Python 3.6+
- Django 3.0+
- Django REST framework
- `drf_yasg` for API documentation

### Setup

1. **Clone the repository**:
   ```sh
   git clone https://github.com/SubhojitGuin/Ecommerce_Django_API.git
   cd Ecommerce_Django_API

2. **Create a virtual environment**
    ```sh
    python -m venv .venv
    source .venv/bin/activate

3. **Install Dependencies**
    ```sh
    pip install -r requirements.txt

4. **Apply migrations:**
    ```sh
    python manage.py migrate
  
5. **Create a superuser:**
    ```sh
    python manage.py createsuperuser

6. **Run the development server:**
    ```sh
    python manage.py runserver

### Usage

#### Access the Admin Panel
Access the admin panel at `http://localhost:8000/admin/` using the superuser credentials

#### Access the API Documentation
- Swagger UI: `http://localhost:8000/swagger/`
- ReDoc: `http://localhost:8000/redoc/`

### License
This project is licensed under the MIT License. See the [📃LICENSE](LICENSE) file for details.