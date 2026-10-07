from assistant.config import today
from assistant.handler import handle_tool_call
from assistant.tools import TOOL_DEFINITIONS


def test_faq_hours():
    result = handle_tool_call("answer_faq", {"question": "What time do you close tonight?"})
    assert result["found"] is True
    assert "10pm" in result["answer"]


def test_faq_no_match():
    result = handle_tool_call("answer_faq", {"question": "Who won the game?"})
    assert result["found"] is False


def test_unknown_tool():
    assert "error" in handle_tool_call("nope", {})


def test_tool_definitions_have_schemas():
    assert all({"name", "description", "parameters"} <= d.keys() for d in TOOL_DEFINITIONS)


def test_pinned_today(monkeypatch):
    monkeypatch.setenv("ASSISTANT_TODAY", "2026-10-07")
    assert today().isoformat() == "2026-10-07"
