# codemonk-backend-internship-assignment
This project is developed using Django and Django Rest Framework as an internship assignment. This project uses Celery for asynchronous tasks like sending email, Redis as the message broker and Swagger for a clean and interactive API documentation UI.

## Features

The features that are implemented are:
* API Creation
* Partial Update of Records with Validation
* User Signup with Email Verification
* Advanced Filtering
* Pagination
* File Upload
* Swagger UI for API Documentation
* Testing

## Installation

1. **Clone the repository:**
`git clone https://github.com/Raghav1909/codemonk-backend-internship-assignment.git`

2. **Install pipenv:**
`pip install pipenv`

3. **Install dependencies using pipenv:**
`pipenv install --dev`

4. **Activate the virtual environment:**
`pipenv shell`

5. **Run migrations:**
`cd backend && python manage.py migrate`

6. **Start the Django development server**:
`python manage.py runserver`

8. **In another terminal start the Celery worker:**
`celery -A backend worker -l info`
