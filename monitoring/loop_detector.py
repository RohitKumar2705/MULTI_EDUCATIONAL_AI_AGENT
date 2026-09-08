def detect_loop(logs):
    agents = [
        log["agent"]
        for log in logs
        
    ]

    repetitions = 0
    for i in range(len(agents) - 1):
        if agents[i] == agents[i+1]:
            repetitions += 1


        if repetitions >= 2:

         return {
            "loop_detected": True,
            "repetitions": repetitions
        }

    return {
        "loop_detected": False,
        "repetitions": repetitions
    }    
