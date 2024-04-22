
## Installation

1. Clone the repository:
   
   git clone  https://github.com/pratdub/Assignment-Backend.git
  

2. Navigate to the project directory:
  
   cd Assignment-Backend
  

3. Install dependencies:
   
   pip install -r requirements.txt
   

4. Apply migrations:
   
   python manage.py migrate
  

## Usage

1. Start the development server:
   
   python manage.py runserver
  

2. Access the application in your browser at `http://localhost:8000/`.

## API Endpoints

- `/api/register/` - POST endpoint for user registration.
- `/api/login/` - POST endpoint for user login and JWT token generation.
- *Add other endpoints as applicable.*

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

