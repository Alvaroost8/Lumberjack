def list_of_ips(logs):
    ips=[]
    for log in logs:
        ip, time, instruction, url, response, response_weight, browser=log_segmentation(log)
        ips.append(ip)
    ips=set(ips)  #To remove duplicate IP addres and to unsort the logs
    return list(ips)