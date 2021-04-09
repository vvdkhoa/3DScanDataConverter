import json
import os

root_path = os.getcwd()

##############################
def read_my_settings():
    
    with open('settings.json') as json_file:
        json_str = json_file.read()
        my_settings = json.loads(json_str)

    # Default CAD Directory Setting #########
    if my_settings['input_path'] == '':
        my_settings['input_path'] = str(os.path.join(root_path, 'CAD_DATA\\InputFile'))
    if my_settings['output_path'] == '':
        my_settings['output_path'] = str(os.path.join(root_path, 'CAD_DATA\\OutputFile'))
    if my_settings['processing_path'] == '':
        my_settings['processing_path'] = str(os.path.join(root_path, 'CAD_DATA\\ProcessingFile'))
        
    return my_settings

##############################
# Get absolute paths of all files in a directory
def absoluteFilePaths(directory):
    for dirpath,_,filenames in os.walk(directory):
        for f in filenames:
            yield os.path.abspath(os.path.join(dirpath, f))

##############################
def my_print(text):
    print('''
++++++++++++++++++++++++++++++++++
+ {}
++++++++++++++++++++++++++++++++++
          '''.format(text))

if __name__ == '__main__':
    pass
