import os
from http.server import BaseHTTPRequestHandler, HTTPServer

name = os.getenv("STUDENT_NAME", "Nurasyl")
surname = os.getenv("STUDENT_SURNAME", "Zhapsarbek")
group = os.getenv("STUDENT_GROUP", "IT2-2308")
student_id = os.getenv("STUDENT_ID", "37841")

message = f"""================================
DevOps Student Application
================================
Name: {name}
Surname: {surname}
Group: {group}
Student ID: {student_id}

Application is running successfully!
"""

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = message.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

if __name__ == "__main__":
    print(message, flush=True)
    HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
