from zipfile import ZipFile

with ZipFile('archive.zip') as filezip:
    for name in filezip.namelist():
        item = name.rstrip("/").split("/")
        print("  " * (len(item) - 1) + item[-1])
