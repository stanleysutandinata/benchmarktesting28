from assistant.tools import TOOLS


def handle_tool_call(name: str, arguments: dict) -> dict:
    """Entry point for tool calls from the voice platform."""
    tool = TOOLS.get(name)
    if tool is None:
        return {"error": f"unknown tool: {name}"}
    try:
        return tool.fn(**arguments)
    except TypeError as e:
        return {"error": f"bad arguments for {name}: {e}"}
