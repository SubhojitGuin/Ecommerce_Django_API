# E-Commerce Django REST API

This is an E-Commerce API built with Django and Django REST framework. It provides endpoints for managing users and products.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [License](#license)
- [Contributors](#contributors)

## Features

- User management (registration, login, wishlist, cart, etc.)
- Product management (CRUD operations - product details, reviews)
- Order management (CRUD operations)
- Payment gateway integration (Stripe)
- Authentication and Authorization (using Django's built-in auth system)
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
   ```

2. **Create a virtual environment**
    ```sh
    python -m venv .venv
    .\.venv\Scripts\activate
    ```

3. **Install Dependencies**
    ```sh
    pip install -r requirements.txt
    ```

4. **Change the directory**
    ```sh
    cd Ecommerce
    ```

4. **Apply migrations:**
    ```sh
    python manage.py migrate
    ```
  
6. **Create a superuser:**
    ```sh
    python manage.py createsuperuser
    ```
    Now add your credentials and save it.

7. **Create the .env file**
    Create a *.env* file in Ecommerce\Ecommerce folder an copy the format from [.env.sample](https://github.com/SubhojitGuin/Ecommerce_Django_API/blob/main/Ecommerce/Ecommerce/.env.sample) i.e.:

    ```sh
    STRIPE_SECRET_KEY=your_stripe_secret_key
    STRIPE_PUBLISHABLE_KEY=your_stripe_publishable_key
    TAX=tax_rate
    ```

    To get your stripe keys, click [here](https://dashboard.stripe.com/test/dashboard).

8. **Run the development server:**
    ```sh
    python manage.py runserver
    ```

## Usage

### Access the Admin Panel
Access the admin panel at `http://localhost:8000/admin/` using the superuser credentials.

![admin page](https://github.com/SubhojitGuin/Ecommerce_Django_API/blob/main/images/admin.png?raw=true)

### Access the API Documentation
- Swagger UI: `http://localhost:8000/swagger/`
- ReDoc: `http://localhost:8000/redoc/`

![api documentation](https://github.com/SubhojitGuin/Ecommerce_Django_API/blob/main/images/Ecommerce.png?raw=true)

## API Endpoints

### Order API
![order api](https://github.com/SubhojitGuin/Ecommerce_Django_API/blob/main/images/order.png?raw=true)

### Payment API
![payment api](https://github.com/SubhojitGuin/Ecommerce_Django_API/blob/main/images/payment.png?raw=true)

### Product API
![product api](https://github.com/SubhojitGuin/Ecommerce_Django_API/blob/main/images/product.png?raw=true)

### User API
![user api](https://github.com/SubhojitGuin/Ecommerce_Django_API/blob/main/images/user.png?raw=true)

## License
This project is licensed under the MIT License. See the [🎗️LICENSE](LICENSE) file for details.

## Contributors

[![langchain contributors](https://contrib.rocks/image?repo=SudeshnaPathak/Ecommerce_Django_API&max=2000)](https://github.com/SudeshnaPathak/Ecommerce_Django_API/graphs/contributors)