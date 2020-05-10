import os

import sys

import tkinter
from tkinter.filedialog import askdirectory
tkinter.Tk().withdraw()

#%% matching extensions 
EXTENSIONS = ['.aux', '.bbl', '.bcf', '.gz', 'lot',
              '.lof', '.lot', '.out', '.blg', '.log', '.toc', '.xml', 
              '.fls', '.fdb_latexmk',
              # '.pdf',
              ]

#%% ask for dir
def ask_for_dir():
    print('---please select destination folder---')
    path = askdirectory(title="destination folder", 
                        initialdir=("."))
           
    # return path
    return path

#%% remove file function
def remove_file(file):
    # construct full path to file
    # note: 'path' will take the global path name from the above function call
    file_path = os.path.join(path, file)
    
    # skip directories
    if not os.path.isfile(file_path):
        return 
    
    # get file extension
    _, ext = os.path.splitext(file)
    
    # purge any files with matching extensions
    if ext in EXTENSIONS:
        print("removing {}".format(file))
        os.remove(file_path)
        
    return

#%% Go through each folder and get file lists
if __name__ == "__main__":
    try:
        PURGE = sys.argv[1]
    except:
        PURGE = 0
        
    dirs = ['preface',
            'appendix_A',
            'appendix_B',
            'appendix_C',
            'chapter_1',
            'chapter_2',
            'chapter_3',
            'chapter_4',
            'chapter_5',
            'main']
        
    if str(PURGE).lower() == 'purge':
        for path in dirs:
            print("---removing files from {}---".format(path))
            # get contents
            contents = os.listdir(path)
            
            # iterate through each file
            for file in contents:
                
                # remove file with matching extensions
                remove_file(file)
                
    elif PURGE == False:
        path = ask_for_dir()
        
        # get contents
        contents = os.listdir(path)
        
        # iterate through each file
        for file in contents:
            
            # remove file with matching extensions
            remove_file(file)
            
    else:
        print("key word is incorrect, please use PURGE or pick a folder")