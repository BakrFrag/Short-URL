# Short-URL
Short URL services , instead of using large links you can use short link , using short link you can redirected to original link 

## Entities & Database Diagram 

https://drawsql.app/development-9/diagrams/shorturl

##  How To Operate Locally 
- machine with Python 3.8.10 and pip3 package manager 
- clone project from github 
- type `pipenv shell`
- install dependancies 
- type `pipenv install -r requirements.txt`
- change to app directory `cd ShortUrl`
- map django orm to database `python manage.py makemigrations`
- apply orm migrations `python manage.py migrate `
- create superuser for admin panal `python manage.py createsuperuser` go with prompts 
- start development server `python manage.py runserver 0.0.0.0:8000`

## Request & Response Cycle 

- postman collection for various request and response in different testcases 
- https://www.getpostman.com/collections/861c0bfb638bf4f528ca

## URLs for services

- for admin panel `http://127.0.0.1:8000/admin/` login with superuser credentials 
- add client from admin panal
- create ClientApiKey from ClientApiKey Model in admin panal 
- the key appears once in alter message save it for further use 
- POST request with url in request body and set `Authorization : Api-Key <API-KEY>` generated from admin panal 
- url `http://127.0.0.1:8000/api/short/v1/` will generate short code if not exists if exists it will return already short code in database 
- GET request with short code parsed as url variable and set `Authorization : Api-Key <API-KEY>` generated from admin panal 
- then you will be redirected to original url if short code in database otherwise will return 404 not found 
- for various request & response in different testcases 
   - load postman collection in you postman app via https://www.getpostman.com/collections/861c0bfb638bf4f528ca

# Project Build

- this project build using Python 3.8.10
- python Django for web applications
- machine with ubuntu 20.04
