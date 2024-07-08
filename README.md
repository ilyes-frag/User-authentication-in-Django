# **Project Structure**

This project implements user authentication using the Django REST Framework. It includes three main files for handling the views, URLs, and serializers: `views.py`, `urls.py`, and `serializers.py`.

## **Views**

The `views.py` file contains the view functions that handle the logic for user authentication, including login, signup, and token validation.

- **Login View**: Authenticates a user and returns an authentication token.
- **Signup View**: Registers a new user and generates an authentication token.
- **Token Test View**: Verifies the validity of an authentication token.

These views use the Django REST Framework's decorators and classes to manage requests, responses, authentication, and permissions.

## **URLs**

The `urls.py` file defines the URL patterns that map to the view functions.

- **Login Endpoint**:
  - **URL**: `/login`
  - **Description**: Maps to the login view function.
  
- **Signup Endpoint**:
  - **URL**: `/signup`
  - **Description**: Maps to the signup view function.
  
- **Token Test Endpoint**:
  - **URL**: `/test_token`
  - **Description**: Maps to the `test_token` view function.

These URL patterns ensure that HTTP requests are routed to the correct view functions for processing.

## **Serializers**

The `serializers.py` file defines the `UserSerializer` which is used to serialize and deserialize `User` model instances.

- **UserSerializer**:
  - **Model**: Uses Django's built-in `User` model.
  - **Fields**: Includes `id`, `username`, `password`, and `email`.

The `UserSerializer` converts the `User` model data to and from JSON format, facilitating the handling of user data in the view functions.

## **Summary**

- **Views**: Implement the logic for user authentication and token validation.
- **URLs**: Define the URL patterns that route requests to the appropriate views.
- **Serializers**: Convert `User` model instances to and from JSON format for easy handling of user data.

By structuring the project this way, the application ensures a clear separation of concerns, making it easier to manage and extend the authentication functionality.
