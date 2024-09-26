
def app(environ, start_response):
    request_uri = environ.get('REQUEST_URI')

    if request_uri == "/new-match":
        status = "200 OK"
        headers = [('Content-type', 'text/html; charset=utf-8')]
        start_response(status, headers)
        with open("src/views/pages/index.html", "rb") as file:
            return [file.read()]

    elif request_uri.startswith("/static/"):
        # Обработка запросов к статическим файлам
        status = "200 OK"
        content_type = [('Content-type', 'text/css; charset=utf-8')]
        start_response(status, content_type)
        with open("src/views/static/css/styles.css", "rb") as file:
            return [file.read()]


if __name__ == '__main__':
    from waitress import serve

    serve(app, host='127.0.0.1', port='8000')
