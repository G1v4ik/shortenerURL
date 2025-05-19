# Shortener URL

## for setup

---

- clone repository
- enter "uv sync"
- enter "uv run main.py" to launch the project

## Methods

---

### Post /

The method accepts the URL string for shortening in the request body and returns a response with the code 201.

- INPUT

```URL

URL: 'http://127.0.0.1:8080/urls' 

```

```json

{
    "url_target": "http://blogshistory.ru"
}

```

- OUTPUT

```json

{
  "url_target": "http://blogshistory.ru",
  "url_key": "ju8ld",
  "id": 1
}

```

### Get /

The method takes the identifier of the shortened URL as a parameter and returns a response with the 307 code and the original URL.

- Request

```URL
URL: http://127.0.0.1:8080/urls/ju8ld
```

- Response

```json

{
  "url_key": "ju8ld",
  "url_target": "http://blogshistory.ru",
  "id": 1
}

```
