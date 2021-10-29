class UploadFile:
    for root, dirs, files in os.walk(walk_from)

    relative path = os.relpath(local_path,file_from)
    dropbox path = os.path.join(file_to,relative_path)

    with open(local_path, 'rb')as f:
        dbx_files.upload(f.read(),dropbox_path, mode = WriteMode('overwrite'))