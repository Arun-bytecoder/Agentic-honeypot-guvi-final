def generate_reply(turn: int) -> str:
    """
    Turn-based agentic behavior.
    Prevents repetitive replies while staying human-like.
    """

    if turn == 1:
        return "Why is my account being suspended?"
    elif turn == 2:
        return "I’m really worried, can you explain what happened?"
    elif turn == 3:
        return "What do I need to do to fix this?"
    else:
        return "Please give me some time, I need to understand this properly."
