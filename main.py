from packages.logger import log_to_console, log_to_file

@log_to_file('log.txt')
@log_to_console
def summator(a, b):
    return a + b


summator(2, 3)
