# Calculate the difference in log times between a log and the next log from the same ip address
def time_diff(features):
    for ip in features:
        for i in range(len(features[ip])):
            log_time=list(features[ip][i]["log_time"])
            if(i==0):
                features[ip][i]["time_diff"]=-1
            else:
                if((log_time[0]-features[ip][i-1]["log_time"][0])<0):
                    features[ip][i]["time_diff"]=-1
                else:
                    time_diff=0
                    if((log_time[2]-features[ip][i-1]["log_time"][2])<0):
                        log_time[2]+=60
                        log_time[1]-=1
                    time_diff+=log_time[2]-features[ip][i-1]["log_time"][2]
                    if((log_time[1]-features[ip][i-1]["log_time"][1])<0):
                        log_time[1]+=60
                        log_time[0]-=1
                    time_diff+=(log_time[1]-features[ip][i-1]["log_time"][1])*60
                    time_diff+=(log_time[0]-features[ip][i-1]["log_time"][0])*3600
                    if(time_diff<0):
                        features[ip][i]["time_diff"]=-1
                    else:
                        features[ip][i]["time_diff"]=time_diff
    return features
