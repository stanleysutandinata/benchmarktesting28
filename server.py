"""Webhook the voice platform calls.

GET  /tools      -> tool definitions
POST /tool-call  -> {"name": ..., "arguments": {...}} -> tool result
"""
import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

from assistant.handler import handle_tool_call
from assistant.tools import TOOL_DEFINITIONS


class Webhook(BaseHTTPRequestHandler):
    def _send(self, status: int, body: dict) -> None:
        payload = json.dumps(body).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def do_GET(self):
        if self.path == "/tools":
            return self._send(200, {"tools": TOOL_DEFINITIONS})
        self._send(404, {"error": "not found"})

    def do_POST(self):
        if self.path != "/tool-call":
            return self._send(404, {"error": "not found"})
        length = int(self.headers.get("Content-Length", 0))
        call = json.loads(self.rfile.read(length) or b"{}")
        self._send(200, handle_tool_call(call.get("name", ""), call.get("arguments", {})))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8080"))
    print(f"Webhook listening on :{port}")
    HTTPServer(("", port), Webhook).serve_forever()
