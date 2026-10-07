# restaurant-assistant

The phone assistant for Harbor Street Kitchen. Callers talk to a hosted voice agent;
when it needs facts, it calls this webhook with a tool call and speaks the result.

## Layout

- `restaurant.json`: name, address, coordinates and timezone of the restaurant.
- `faq.json`: the FAQ the assistant answers from.
- `assistant/tools.py`: the tools the voice agent can call (`TOOL_DEFINITIONS`) and
  the functions behind them. Add new capabilities here.
- `assistant/handler.py`: `handle_tool_call(name, arguments)`, the single entry point.
- `assistant/config.py`: loads config. `today()` returns the restaurant's local date;
  set `ASSISTANT_TODAY=YYYY-MM-DD` to pin it for tests and call replays.
- `server.py`: the webhook (`GET /tools`, `POST /tool-call`).

## Run

```bash
pip install -r requirements-dev.txt
pytest
python server.py   # listens on :8080
```

Try a call:

```bash
curl -s localhost:8080/tool-call -d '{"name":"answer_faq","arguments":{"question":"Do you take reservations?"}}'
```

Tool results are JSON. Keep them short and factual; the voice agent reads them aloud.
