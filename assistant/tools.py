"""Tools exposed to the voice agent.

The voice platform reads TOOL_DEFINITIONS to know what it can call, then sends
tool calls to our webhook (see server.py). Each tool returns a JSON-serialisable
dict that the voice agent turns into a spoken answer.
"""
from dataclasses import dataclass
from typing import Callable

from assistant.faq import answer_faq


@dataclass
class Tool:
    name: str
    description: str
    parameters: dict
    fn: Callable[..., dict]


TOOLS: dict[str, Tool] = {
    "answer_faq": Tool(
        name="answer_faq",
        description="Answer a caller's question about the restaurant (hours, reservations, parking, menu) from the FAQ.",
        parameters={
            "type": "object",
            "properties": {"question": {"type": "string", "description": "The caller's question."}},
            "required": ["question"],
        },
        fn=answer_faq,
    ),
}

TOOL_DEFINITIONS = [
    {"name": t.name, "description": t.description, "parameters": t.parameters} for t in TOOLS.values()
]
