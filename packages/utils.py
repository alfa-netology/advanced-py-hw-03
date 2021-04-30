from packages.logger import log_to_console, log_to_file
from hashlib import md5

LOG_PATH = 'log.txt'

@log_to_file(LOG_PATH)
@log_to_console
def generate_hash(source_path):
    with open(source_path, encoding="utf-8") as file:
        for line in file:
            yield f"{line}MD5 hash: {md5(line.encode()).hexdigest()}\n"

@log_to_file(LOG_PATH)
@log_to_console
def get_hash(source):
    with open('hash.txt', 'w', encoding='utf-8') as file:
        for hash_string in generate_hash(source):
            file.write(f"{hash_string}\n")
    return f"All hash generate successful"
