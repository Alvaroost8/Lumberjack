# Convert log to dictionary
def log_to_dict(log):
    ip, country, coords, log_time, instruction, url, response, response_weight, browser=extract_features(log)
    log_dict={"ip":ip, "country":country, "coords":coords, "log_time":log_time, "instruction":instruction, "url":url, "response":response, "response_weight":response_weight, "browser":browser}
    return log_dict