def parse_event(line):
    line = line.strip().split(maxsplit=2)

    if len(line) >= 2:
        time = line[0]
        level = line[1]

        if level == 'DEBUG' or level == 'INFO' or level == "WARNING" or level == 'ERROR':
            if len(line) == 3:
                message = line[2]
            else:
                message = ''

            return {'time': time, 'level': level, 'message': message}
    raise ValueError

