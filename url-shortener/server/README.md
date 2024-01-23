## setup server
1. Install dependencies
```
poetry init
```


## run project (dev)
1. Activate virtual environment
2. Run the server
```
cd url-shortener\server\src
uvicorn --factory app:main --host 0.0.0.0 --port 8000
```
or
From VSCode Run > Python: url-shortener


## call APIs (dev)
1. Run server (ref : run project (dev))
2. From rest client tool (e.g. postman), call the API
method : POST
url : http://127.0.0.1:8080//service/url-shortener
body : GraphQL
mutation ShortenUrl {
	shortenUrl( originalUrl: "https://url-shortener/services/123456789/asdfghjkl")
	{
		shortUrl,
        originalUrl
	}
}

Sample response
{
    "data": {
        "shortenUrl": {
            "shortUrl": "true",
            "originalUrl": "https://url-shortener/services/123456789/asdfghjkl"
        }
    }
}


## Challenge info
https://codingchallenges.fyi/challenges/challenge-url-shortener/
