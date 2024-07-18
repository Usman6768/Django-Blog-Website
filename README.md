# Django Blog Website

This is a Django-based blog website project where users can create, edit, and delete blog posts. It includes features such as user authentication, admin panel integration, and basic CRUD operations for managing blog posts.

# Features

- **User Authentication:** Users can register, log in, and log out.
- **Admin Panel:** Admins have access to manage users and blog posts.
- **CRUD Operations:** Users can create, read, update, and delete blog posts.
- **Responsive Design:** Basic styling with Bootstrap for responsiveness.

# Installation

To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Usman6768/Django-Blog-Website.git
   ```
2. Navigate into the project directory:
   ```bash
   cd Django-Blog-Website
   ```
3. Create a virtual environment:
   ```bash
   python -m venv env
   ```
4. Activate the virtual environment:
   - On Windows:
     ```bash
     env\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source env/bin/activate
     ```
5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
6. Apply database migrations:
   ```bash
   python manage.py migrate
   ```
7. Create a superuser (admin account):
   ```bash
   python manage.py createsuperuser
   ```
8. Start the development server:
   ```bash
   python manage.py runserver
   ```
9. Open your web browser and go to `http://127.0.0.1:8000/` to view the blog website.

## Usage

- **Admin Access:** Visit `http://127.0.0.1:8000/admin/` to access the admin panel and manage users and blog posts.
- **Creating Posts:** Logged-in users can create new blog posts via the "New Post" button.
- **Editing/Deleting Posts:** Users can edit or delete their own posts via the post detail view.

