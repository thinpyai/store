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


## call APIs (dev)
1. Run server (ref : run project (dev))
2. From rest client tool (e.g. postman), call the API
method : POST
url : http://127.0.0.1:8080//service/url-shortener
body : GraphQL
mutation ShortenUrl {
	shortenUrl( longUrl: "https://graphql.org/learn/queries/")
	{
		shortenedUrl,
        longUrl
	}
}

Sample response
{
    "data": {
        "shortenUrl": {
            "shortenedUrl": "true",
            "longUrl": "https://graphql.org/learn/queries/"
        }
    }
}


## Challenge info
https://codingchallenges.fyi/challenges/challenge-url-shortener/
