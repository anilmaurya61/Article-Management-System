# Article Management System

## Overview
This project is an **Article Management System** designed for a media company to streamline article creation, review, and publishing. It includes both a web-based interface and a RESTful API for seamless third-party integration.

The system supports three user roles:

1. **Journalist**: Can submit and edit their own articles.
2. **Editor**: Can review, approve, and publish articles.
3. **Admin**: Has full access to manage users and articles.

## Features

### Part 1: Article Submission Form
The frontend includes a two-page article submission form with the following features:

#### Page 1:
- **Title** (Text Field)
- **Subtitle** (Text Field)
- **Article Content** (Text Area)
- **Author Name** (Text Field)
- **Email Address** (Email Field)

#### Page 2:
- **Article Image** (File Upload)
- **Tags** (Checkboxes for predefined tags: Politics, Sports, Tech, etc.)
- **Category** (Dropdown: News, Opinion, Feature, etc.)
- **Publish Date** (Date Field, must be a future date)
- **Agree to Terms** (Checkbox)

#### Custom Validation:
- Title must be at least 10 characters long.
- Publish date must be in the future.
- Email must be in a valid format.
- Terms checkbox must be checked.

#### Pagination:
- Forms are split into two pages with data persistence between pages.

#### Error Handling:
- User-friendly error messages displayed for invalid inputs.

### Part 2: Backend and API

#### Authentication:
- User registration, login, and logout functionality.
- Password reset via email.
- Token Authentication for API access.

#### Authorization:
- Role-based access control using Django’s permission system.

#### CRUD Operations:
- Create, edit, and delete articles.
- Article model fields include title, content, author, image, tags, category, and publish_date.
- Role-based restrictions:
  - Journalists can create and edit their own articles.
  - Editors can approve, reject, or publish articles.
  - Admins can manage articles and users.

#### API Features:
- REST API built with Django Rest Framework (DRF).
- CRUD operations on articles.
- Pagination, search, and filtering (e.g., by category or title).
- Role-based access control for API endpoints.

#### Bonus Features:
- Email notifications for article submission, approval, or rejection.
- Public endpoint for retrieving published articles.

## Project Structure

```plaintext
artical_management_project/
|-- README.md
|-- articles/
|   |-- models.py
|   |-- serializers.py
|   |-- views.py
|   |-- permissions.py
|   |-- urls.py
|
|-- users/
|   |-- models.py
|   |-- serializers.py
|   |-- views.py
|   |-- permissions.py
|   |-- urls.py
|
|-- artical_management_project/
|   |-- settings.py
|   |-- urls.py
|
|-- db.sqlite3
|-- manage.py
|-- media/
|-- static/
|-- templates/
```

## Installation

### Prerequisites
- Python 3.8+
- Django 4.2+
- Django Rest Framework (DRF)

### Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd article_management_project
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run database migrations:
   ```bash
   python manage.py migrate
   ```

4. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

6. Access the application at `http://127.0.0.1:8000`.

## API Endpoints

### Authentication
- `POST /api/register/`: Register a new user.
- `POST /api/login/`: Login and obtain token.
- `POST /api/logout/`: Logout the user.
- `POST /api/password-change/`: Change user password.

### Articles
- `GET /api/articles/`: List all articles (with pagination, search, and filtering).
- `POST /api/articles/create/`: Create a new article.
- `GET /api/articles/<id>/`: Retrieve article details.
- `PUT /api/articles/<id>/`: Update article.
- `DELETE /api/articles/delete/<id>/`: Delete article.


## Validation
- Custom validation for form fields and API requests as described in the feature list.




