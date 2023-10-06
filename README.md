# KONG API Integration to Python File Upload process based on the given task from [Original ReadMe](Original.md)

## Clone Repository
```
git clone https://github.com/johnroworld/KONG-PYTHON.git
```

## Installation

Go to root directory of the project and run:
```
docker-compose build && docker-compose up -d
```

Note: KONG API Gateway will listen to port 8000
and Python will listen to port 5000

## Run API REST

API Endpoints: 
```
1.) Upload file - http://127.0.0.1:8000/upload-service

(POST multipart):
{
    "input": [file]
}

2.) Retrieve file - http://127.0.0.1:8000/upload-service/<filename>
you will be redirected to CDN URL of the uploaded file
```

## Through browser

Open KONG-CDN/upload-service.html from any browser
```
1.) Upload file - http://127.0.0.1:8000/upload-service
    Choose any file to upload and click submit. You will see the CND URL after the upload process

2.) Retrieve file - http://127.0.0.1:8000/upload-service/<filename>
you will be redirected to CDN URL of the uploaded file
```

## Done tasks

1.) CDN Integration

2.) Asset Upload and Retrieval


## Added libraries/tools:
1. Flask/PYTHON
2. Docker
3. KONG

