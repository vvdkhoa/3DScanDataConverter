import json
import os
from pathlib import Path

root_path = os.getcwd()
cad_path = Path(root_path).parent

##############################
def read_my_settings():
    
    with open('settings.json') as json_file:
        json_str = json_file.read()
        my_settings = json.loads(json_str)

    # Default CAD Directory Setting #########
    if my_settings['input_path'] == '':
        my_settings['input_path'] = str(os.path.join(cad_path, 'CAD_DATA\\InputFile'))
    if my_settings['output_path'] == '':
        my_settings['output_path'] = str(os.path.join(cad_path, 'CAD_DATA\\OutputFile'))
    if my_settings['processing_path'] == '':
        my_settings['processing_path'] = str(os.path.join(cad_path, 'CAD_DATA\\ProcessingFile'))
        
    return my_settings

 ##############################
def read_translate():

    try:
        with open('translate.json') as json_file:
            json_str = json_file.read()
            translate = json.loads(json_str)
    except:
        with open('translate.json', encoding="utf8", errors='ignore') as json_file:
            json_str = json_file.read()
            translate = json.loads(json_str)
        
    return translate

##############################
# Get absolute paths of all files in a directory
def absoluteFilePaths(directory):
    for dirpath,_,filenames in os.walk(directory):
        for f in filenames:
            yield os.path.abspath(os.path.join(dirpath, f))


##############################
def clear_folder(folder_path):
    filelist = [ f for f in os.listdir(folder_path) if not f.endswith(".py") ]
    error = []
    if filelist:
        for f in filelist:
            try:
                os.remove(os.path.join(folder_path, f))
            except PermissionError:
                print("Can not remove: {}".format(f))
                error.append(f)
    return error

##############################
def my_print(text):
    print('''
++++++++++++++++++++++++++++++++++
+ {}
++++++++++++++++++++++++++++++++++
          '''.format(text))

##############################
if __name__ == '__main__':
    pass
