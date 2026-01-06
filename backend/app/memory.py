sessions = {}

def get_memory(session_id: str):
    if session_id not in sessions:
        sessions[session_id] = {
            "name": None,
            "country": None
        }
    return sessions[session_id]
