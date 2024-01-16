# setup server
1. Install dependencies
```
poetry init
```

# run project (development)
1. Activate virtual environment

2. Run the server
```
cd url-shortener\server\src
uvicorn --factory app:main --host 0.0.0.0 --port 8000
```