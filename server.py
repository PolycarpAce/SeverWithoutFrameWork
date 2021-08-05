#Challange Creating sever without using a framework

def app(environ, start_response):
    data = "Hello world!, I made it"
    data = data.encode("utf-8")
    start_response(
        f"200 OK", [
            ("Content-Type", "text/plain"),
            ("Content-Length", str(len(data)))
        ]
    )
    return iter([data])