# Read setting
import json
with open('settings.json') as json_file:
    json_str = json_file.read()
    my_settings = json.loads(json_str)

# Meshlab
import pymeshlab
import pymeshlab    # Import 2 times to avoid exception


# Import HELP function
from my_help import my_print


##################################
# Mesh Data Filter Using Meshlab
def mesh_filter(my_settings):

    my_print('Mesh Data Processing')

    # Read stl file
    ms = pymeshlab.MeshSet()
    ms.load_new_mesh("{}\\input.stl".format(my_settings['input_path']))

    # Close vertices
    ms.merge_close_vertices(threshold=1)

    # HC Smooth
    for i in range(my_settings['hc_laplacian_smooth_time']):
        ms.hc_laplacian_smooth()

    # Filling holes poisson
    ms.surface_reconstruction_screened_poisson(
        visiblelayer=False, depth=10, fulldepth=5, cgdepth=0, scale=1.1, samplespernode=1.5, pointweight=4,
        iters=my_settings['poisson_iters'],
        confidence=False, preclean=True)     # preclean= False
    
    # Reduce face numble
    ms.simplification_quadric_edge_collapse_decimation(targetfacenum=my_settings['targetfacenum'])

    # Save project
    ms.save_current_mesh("{}\\filtered_mesh.stl".format(my_settings['processing_path']))

    
##################################
if __name__ == '__main__':
    pass

    #my_print('MY SETTINGS')
    #for key in my_settings:
    #    print("{}: {}".format(key, my_settings[key]))

    # print('Input path' + my_settings['input_path'])

    #mesh_filter(my_settings)

    #convert_stl_iges(my_settings)

    #my_print('COMPLETED')
