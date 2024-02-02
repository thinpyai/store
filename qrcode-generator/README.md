## Run project (local)

1. Run the project
```
cd qrcode-generator
python manage.py runserver
```

2. Call from browser
Login as admin user.
http://127.0.0.1:8000/users/
http://localhost:8000/api/generate/?data=YourDataHere


## Reference
https://www.django-rest-framework.org/tutorial/quickstart/

## Challenge
https://codingchallenges.fyi/challenges/challenge-qr-generator

## DB Migration
```
python manage.py makemigrations
python manage.py migrate
```
