# Product Backend Code

## Overview

The Django Product Management API is designed for building REST APIs to manage items and categories within a product. It facilitates the creation, updating, and deletion of items while also providing features for applying filters to enhance the visibility of items.

## Table of Contents

- ## Installation

  1. **Set Up Virtual Environment**

     Create a virtual environment to isolate project dependencies. Navigate to your project folder in the terminal and run:

     ```bash
     python -m venv venv
     ```

     Activate the virtual environment:

     - On Windows:

       ```bash
       venv\Scripts\activate
       ```

     - On Unix or MacOS:

       ```bash
       source venv/bin/activate
       ```

  2. **Install Requirements**

     While inside the virtual environment, install the requirements using pip:

     ```bash
     pip install -r requirements.txt
     ```

  3. **Configuartions**

    Add the required Database configurations in the Settings.py file

  3. **Run Initial Migrations**

     Run the initial database migrations to set up the database:

     ```bash
     python manage.py makemigrations
     ```

     ```bash
     python manage.py migrate
     ```

  4. **Run the Development Server**

     Start the development server to see your Django project in action:

     ```bash
     python manage.py runserver
     ```

     By default, the development server will be available at `http://localhost:8000/`.

- ## Unit Testing

  1. **Run the Unit Tests**

     Move to the Backend directory

     Run the following command for the execution of the unit tests:

     ```bash
     python manage.py test products
     ```

     The tests are in the products directory (path: Backend\products\tests.py)

- ## API Documentation

   - The API documentation can be found in the repo as a Postman collection (Product-collection).

   - The API documentation can be found at https://documenter.getpostman.com/view/32908544/2sA2r3b6pG#3e4fa798-fe6c-4548-ad4a-e3c3bd53f1be

   - The Postman collection is also available in the repo under the name Product_Collection.

- ## Deployment

   - The Backend is deployed on AWS EC2, and the Database (PostgreSQL) is deployed on AWS RDS.
   - The links for the API endpoints deployed on EC2 are available as part of the API documentation.

1. Clone the repository:

   ```bash
   git clone https://github.com/Vishnu-Kandati/Application-Backend-Code.git
