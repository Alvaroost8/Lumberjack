# Convert log to dictionary, with the ip as the key and the logs as the value
def log_to_dict(logs, ip_list):
    logs_ip_dict={}
    for ip in ip_list:
        for log in logs:
            if ip in log:
                ip, country, coords, log_time, instruction, url, response, response_weight, browser=extract_features(log)
                log_dict={"ip":ip, "country":country, "coords":coords, "log_time":log_time, "instruction":instruction, "url":url, "response":response, "response_weight":response_weight, "browser":browser}
                if ip in logs_ip_dict:
                    logs_ip_dict[ip].append(log_dict)
                else:
                    logs_ip_dict[ip]=[log_dict]
    return log_dict
