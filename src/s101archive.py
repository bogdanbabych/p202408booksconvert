import zipfile
import os, sys

def archive_epub_files(directory):
    """
    Archives all EPUB files within a given directory into a ZIP file.

    Args:
        directory: The directory to search for EPUB files.
    """
    iCount = 0
    ## directory to search
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.startswith('.'):
                path2tmpFile = os.path.join(root, file)
                os.remove(path2tmpFile)

        for dir in dirs:
            if dir.endswith('.epub'): # found the directory to convert into zip (with the epub extension)
                sys.stderr.write(f'{dir}\n')
                dirWOext, extension = os.path.splitext(dir) # remove extension .epub
                path_dir2zip = os.path.join(root, dir)
                zipped_file_name = f"{dirWOext}_book.epub" # add back the extension to the otput filename, but with the _book.epub ending...
                zipped_file_path_name = os.path.join(root, zipped_file_name) # generate a file name for zipped _book.epub file

                zipped_file_name2 = f"{dirWOext}_book.mobi"
                zipped_file_path_name2 = os.path.join(root, zipped_file_name2)

                zipped_file_name3 = f"{dirWOext}_b.epub"
                zipped_file_path_name3 = os.path.join(root, zipped_file_name3)

                '''
                with zipfile.ZipFile(zip_file_path_name, 'w') as zip_file:
                    zip_file.write(, os.path.relpath(, directory))
                '''
                # execute external command:
                command = 'zip -r -q ' + zipped_file_path_name + ' ' + path_dir2zip
                command2 = 'rm -rf ' + path_dir2zip
                command3 = 'ebook-convert ' + zipped_file_path_name + ' ' + zipped_file_path_name2
                command4 = 'ebook-convert ' + zipped_file_path_name2 + ' ' + zipped_file_path_name3

                
                # 76C2A2ADC6DB5EFD1C002118F63B7A60_book.mobi 76C2A2ADC6DB5EFD1C002118F63B7A60.epub'
                os.system(command)
                sys.stderr.write(command + ' - done!\n')
                os.system(command2)
                sys.stderr.write(command2 + ' - done!\n')
                os.system(command3)
                sys.stderr.write(command3 + ' - done!\n')
                os.system(command4)
                sys.stderr.write(command4 + ' - done!\n')

                try:
                    os.remove(zipped_file_path_name)
                except:
                    sys.stderr.write(f'cannot remove file{zipped_file_path_name}\n')

                try:
                    os.remove(zipped_file_path_name2)
                except:
                    sys.stderr.write(f'cannot remove file{zipped_file_path_name2}\n')                
                    

                iCount += 1

                sys.stderr.write('\nProcessed book No. ' + str(iCount) + ' ' + zipped_file_path_name3 + '\n\n\n')



if __name__ == "__main__":
    directory_to_archive = sys.argv[1] # "../data/data/BooksC"
    sys.stderr.write(directory_to_archive + '\n')
    archive_epub_files(directory_to_archive)



'''
# original suggestion - gemini
# https://gemini.google.com/app/41ea0925cdc0fc8b
import zipfile
import os

def archive_epub_files(directory):
    """
    Archives all EPUB files within a given directory into a ZIP file.

    Args:
        directory: The directory to search for EPUB files.
    """

    zip_file_name = f"{directory}.zip"
    with zipfile.ZipFile(zip_file_name, 'w') as zip_file:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith('.epub'):
                    file_path = os.path.join(root, file)
                    zip_file.write(file_path, os.path.relpath(file_path, directory))

if __name__ == "__main__":
    directory_to_archive = "/path/to/your/directory"
    archive_epub_files(directory_to_archive)

'''