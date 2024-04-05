def read_log_file(log_file_path):
    log_list = []
    with open(log_file_path, 'r') as file:
        for line in file:
            if line.startswith('www.sitges') or line.startswith('sitges'):
                log_list.append(line.strip())
    return log_list

# Example TEST
file_path = ""
log_strings = read_log_file(file_path)
print(log_strings)