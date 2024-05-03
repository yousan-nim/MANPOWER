# MANPOWER BACK-ENDS WORKSHOP
This is workshop backend for SDP team from Manpower. 

## Tasks
- [x] Create project using Python. 
- [x] Load file .csv in to Mongodb. [Example File](https://drive.google.com/file/d/1RTf4RDgoH73LLnfXCz5WAm6qB_CowSxH/view?usp=share_link)
- [x] Build API for  CREAT READ UPDATE and DELTE data.
- [x] Using JWT Authentication.
- [x] Use Swagger for create AIP Document.
- [x] Push souce code to Github.
- [x] Deploy Project with Docker file.

## Mongodb Security (Network Access)
- [x] 0.0.0.0/0 all,=.

## Project Installation DONE!.
- [x] makemigrations.
- [x] migrate.
- [x] createsuperuser.

## Installation on your device.
```
git clone https://github.com/IZZARA-URA/MANPOWER.git
```

```
docker build -t manpower .
docker run -p 8000:8000 manpower 
```
Done...

## API.
1. manpower (main tasks) => Superuser only
  - /manpower/get-all
  - /manpower/post-data/
  - /manpower/get-data/{id}
  - /manpower/patch-all/{id}
  - /manpowerdelete-data/{id}

2. users (options) => mycustion users
  - /users/login
  - /users/logout
  - /users/register
  - /users/token
  - /users/token/refresh






