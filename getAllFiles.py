import glob
import os

def list_of_files(path, file_ending='*.pdf'):
    '''
    path = directory of files
    file_ending = type of files (default = ".pdf")
    '''
    return glob.glob(os.path.join(path, file_ending))

#print(list_of_files(rf"C:\Users\4501531\OneDrive - Signode Industrial Group\Desktop\Sid's Work\Test Python\Invoice edits"))