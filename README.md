# Library-Management-System
Markdown

# 📚 Online Library Management System

A robust Django-based web application designed for library administrators to manage authors, books, and borrowing records. This project features a modern UI built with Tailwind CSS and supports data export to Excel.

## 🚀 Features

- **Management Dashboard**: Admins can add and view Authors, Books, and Borrowing Records.
- **Form Validation**: Custom email validation and date pickers for data integrity.
- **Pagination**: Built-in Django pagination (5 records per page) for smooth navigation.
- **Excel Export**: Export all library data into a multi-sheet Excel file (.xlsx) using `openpyxl`.
- **Modern UI**: Fully responsive interface styled with **Tailwind CSS**.
- **Class-Based Views**: Clean, maintainable code following Django best practices.

## 🛠️ Tech Stack

- **Backend**: Python 3.x, Django 5.x / 6.x
- **Frontend**: Tailwind CSS (via CDN), HTML5
- **Database**: SQLite (Default)
- **Libraries**: `openpyxl` (Excel generation)

## 📋 Prerequisites

Ensure you have Python installed. You can check by running:
```bash
python --version
⚙️ Installation & Setup
Clone the repository:

Bash

git clone <your-repository-link>
cd library-management-system
Create a virtual environment:

Bash

python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
Install dependencies:

Bash

pip install django openpyxl
Apply Migrations:

Bash

python manage.py makemigrations library
python manage.py migrate
Create a Superuser (to access the Django admin):

Bash

python manage.py createsuperuser
Run the Server:

Bash

python manage.py runserver
Access the application at: http://127.0.0.1:8000/authors/

📁 Project Structure
library/models.py: Database schema for Author, Book, and BorrowRecord.

library/forms.py: Tailwind-styled forms with custom validation logic.

library/views.py: Logic for data handling, pagination, and Excel export.

templates/library/: Reusable HTML templates using Django template inheritance.

📖 Usage Guide
Authors: Start by adding an author via the "Add Author" button.

Books: Add books and assign them to an existing author from the dropdown.

Borrowing: Record user borrowing details by selecting a book and dates.

Export: Click "Export Excel" on any list page to download the full library report.



