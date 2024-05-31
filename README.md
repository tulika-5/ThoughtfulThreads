

# ThoughtfulThreads

ThoughtfulThreads is a Django-based blog website where users can read blog posts from various categories such as politics, science and technology, entertainment, and sports. Users can register as either writers or readers, login to save their favorite blogs to their profile, and access exclusive features.

## Features

- User registration and authentication
  - Register as a writer or reader
  - Login and logout functionality
- Blog posts categorized into different topics
  - Politics
  - Science and Technology
  - Entertainment
  - Sports
- Save blog posts to your profile
  - Heart (like) a blog post
  - Mark a blog post to read later
- Admin interface for managing posts and categories

## Getting Started

These instructions will help you set up and run the project on your local machine for development and testing purposes.

### Prerequisites

- Python 3.x
- Django 3.x or later
- Pip (Python package installer)

### Installation

1. Clone the repository

   ```bash
   git clone https://github.com/yourusername/thoughtfulthreads.git
   cd thoughtfulthreads
   ```

2. Create and activate a virtual environment

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages

   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations to set up the database

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create a superuser for accessing the admin interface

   ```bash
   python manage.py createsuperuser
   ```

6. Collect static files

   ```bash
   python manage.py collectstatic
   ```

7. Run the development server

   ```bash
   python manage.py runserver
   ```

   Open your web browser and navigate to `http://127.0.0.1:8000/`.

## Usage

### Home Page

The home page displays a list of blog posts categorized into different topics. Users can read blog posts without logging in.

### Registration and Login

- To access the registration page, go to `http://127.0.0.1:8000/register/`.
- To access the login page, go to `http://127.0.0.1:8000/login/`.

### Admin Interface

To access the admin interface, go to `http://127.0.0.1:8000/admin/` and log in with the superuser credentials created earlier.

### User Profiles

Registered users can save blog posts to their profile by liking or marking them to read later.


## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- Django documentation and tutorials
- Stack Overflow community for troubleshooting and tips

