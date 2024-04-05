import pytz
import datetime

def calculate_local_time(time, time_zone):
    time=time.split(":")
    
    local=pytz.timezone("Europe/Madrid")
    origin=pytz.timezone(time_zone)
    
    time_madrid=datetime.datetime.now(local)
    hour=time_madrid.hour
    
    time_origin=time_madrid.astimezone(origin)
    
    log_time=[int(time[0])+time_origin.hour-hour,int(time[1]),int(time[2])]
    
    if(log_time[0]>23):
        log_time[0]-=24
    elif(log_time[0]<0):
        log_time[0]+=24
    return (log_time[0],log_time[1],log_time[2])