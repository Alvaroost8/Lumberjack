def log_to_dict(logs, ip_list):
    logs_ip_dict={}
    time_zones={}
    countries={}
    coordinates={}
    for log in logs:
        ip, time, instruction, url, response, response_weight, browser=log_segmentation(log)
        if ip not in logs_ip_dict:
            country, coords, time_zone=geolocalizate_ip(ip)
            log_time=calculate_local_time(time, time_zone)
            time_zones[ip]=time_zone
            countries[ip]=country
            coordinates[ip]=coords
        else:
            log_time=calculate_local_time(time, time_zones[ip])
        log_dict={"country":countries[ip], "coords":coordinates[ip], "log_time":log_time, "instruction":instruction, "url":url, "response":response, "response_weight":response_weight, "browser":browser}
        if ip in logs_ip_dict:
            logs_ip_dict[ip].append(log_dict)
        else:
            logs_ip_dict[ip]=[log_dict]
    return logs_ip_dict
