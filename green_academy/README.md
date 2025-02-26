# Green Academy API 

## 🗂️Project Overview
The Green Academy API serves as the backbone of Green Academy's online learning platform, facilitating **course management,** **student enrollment,** and **secure data handling.** Built with Django REST Framework, it adheres to RESTful principles while ensuring performance optimisation, robust security, and scalability through caching, pagination, and authentication mechanisms

## 📋Prerequisites
- Python 3.9+
- PostgreSQL (recommended) or SQLite
- pip package manager

## ⚙️Installation & Setup
### 1. Clone the Repository 
```
git clone https://github.com/your-username/green-academy-api.git
cd green-academy-api
```

### 2. Set Up a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your-django-secret-key
DATABASE_URL=postgres://user:password@localhost:5432/green_academy  # Example for PostgreSQL
DEBUG=True
```

### 5. Apply Database Migrations

```bash
python manage.py migrate
```

### 6. Create a Superuser (Admin)

```bash
python manage.py createsuperuser
```

---

## Running the API

```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/`.

---

## 📝Testing

### 1. Run Automated Tests

```bash
python manage.py test
```

### 2. Manual Testing with Tools

- Use **Postman** or **curl** to send HTTP requests.
- Access the browsable API at `http://localhost:8000/api/` after starting the server.

#### Example Requests

**Get All Courses (Paginated):**

```bash
curl http://localhost:8000/api/courses/
```

**Enroll a Student:**

```bash
curl -X POST http://localhost:8000/api/enrollments/ \
  -H "Content-Type: application/json" \
  -d '{"student_id": 1, "course_id": 5}'
```

---

### 3. Type Checking with Mypy

Ensure static type consistency:

```bash
mypy . --ignore-missing-imports
```

---

## 📤Deployment
### 1. Deployment Steps
- Install dependencies on the server:
```
pip install -r requirements.txt
```
- Apply database migrations:
```
python manage.py migrate
```
- Set up environment variables:
```
export SECRET_KEY='your-secret-key'
export DATABASE_URL='your-database-url'
```
- Start the server:
```
gunicorn green_academy.wsgi:application --bind 0.0.0.0:8000
```
### 2. Monitoring and Logging
- **Error Logging:** Configured using Django's built-in logging module.
- **Performance Monitoring:** Monitored via New Relic or Datadog.
- **Uptime Checks:** Implemented using Pingdom.

## 🌟Key Features

### Pagination

- Endpoints returning lists (e.g., `/api/courses/`) use **page-based pagination**.
- Default page size: `10` (configurable via `?page_size=` query parameter).
- Example: `GET /api/courses/?page=2&page_size=5`

### Caching

- **In-memory caching** (Django's `LocMemCache`) is implemented for:
  - Course list endpoints
  - Frequently accessed enrollment data
- Cached data expires after `300 seconds` (5 minutes).

### Security

- **Personal data** (e.g., student names, emails) is:
  - Encrypted at rest
  - Accessed only via secure endpoints
  - GDPR-compliant (right to erasure included)
- Authentication required for write operations (admin/superuser).

---

## 🗃️Project Structure

``` text
.
├── green_academy/              # Django project root
│   ├── courses/                # Courses app (models, views, serializers)
│   ├── enrollments/            # Enrollments app
│   ├── green_academy/          # Root URL routing & Project settings
│   ├── user/                   # User app
│   ├── .gitignore              # Git ignored (IDE, environment...)
│   ├── manage.py               # Main
│   └── README.md               # Project Readme
├── API_DESIGN.md               # Endpoint documentation
├── requirements.txt            # Dependencies
└── README.md                   # This file
```

---

## 📃API Design Documentation

Refer to [API_DESIGN.md](../API_DESIGN.md) for detailed endpoint specifications, request/response examples, and status codes.

---

## 🏷️License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## 🤝🏽Contribution Guidelines
- Pull Requests: Always create a PR for changes.
- Code Formatting: Follow PEP 8 standards.
- Testing: Ensure all new features have test coverage.
- Security Checks: Run security tests before deploying.

## 👏🏽Acknoledgments 
- Django & Django REST Framework
- PostgreSQL

