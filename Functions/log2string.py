def read_log_file(log_file_path):
    log_list = []
    with open(log_file_path, 'r') as file:
        for line in file:
          log_list.append(line.strip())
    return log_list
