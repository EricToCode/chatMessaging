# chatMessaging

This is a Django app.
It is a messaging app with user login features.

To use app, run the following commands inside the main folder

First initiate redis as backing store using Docker:
docker run -p 6379:6379 -d redis:5

Then start the local server using Django:
python3 manage.py runserver
