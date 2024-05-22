import re

def listify_log(log_data):

    """ input: string blob (log data)
        output: list (of logs)
    """

    pattern = re.compile(r'\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2} (?:AM|PM)')

    matches = list(pattern.finditer(log_data)) # find the datetimes

    positions = [match.start() for match in matches] # we'll use these indexes to snap logs together with their datetime

    logs = []
    for i in range(len(positions)):
        if i == len(positions) - 1:
            logs.append(log_data[positions[i]:])
        else:
            logs.append(log_data[positions[i]:positions[i+1]])
    
    return logs