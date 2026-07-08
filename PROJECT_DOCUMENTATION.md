# Project Documentation

## Project Title
Fatima’s Restaurant Web Application

## Submitted By
[Your Name]

## Course/Module
Django Web Development Project

## Date
July 2026

---

## 1. Introduction
This project is a full-featured Django web application for a restaurant business. It provides a modern online platform where visitors can browse restaurant products, search for items, contact the restaurant, create accounts, and log in securely. The system also includes an admin dashboard for managing products and customer messages.

The application is built using the Django framework, SQLite database, Bootstrap for the front-end, and Pillow for image handling. It demonstrates how a real-world web application can be developed using Django’s Model-View-Template architecture.

---

## 2. Project Overview
The Fatima’s Restaurant Web Application is designed to provide an online presence for a restaurant. It allows users to:
- View the homepage with attractive restaurant imagery
- Browse products and menu items
- Search for products by name, description, or category
- Contact the restaurant through a contact form
- Register and log in to the platform
- Access restricted product pages after authentication

The project uses Django’s built-in authentication system and includes message notifications for successful or failed actions.

---

## 3. Objectives of the Project
The main objectives of this project are:
1. To design and develop a dynamic web application using Django.
2. To create a user-friendly interface for restaurant product presentation.
3. To implement a contact form for customer communication.
4. To provide authentication features such as login, signup, and logout.
5. To manage data through Django models and the admin panel.
6. To demonstrate practical web development skills such as routing, templates, forms, and database integration.

---

## 4. Problem Statement
Many small businesses, including restaurants, need an online platform to display their products and services effectively. Without a website, they may miss opportunities to attract customers, present their menu, and collect customer inquiries.

This project addresses that problem by providing a simple, attractive, and functional website where restaurant products can be displayed online and users can easily get in touch with the business.

---

## 5. Scope of the Project
The scope of this project includes:
- Home page with promotional images and featured products
- Product listing page with pagination
- Search functionality for products
- About page for business information
- Contact page with a working contact form
- User registration and login
- Logout functionality
- Admin management for products and contact messages

The project does not include online payment, delivery tracking, or a full e-commerce system.

---

## 6. Functional Requirements
The system includes the following functional requirements:

### User Functions
- Users can visit the home page.
- Users can view information about the restaurant.
- Users can browse all products.
- Users can use the search bar to find products.
- Users can submit contact messages.
- Users can create a new account.
- Users can log in to the application.
- Users can log out of the application.

### Admin Functions
- Admin can manage products through Django admin.
- Admin can view customer contact messages.
- Admin can mark messages as read.

---

## 7. Non-Functional Requirements
The project also includes the following non-functional requirements:
- User-friendly interface
- Responsive design using Bootstrap
- Security through Django authentication and CSRF protection
- Fast and simple navigation
- Easy maintenance through modular app structure
- Scalability for future enhancements

---

## 8. Tools and Technologies Used
The project was developed using the following technologies:

### Front-End
- HTML
- CSS
- Bootstrap 5
- JavaScript (for Bootstrap components)

### Back-End
- Python
- Django Framework

### Database
- SQLite

### Other Tools
- Pillow (for image uploads)
- Python-dotenv (for environment configuration)

---

## 9. System Architecture
The application follows the Django MVC/MVT architecture:
- Model: Defines the structure of the database tables.
- View: Handles business logic and requests.
- Template: Displays content to the user.
- URL Conf: Maps paths to views.

The project consists of:
- One main Django project: project1
- One application: test1

This ensures the project is modular, maintainable, and easy to extend.

---

## 10. Project Structure
The project folder contains the following main components:

- manage.py: Used to run the Django project
- project1/: Main project settings and URL configuration
- test1/: Main application containing models, views, templates, forms, and static files
- media/: Stores uploaded product images
- db.sqlite3: SQLite database file
- requirements.txt: Project dependencies

---

## 11. Application Modules
### 11.1 Home Module
The home page displays the restaurant’s image carousel and available products. It provides a visually appealing landing page for users.

### 11.2 Product Module
The product page lists products with details such as name, category, ID, description, and image. Products are paginated to make browsing easier.

### 11.3 Search Module
The search feature enables visitors to find products by entering keywords related to the product name, description, or category.

### 11.4 Contact Module
The contact module contains a form where users can submit their name, email, and message. The data is stored in the database and can be viewed from the admin panel.

### 11.5 Authentication Module
This module allows users to sign up, log in, and log out securely. It uses Django’s built-in authentication system.

### 11.6 About Module
The about page presents information about the restaurant, its values, and its mission.

---

## 12. Database Design
The application uses SQLite and contains two main models.

### 12.1 Product Model
The Product model stores product information, including:
- product_id
- product_name
- product_description
- product_category
- product_img

This model is used to display products on the website.

### 12.2 ContactMessage Model
The ContactMessage model stores contact form submissions, including:
- name
- email
- message
- created_at
- is_read

This helps the restaurant manage customer inquiries.

---

## 13. Forms Used
The project uses a Django ModelForm for the contact page.

### ContactForm
The ContactForm collects:
- Name
- Email
- Message

It includes Bootstrap styling and validation rules.

---

## 14. Views Implemented
The following views are implemented in the application:

### loginuser
Handles user login with authentication and displays error messages for invalid credentials.

### signupuser
Handles new user registration and automatically logs the user in after successful signup.

### logoutuser
Logs the user out and shows a success message.

### findproduct
Searches for products based on the user’s input and displays matching results.

### product
Displays all products with pagination.

### home
Displays the homepage with product cards.

### contact
Handles the contact form submission and displays success messages.

### about
Displays the about page.

---

## 15. URL Routing
The project uses Django URL patterns for navigation:
- / - Home page
- /contact/ - Contact page
- /product/ - Product page
- /about/ - About page
- /loginuser/ - Login page
- /signupuser/ - Signup page
- /logout/ - Logout page
- /findproduct/ - Search results page
- /admin/ - Django admin panel

---

## 16. User Interface and Templates
The project uses separate HTML templates for each page:
- home.html
- product.html
- contact.html
- about.html
- loginuser.html
- signupuser.html
- navbar.html
- footer.html

The templates are designed with Bootstrap to make the website visually appealing and easy to use.

---

## 17. Installation and Setup
To run this project locally, follow these steps:

1. Open the project folder.
2. Activate the virtual environment.
3. Install dependencies using:
   pip install -r requirements.txt
4. Run database migrations:
   python manage.py migrate
5. Start the development server:
   python manage.py runserver

You can then open the application in your browser at:
http://127.0.0.1:8000/

---

## 18. How to Use the Application
### Visiting the Website
Users can open the home page and browse the restaurant’s products.

### Searching Products
Enter a keyword in the search bar to find products based on name, category, or description.

### Contacting the Restaurant
Go to the contact page and fill out the form to send a message.

### Registering an Account
A new user can click Register and create an account.

### Logging In
Existing users can log in using their username and password.

### Admin Panel
Access the admin panel at /admin/ to manage products and view messages.

---

## 19. Security Features
The application includes basic security features such as:
- Django authentication system
- CSRF protection
- Secure form handling
- Protected product page with login requirement

---

## 20. Challenges Encountered
During the development of this project, some challenges included:
- Setting up Django templates and navigation correctly
- Managing image uploads with the ImageField model
- Ensuring forms validate properly
- Implementing search functionality effectively
- Organizing the templates and static files for a clean design

These challenges were resolved by using Django’s built-in features and proper project structure.

---

## 21. Limitations of the Project
Although the project is functional, it has some limitations:
- It does not include real online payment functionality.
- It does not support order tracking.
- It does not include a full inventory or delivery management system.
- It uses SQLite, which is suitable for development but may not be ideal for large-scale deployment.

---

## 22. Future Enhancements
The project can be improved in the future by adding:
- Online ordering and checkout
- Payment gateway integration
- Order tracking system
- User profile management
- Admin analytics dashboard
- Database migration to PostgreSQL for production
- Mobile app support

---

## 23. Conclusion
The Fatima’s Restaurant Web Application is a complete Django-based project that demonstrates essential web development concepts such as models, views, templates, forms, authentication, routing, and database integration. The application is user-friendly, functional, and suitable for demonstrating the capabilities of Django in building real-world web systems.

This project serves as a strong foundation for further development and can be expanded into a larger restaurant management system in the future.

---

## 24. Appendix
### Key Files
- [project1/settings.py](project1/settings.py)
- [project1/urls.py](project1/urls.py)
- [test1/models.py](test1/models.py)
- [test1/views.py](test1/views.py)
- [test1/forms.py](test1/forms.py)
- [test1/templates/test1/home.html](test1/templates/test1/home.html)
- [test1/templates/test1/product.html](test1/templates/test1/product.html)
- [test1/templates/test1/contact.html](test1/templates/test1/contact.html)

### Dependencies
- Django==6.0.6
- Pillow==12.2.0
- python-dotenv==1.2.2
