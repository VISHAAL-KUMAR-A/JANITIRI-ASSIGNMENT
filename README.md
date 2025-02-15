# REALTIME-CHAT-APPLICATION

This is a real-time chat application built using Django and Django Channels. It allows users to communicate with each other in real-time through a web interface.

## Features
- User Registration
- Login
- Patient and Users details
- Heart rates of the users and patients

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/VISHAAL-KUMAR-A/JANITIRI-ASSIGNMENT.git
   ```
2. Navigate to the project directory:
   ```
   cd janitiriassignment
   ```
3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
4. Install Django:
    ```
    pip install django
    ```
5.Create a virtual Environment:
    ```
    pip install virtualenv
      ```
   ```
      virtualenv venv
   ```
   ```
      python -m venv venv
   ```
    venv\Scripts\activate

4. Run the migrations:
   ```
   python manage.py migrate
   ```
5. Start the development server:
   ```
   python manage.py runserver
   ```

## Usage
- Open your web browser and go to `http://127.0.0.1:8000/api/`.
- for registration `http://127.0.0.1:8000/api/register/`
- here you need to give the information in the content in json format like this
`{
    "name": "John Doe",
    "email": "john@example.com",
    "password": "your_password",
    "role": "USER" or "PATIENT"
}`
- You will receive 200 ok while doing the post request and you will also get a message that the user already exist if they are being registered already
- You can check the credentials in the `http://127.0.0.1:8000/api/login/`
- here you need to give the information as 
`{
"email":"yourEmail",
"password":"your_password"
}` 
- If the email and password are correct then you will get the details of the user otherwise you will receive invalid credentials error
- Here you can add and get the information of the patient `http://127.0.0.1:8000/api/patients/`
- Here you can get the information of the heart rate of the patient `http://127.0.0.1:8000/api/heart-rates/`
## Contributing
Feel free to submit issues or pull requests. Contributions are welcome!

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
