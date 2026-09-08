from datetime import datetime 
class BehaviorMonitor:
    def __init__(self):
        self.logs = []

    def log_event(self,agent,action,message):
        event = {
            "timestamp": (
                datetime.now().isoformat()
            ),
            "agent": agent,
            "action": action,
            "message": message
        }    

        self.logs.append(event)

    def get_logs(self):
        return self.logs    