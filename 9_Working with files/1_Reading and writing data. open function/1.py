def file_read(file_name: str) -> None:
    file = open(file_name, encoding='utf-8')
    print(file.read())
