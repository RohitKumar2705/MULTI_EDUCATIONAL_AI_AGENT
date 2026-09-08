def calculate_emergence_metrics(
        loop_result:dict,
        conflict_result: dict,
        redundancy_result: dict
    )->dict:

    """
    combine all emergent behavoir detection result 
    """
    loop_detected = loop_result.get("loop_detected",False)
    conflict_detected = conflict_result.get("conflict_detected","False")
    redundancy_detected = redundancy_result.get("redundancy_detected",False)

    negative_emergence_count = sum([ loop_detected, conflict_detected, redundancy_detected ])
    return { "loop_detected": loop_detected, "conflict_detected": conflict_detected, "redundancy_detected": redundancy_detected, "negative_emergence_count": ( negative_emergence_count ) }