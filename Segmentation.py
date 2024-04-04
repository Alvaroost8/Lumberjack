import re

def log_segmentation(log):
    match=re.search("^www.(?:\w)+.(?:\w)+ ([0-9]+.[0-9]+.[0-9]+.[0-9]+) - - \[\d{2}/[A-Za-z]{2,3}/\d{4}:(\d{2}:\d{2}:\d{2}) \+\d+\] \"([A-Z]{,4}) (.+ HTTP/(?:[0-9]\.)+[0-9])\" ([0-9]+) ([0-9]+) (?:\"-\" )?\"(.+)\"",log)
    return match.group(1), match.group(2), match.group(3), match.group(4), match.group(5), match.group(6), match.group(7)

log="www.sitgesanytime.com 47.76.35.19 - - [22/Jan/2024:00:00:07 +0100] \"HEAD /fr/pag492/explora-platges-i-ports-2/id12/les-anquines.htm HTTP/1.1\" 301 4840 \"-\" \"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3928.157 Safari/537.36\""
log2="www.sitgesanytime.com 195.154.122.156 - - [22/Jan/2024:22:23:49 +0100] \"GET /plantilles/turisme/img/temps3/31.svg HTTP/2.0\" 200 4871 \"https://www.sitgesanytime.com/de/planen-sie-ihre-reise/sitges-auf-einen-blick/id78/casa-vilella.htm\" \"Mozilla/5.0 (compatible; AhrefsBot/7.0; +http://ahrefs.com/robot/)\""
log3="www.sitgesanytime.com 195.154.122.46 - - [22/Jan/2024:22:26:12 +0100] \"GET /comu/js/jquery.browser.js HTTP/2.0\" 200 1476 \"https://www.sitgesanytime.com/fr/pl7/que-faire/sites-a-visiter/id26/port-de-sitges-aiguadolc.htm\" \"Mozilla/5.0 (compatible; AhrefsBot/7.0; +http://ahrefs.com/robot/)\""

a,b,c,d,e,f,g=log_segmentation(log)
print(a)  #IP
print(b)  #Time
print(c)  #Instruction
print(d)  #URL
print(e)  #Server response
print(f)  #Response weight in bytes
print(g)  #Client browser