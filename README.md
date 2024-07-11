# Application configuration and startup

## 1. Dependency Installation
1. Install poetry
2. Install npm

## 2. Backend app setup
```
cd backend/
poetry install
```

## 3. Frontend app setup
```
cd frontend/
npm install
```

## 5. Run Backend Application
```
cd backend/
uvicorn app:app --host 0.0.0.0 --port 80
```

## 6. Run Frontend Application
> NOTE:  
> Run following commands in a separate terminal.

```
cd frontend/
npm run dev
```

## 7. Interact with Frontend
Go to a broswer and hit this url:<br>
[http://localhost:5173](http://localhost:5173)

## 8. Interact with Backend Application directly

### a. Using Swagger UI
* Go to a broswer and hit this url:<br>
[http://localhost/docs](http://localhost/docs)
* Enter start and end date in the ```/status_count``` endpoint
* Eg: ```2024-07-10T18:30:00```

### b. Using Postman
* Go to Postman and add a new GET request:<br>
* Enter this URL:<br>
http://localhost/status_count?start=2024-07-11T00:00:00&end=2024-07-11T18:30:00
* Customize the start and end date by going into Params section in Postman
