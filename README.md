# PyReqView

A simple Python webapp to view request data (method, URL arguments, headers, and body data) in a tabular format.

## Setup

### Flask configuration

|Environment Variable|Description|
|---|---|
|`FLASK_HOST`|Change the host address (defaults to `localhost`)|
|`FLASK_PORT`|Change the port that Flask listens on (defaults to `5000`)|

### Python

Run `python server.py` from the root directory. Environment variables are optional.

```
$ FLASK_HOST=newFlaskHostAddress
$ FLASK_PORT=2222
```

```
$ python server.py
```

### Docker

Build the image from the root directory.

```
$ docker build -t pyreqview .
```

Run the image. Environment variables are optional.

```
$ docker run -e FLASK_HOST=newFlaskHostAddress -e FLASK_POST=2222 -p 2222:2222 pyreqview
```

```
$ docker run -e FLASK_HOST=0.0.0.0 -p 5000:5000 pyreqview
```

## Usage
Send a request to `/request` with your browser or CLI tool like [`curl`](https://curl.se/). The path accepts `DELETE`, `GET`, `PATCH`, `POST`, and `PUT` methods.

Navigate to the index page (`/`).