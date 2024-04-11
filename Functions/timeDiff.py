# Calculate the difference in log times between a log and the next log from the same ip address
def time_diff(logs_ip_dict):
    for ip in logs_ip_dict:
        for i in range(len(logs_ip_dict[ip])-1):
            logs_ip_dict[ip][i]["time_diff"] = logs_ip_dict[ip][i+1]["log_time"][0]-logs_ip_dict[ip][i]["log_time"][0]
    return logs_ip_dict