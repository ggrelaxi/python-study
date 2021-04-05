import os

def fileScanner(ext):
    files = os.listdir('.')
    fixExtension = '.' + ext
    result = []

    for i in range(len(files)):
        filename, file_extension = os.path.splitext(files[i])
        if file_extension == fixExtension:
            result.append(files[i])

    return result