# Extract features from log
def extract_features(log): 
    ip, time, instruction, url, response, response_weight, browser=log_segmentation(log)
    country, coords, time_zone=geolocalizate_ip(ip)
    log_time=calculate_local_time(time, time_zone)
    return ip, country, coords, log_time, instruction, url, response, response_weight, browser