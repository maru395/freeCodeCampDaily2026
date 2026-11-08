conversion = {
    "B" : 1,
    "KB" : 1000,
    "MB" : 1000000,
    "GB" : 1000000000,
}

def number_of_files(file_size, file_unit, drive_size_gb):

    return (drive_size_gb * 1000000000) // (file_size * conversion[file_unit])
