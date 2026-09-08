def detect_redundancy(logs):
    messages = []
    redundant_events = []
    for log in logs:
        message = (
            log["message"].lower().strip()
        )

        if message in messages:
            redundant_events.append(log)

        messages.append(message)

    return {
        "redundancy_detected": (
            len(redundant_events) > 0
        ),
        "redundant_events": (
            redundant_events
        )
    }