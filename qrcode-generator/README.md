## Run project (local)
1. Run db container
Go to the root directory where docker-compose.yml locates.
```
docker-compose up -d
```

2. Run the project
```
cd qrcode-generator
python manage.py runserver
```

3. Call from browser
Login as admin user.
http://127.0.0.1:8000/users/
http://127.0.0.1:8000/groups/
Authenticated

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

## Direct access to DB container

