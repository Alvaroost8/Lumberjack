def log_segmentation(log):
    match=re.search("^(?:(?:[\w-])+\.)+(?:[\w-])+ ([0-9]+.[0-9]+.[0-9]+.[0-9]+) - - \[\d{2}/[A-Za-z]{2,3}/\d{4}:(\d{2}:\d{2}:\d{2}) \+\d+\] \"([A-Z]+) (.+ HTTP/(?:[0-9]\.)+[0-9])\" ([0-9]+) ([0-9]+) (?:\"-\" )?(?:\".+\" )?\"(.+)\"",log)
    if(match!=None):
      return match.group(1), match.group(2), match.group(3), match.group(4), match.group(5), match.group(6), match.group(7)
    else:
      match=re.search("^(?:(?:[\w-])+\.)+(?:[\w-])+ ([0-9]+.[0-9]+.[0-9]+.[0-9]+) - - \[\d{2}/[A-Za-z]{2,3}/\d{4}:(\d{2}:\d{2}:\d{2}) \+\d+\] \"(.+)*\" ([0-9]+) ([0-9]+) \"-\" \"-\"",log)
      return match.group(1), match.group(2), None, match.group(3), match.group(4), match.group(5), None
