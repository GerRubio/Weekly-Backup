import datetime, os, statistics, time, zipfile

# Available extensions.
extensions = ('.html', '.py', '.txt', '.jpg', '.png')

# Week days.
week_days = datetime.datetime.today().weekday()

files_list = []
files_names = []
files_sizes = []
average_size = 0
total_time = 0

# Get the files in directories.
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith(extensions):
            files_list.append(os.path.join(root, file))
            
            # Gets the name of the files.
            files_names.append(file)
    
# Compression mode.
compression = zipfile.ZIP_DEFLATED

# Create the zip file. If the file exists, it is deleted and a new one is created.
if week_days == 0:
    if os.path.isfile('Lunes.zip'):
        os.remove('Lunes.zip')

    compress_file = zipfile.ZipFile('Lunes.zip', mode = 'w')
elif week_days == 1:
    if os.path.isfile('Martes.zip'):
        os.remove('Martes.zip')
    
    compress_file = zipfile.ZipFile('Martes.zip', mode = 'w')
elif week_days == 2:
    if os.path.isfile('Miercoles.zip'):
        os.remove('Miercoles.zip')

    compress_file = zipfile.ZipFile('Miercoles.zip', mode = 'w')
elif week_days == 3:
    if os.path.isfile('Jueves.zip'):
        os.remove('Jueves.zip')

    compress_file = zipfile.ZipFile('Jueves.zip', mode = 'w')
elif week_days == 4:
    if os.path.isfile('Viernes.zip'):
        os.remove('Viernes.zip')

    compress_file = zipfile.ZipFile('Viernes.zip', mode = 'w')
elif week_days == 5:
    if os.path.isfile('Sábado.zip'):
        os.remove('Sábado.zip')

    compress_file = zipfile.ZipFile('Sábado.zip', mode = 'w')
elif week_days == 6:
    if os.path.isfile('Domingo.zip'):
        os.remove('Domingo.zip')

    compress_file = zipfile.ZipFile('Domingo.zip', mode = 'w')
    
try:
    # Starting to calculate the compression time.
    start_time = datetime.datetime.now().second

    for file_name in files_list:     
        # Add file to the zip file.
        compress_file.write(file_name, compress_type = compression)

except FileNotFoundError:
    print('File not found')
finally:
    # Close file.
    compress_file.close()

# Get the time when it finished to compress.
end_time = datetime.datetime.now().second

# Total time to compress file.
total_time = end_time - start_time

for size in files_list:
    files_sizes.append(os.path.getsize(size))

# Total files size.
sum_sizes = sum(files_sizes)

# If the program does not find any file to compress.
if sum_sizes == 0:
    print('There are no files in this directory')
else:
    # Average files size.
    average_size = round(statistics.mean(files_sizes))

# Results.
print(f'Compressed files:')

for files in files_names:
    print(files)

print('')  
print(f'Total files saved: {len(files_list)}')
print(f'Total files size: {sum_sizes} bytes')
print(f'Average files size: {average_size} bytes')
print(f'Total time to compress: {total_time} seconds')