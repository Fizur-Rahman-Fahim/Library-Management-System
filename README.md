# Library Management System

A modern library management system built with Django that allows users to browse, borrow, and return books online. The system includes user authentication, balance management, and a book categorization system.

## Features

- User Authentication (Register, Login, Logout)
- Book Management
  - Browse books by category
  - Search functionality
  - Book details with cover images
- User Profile Management
  - View borrowed books
  - Balance management
  - Deposit money
- Admin Interface
  - Manage books, categories, and users
  - Track borrowed books
  - Monitor user balances

## Technologies Used

- Python 3.12
- Django 5.1.1
- Bootstrap 5.3
- Font Awesome 6.0
- SQLite (Development) / PostgreSQL (Production)

## Installation

1. Clone the repository
```bash
git clone https://github.com/Fizur-Rahman-Fahim/Library-Management-System.git
cd library_management
```

2. Create a virtual environment and activate it
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Apply migrations
```bash
python manage.py migrate
```

5. Create a superuser
```bash
python manage.py createsuperuser
```

6. Run the development server
```bash
python manage.py runserver
```

## Environment Variables

Create a `.env` file in the root directory and add the following variables:
```
DEBUG=False
SECRET_KEY=your-secret-key
DATABASE_URL=your-database-url
ALLOWED_HOSTS=your-domain.com,www.your-domain.com
```

## Deployment

This application is configured for deployment on Render. Follow these steps:

1. Create a new Web Service on Render
2. Connect your GitHub repository
3. Set the following:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn library_management.wsgi:application`
4. Add environment variables in Render dashboard

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Screenshots

[screenshots are here]
