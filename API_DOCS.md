# API Docs

## Table of Contents
- [Order API](#order-api)
- [Payment API](#payment-api)
- [Product API](#product-api)


## Order API
### Order API Overview
The Order API is used to manage orders in the system. It allows you to create and read orders.

### Order API Endpoints
1. #### `POST /order/create/{user_id}`
    **Description**: Creates a new order for the specified user.

    The JSON object represents an order submitted by a user.
    - **`payment_method`**: The payment method used for the order (e.g. `cod` for Cash on Delivery, and `online` for Online Payment).
    - **`address`**: The address to which the order should be delivered.

    Request Payload:
    ```sh
    {
        "payment_method": "cod",
        "address": "user_adress"
    }
    ```

2. #### `GET /order/get_all_orders/{user_id}/`
    **Description**: Retrieves all orders for the specified user.

3. #### `GET /order/get_order/{order_id}/`
    **Description**: Retrieves a specific order by its ID.

## Payment API
### Payment API Overview
The Payment API is used to manage payments in the system. It allows you to create payments

### Payment API Endpoints
1. #### `POST /payment/make_payment/{order_id}`
    **Description**: Makes a payment for the specified order.

    The JSON object represents a payment submitted by a user.
    - **`payment_method_id`**: The ID of the payment method used for the payment.

    Request Payload:
    ```sh
    {
        "payment_method_id": "pm_card_visa"
    }
    ```

## Product API
### Product API Overview
The Product API is used to manage products in the system. It allows you to create, read and update products and manage their reviews and ratings along with filtering of products based on Price, Category, Rating and filtering product reviews based on Ratings.

### Product API Endpoints
1. #### `POST /product/add_review/`
    **Description**: Adds a review for a product.

    This JSON object represents a product review submitted by a user.
    - **`user`**: The ID of the user who submitted the review.
    - **`product`**: The ID of the product being reviewed.
    - **`rating`**: The rating given to the product by the user (out of 5).
    - **`review`**: The textual review provided by the user.

    Request Payload:
    ```sh
    {
        "user": 4,
        "product": 3,
        "rating": 5,
        "review": "Good product"
    }
    ```

2. #### `POST /product/create/`
    **Description**: Creates a new product in the system.

    The JSON object represents a product to be created.
    - **`name`**: The name of the product.
    - **`description`**: The description of the product.
    - **`price`**: The price of the product.
    - **`quantity`**: The quantity of the product available.
    - **`brand`**: The brand of the product.
    - **`category`**: The category of the product.
    - **`image_path`**: The path to the image of the product.

    Request Payload:
    ```sh
    {
        "name": "Product",
        "description": "Product Description",
        "price": 40.00,
        "quantity": 5,
        "brand": "Brand Name",
        "category": "Category",
        "image_path": "/images/products/product.jpg"
    }
    ```

3. #### `DELETE /product/delete/`
    **Description**: Deletes a product from the system.

    The JSON object represents the product to be deleted.
    - **`id`**: The ID of the product to be deleted.

    Request Payload:
    ```sh
    {
        "id": 1
    }
    ```

4. #### `DELETE /product/delete_review/{user_id}/{product_id}/`
    **Description**: Deletes a review for a product.
    - **`user_id`**: The ID of the user who submitted the review.
    - **`product_id`**: The ID of the product being reviewed.

5. #### `GET /product/detail/{product_id}/`
    **Description**: Retrieves the details of a specific product by its ID.
    - **`product_id`**: The ID of the product.

6. #### `GET /product/filter_review_by_rating/{product_id}/{rating}/`
    **Description**: Retrieves reviews for a product filtered by rating.
    - **`product_id`**: The ID of the product.
    - **`rating`**: The rating to filter by.

7. #### `POST /product/filterby_brand/`
    **Description**: Retrieves products filtered by brand.

    The JSON object represents the filter criteria.
    - **`brand`**: The brand to filter by.

    Request Payload:
    ```sh
    {
        "brand": "Brand Name"
    }
    ```

8. #### `POST /product/filterby_category/`
    **Description**: Retrieves products filtered by category.

    The JSON object represents the filter criteria.
    - **`category`**: The category to filter by.

    Request Payload:
    ```sh
    {
        "category": "Category Name"
    }
    ```

9. #### `POST /product/filterby_price/`
    **Description**: Retrieves products filtered by price range.

    The JSON object represents the filter criteria.
    - **`min_price`**: The minimum price.
    - **`max_price`**: The maximum price.

    Request Payload:
    ```sh
    {
        "min_price": 20.00,
        "max_price": 50.00
    }
    ```

10. #### `POST /product/filter_review_by_rating/`
