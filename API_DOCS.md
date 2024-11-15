# API Docs

## Table of Contents
- [Order API](#order-api)
- [Payment API](#payment-api)
- [Product API](#product-api)
- [User API](#user-api)

## Order API
### Order API Overview
The Order API is used to manage orders in the system. It allows you to create and read orders.

### Order API Endpoints
1. #### `POST /order/create/{user_id}`
    **Description**: Creates a new order for the specified user.
    - **`user_id`**: The ID of the user who is placing the order.

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
    - **`user_id`**: The ID of the user.

3. #### `GET /order/get_order/{order_id}/`
    **Description**: Retrieves a specific order by its ID.
    - **`order_id`**: The ID of the order.

## Payment API
### Payment API Overview
The Payment API is used to manage payments in the system. It allows you to create payments

### Payment API Endpoints
1. #### `POST /payment/make_payment/{order_id}`
    **Description**: Makes a payment for the specified order.
    - **`order_id`**: The ID of the order for which the payment is being made.

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

10. #### `GET /product/get_review/{product_id}/`
    **Description**: Retrieves reviews for a specific product by its ID.
    - **`product_id`**: The ID of the product.

11. #### `GET /product/list/{user_id}/`
    **Description**: Retrieves a list of products for a specific user.
    - **`user_id`**: The ID of the user.

12. #### `POST /product/search/`
    **Description**: Searches for products based on a keyword. All the keys are optional. If a key is not provided, it is not used in the search. It also supports partial search for the keyword. For example, if the keyword is "lap", it will return products with names like "Laptop", "Lapdesk", etc.

    The JSON object represents the search criteria.
    - **`name`**: The keyword to search for.
    - **`brand`**: The brand to search in.
    - **`category`**: The category to search in.
    - **`min_price`**: The minimum price.
    - **`max_price`**: The maximum price.

    Request Payload:
    ```sh
    {
    "name": "",
    "brand": "",
    "min_price": 80000,
    "max_price": 150000,
    "category": "Lap"
    }
    ```

13. #### `PUT /product/update/`
    **Description**: Updates a product. All the keys are optional. If a key is not provided, it is not used in the update. The ID of the product to be updated must be provided.

    The JSON object represents the product to be updated.
    - **`id`**: The ID of the product to be updated.
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
        "id": 1,
        "name": "Product",
        "description": "Product Description",
        "price": 40.00,
        "quantity": 5,
        "brand": "Brand Name",
        "category": "Category",
        "image_path": "/images/products/product.jpg"
    }
    ```

14. #### `PUT /product/update_review/{user_id}/{product_id}`
    **Description**: Updates a review for a product.
    - **`user_id`**: The ID of the user who submitted the review.
    - **`product_id`**: The ID of the product being reviewed.

    The JSON object represents the updated review.
    - **`rating`**: The updated rating given to the product by the user (out of 5).
    - **`review`**: The updated textual review provided by the user.

    Request Payload:
    ```sh
    {
        "rating": 4,
        "review": "Updated review"
    }
    ```

## User API
### User API Overview
The User API is used to manage users in the system. It allows you to create, read, update, delete, signup and signin users. It also provides endpoints for adding, updating and removing from a user's cart and wishlist.

### User API Endpoints
1. #### `POST /user/add_to_cart/`
    **Description**: Adds a product to the user's cart.

    The JSON object represents the product to be added to the cart.
    - **`user_id`**: The ID of the user.
    - **`product_id`**: The ID of the product.

    Request Payload:
    ```sh
    {
        "user_id": 1,
        "product_id": 2
    }
    ```

2. #### `GET /user/add_to_wishlist/{user_id}/{product_id}/`
    **Description**: Adds a product to the user's wishlist.
    - **`user_id`**: The ID of the user.
    - **`product_id`**: The ID of the product.

3. #### `DELETE /user/clear_cart/{user_id}`
    **Description**: Clears the user's cart.
    - **`user_id`**: The ID of the user.

4. #### `DELETE /user/delete/`
    **Description**: Deletes a user.
    - **`id`**: The ID of the user to be deleted.

    The JSON object represents the user to be deleted.
    Request Payload:
    ```sh
    {
        "id": 1
    }
    ```

5. #### `GET /user/get_cart/{user_id}/`
    **Description**: Retrieves the user's cart.
    - **`user_id`**: The ID of the user.

6. #### `GET /user/get_wishlist/{user_id}/`
    **Description**: Retrieves the user's wishlist.
    - **`user_id`**: The ID of the user.

7. #### `POST /user/login/`
    **Description**: Logs in a user.

    The JSON object represents the user's login credentials.
    - **`email`**: The email of the user.
    - **`password`**: The password of the user.

    Request Payload:
    ```sh
    {
        "email": "user_email",
        "password": "user_password"
    }
    ```

8. #### `GET /user/user_profile/{user_id}/`
    **Description**: Retrieves the profile of a user.
    - **`user_id`**: The ID of the user.

9. #### `DELETE /user/remove_from_cart/{user_id}/{product_id}/`
    **Description**: Removes a product from the user's cart.
    - **`user_id`**: The ID of the user.
    - **`product_id`**: The ID of the product.

10. #### `DELETE /user/remove_from_wishlist/{user_id}/{product_id}/`
    **Description**: Removes a product from the user's wishlist.
    - **`user_id`**: The ID of the user.
    - **`product_id`**: The ID of the product.

11. #### `POST /user/signup/`
    **Description**: Signs up a new user.

    The JSON object represents the user's signup details.
    - **`first_name`**: The first name of the user.
    - **`last_name`**: The last name of the user.
    - **`email`**: The email of the user.
    - **`password`**: The password of the user.
    - **`phone_number`**: The phone number of the user.
    - **`address`**: The address of the user.
    - **`city`**: The city of the user.
    - **`state`**: The state of the user.
    - **`country`**: The country of the user.
    - **`pin_code`**: The zip code of the user.
    - **`date_of_birth`**: The date of birth of the user.

    Request Payload:
    ```sh
    {
        "first_name": "First Name",
        "last_name": "Last Name",
        "email": "user_email",
        "password": "user_password",
        "phone_number": 0123456789,
        "address": "user_address",
        "city": "user_city",
        "state": "user_state",
        "country": "user_country",
        "pin_code": 10001,
        "date_of_birth": "1990-05-15"
    }
    ```

12. #### `PUT /user/update/`
    - **Description**: Updates a user's profile. All the keys are optional. If a key is not provided, it is not used in the update. The ID of the user to be updated must be provided.

    The JSON object represents the user's updated profile details.
    - **`id`**: The ID of the user.
    - **`first_name`**: The first name of the user.
    - **`last_name`**: The last name of the user.
    - **`email`**: The email of the user.
    - **`phone_number`**: The phone number of the user.
    - **`address`**: The address of the user.
    - **`city`**: The city of the user.
    - **`state`**: The state of the user.
    - **`country`**: The country of the user.
    - **`pin_code`**: The zip code of the user.
    - **`date_of_birth`**: The date of birth of the user.
    - **`password`**: The password of the user.

    Request Payload:
    ```sh
    {
        "id": 1,
        "first_name": "First Name",
        "last_name": "Last Name",
        "email": "user_email",
        "phone_number": 0123456789,
        "address": "user_address",
        "city": "user_city",
        "state": "user_state",
        "country": "user_country",
        "pin_code": 10001,
        "date_of_birth": "1990-05-15",
        "password": "user_password"
    }
    ```

13. #### `POST /user/update_cart/{user_id}`
    **Description**: Updates the user's cart.
    - **`user_id`**: The ID of the user.

    The JSON object represents the updated cart.
    - **`cart`**: The updated cart. The keys are product IDs and the values are the quantities of the products.

    Request Payload:
    ```sh
    {
        "cart": {"5": 4, "4": 5}
    }
    ```
