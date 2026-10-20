"""Local test double for page objects and API tests; no external services."""

import json
from http.server import BaseHTTPRequestHandler


class DemoHandler(BaseHTTPRequestHandler):
    def log_message(self, *args):
        pass

    def respond(self, status, body, content_type="application/json"):
        encoded = body.encode()
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)

    def do_GET(self):
        if self.path == "/health":
            self.respond(200, '{"status":"ok"}')
        elif self.path == "/api/users":
            self.respond(200, '[]')
        elif self.path == "/api/protected":
            self.respond(401, '{"error":"unauthorized"}')
        elif self.path.startswith("/dashboard"):
            self.respond(200, '''<html><body><div class="user-avatar">Test user</div>
                <nav class="nav-menu">Dashboard</nav><input type="search">
                <div class="stat-card">Test statistics</div><button id="logout">Logout</button>
                </body></html>''', "text/html")
        elif self.path.startswith("/reset"):
            self.respond(200, "<html><body>Reset test form</body></html>", "text/html")
        else:
            self.respond(200, '''<html><body><form novalidate><input id="email">
                <input id="password" type="password"><button type="submit">Log in</button></form>
                <div class="error-message" style="display:none"></div>
                <a href="/reset">Forgot password?</a><script>
                document.querySelector('form').onsubmit=async e=>{e.preventDefault();
                let r=await fetch('/login',{method:'POST',headers:{'Content-Type':'application/json'},
                body:JSON.stringify({email:document.querySelector('#email').value,
                password:document.querySelector('#password').value})});
                if(r.ok){location.href='/dashboard'}else{let d=document.querySelector('.error-message');
                d.textContent='Invalid credentials';d.style.display='block'}};
                </script></body></html>''', "text/html")

    def do_POST(self):
        body = json.loads(self.rfile.read(int(self.headers.get("Content-Length", 0))) or b"{}")
        if self.path == "/login":
            valid = body.get("email") == "test@example.com" and body.get("password") == "password123"
            self.respond(200 if valid else 401, '{}')
        elif self.path == "/api/users":
            self.respond(201, json.dumps({"id": 1, **body}))
        else:
            self.respond(404, '{}')
