import time

def calculate_latency(start_time:float,end_time:float)->float:
    """
    Calculate how long the complete multi-agent workflow took.
    """
    return round(end_time - start_time,4)

def calculate_agent_count(logs:list)->int:
    """
    Count how many agent actions were recorded.
    """

    return len(logs)

def calculate_unique_agents(logs:list)->int:
    """
    Count the number of different agents involved.
    """

    agents = set()
    for log in logs:
        agents.add(log["agent"])
    return len(agents)

def calculate_performance_metrics(logs:list,start_time:float,end_time:float)->dict:
    """
Calculate all basic performance metrics.
"""

    latency = calculate_latency(start_time,end_time)
    total_agent_actions = calculate_agent_count(logs)

    unique_agents = calculate_unique_agents(logs)

    return { "latency_seconds": latency, "total_agent_actions": total_agent_actions, "unique_agents": unique_agents }