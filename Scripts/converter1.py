# Meshlab
import pymeshlab
# import pymeshlab    # Import 2 times to avoid exception

import ntpath

# Import HELP function
from my_help import my_print, read_my_settings


##################################
# Mesh Data Filter Using Meshlab
def mesh_filter(file_path):

    my_print('Mesh Data Processing')

    my_settings = read_my_settings()

    # Create a new MeshSet
    
    ms = pymeshlab.MeshSet()

    # Load a new mesh
    ms.load_new_mesh(file_path)

    # Close vertices
    ms.merge_close_vertices(threshold=my_settings['merge_close_vertices_threshold'])

    #ms.remove_unreferenced_vertices()

    # HC Smooth
    for i in range(my_settings['hc_laplacian_smooth_time']):
        ms.hc_laplacian_smooth()

    # Filling holes poisson
    try:
        print('Try surface_reconstruction_screened_poisson with preclean=False')
        ms.surface_reconstruction_screened_poisson( visiblelayer=False,
            depth=my_settings['poisson_depth'], fulldepth=5, cgdepth=0, scale=1.1, samplespernode=1.5,
            pointweight=4, iters=8, confidence=False, preclean=False)
    except:
        print('Surface_reconstruction_screened_poisson preclean=True')
        ms.surface_reconstruction_screened_poisson( visiblelayer=False,
            depth=my_settings['poisson_depth'], fulldepth=5, cgdepth=0, scale=1.1, samplespernode=1.5,
            pointweight=4, iters=8, confidence=False, preclean=True)

    # Reduce face numble
    ms.simplification_quadric_edge_collapse_decimation(
        targetfacenum=my_settings['targetfacenum'], targetperc=0, qualitythr=0.3,
        preserveboundary=False, boundaryweight=1, preservenormal=False, preservetopology=False,
        optimalplacement=True, planarquadric=False, planarweight=0.001, qualityweight=False,
        autoclean=True, selected =False)

    # Save project
    input_file_name = ntpath.basename(file_path).split('.')[0]
    
    save_path = "{}\\{}_Converted.stl".format(my_settings['processing_path'], input_file_name)

    ms.save_current_mesh(save_path)

    return save_path

##################################
if __name__ == '__main__':
    ms = None
    ms = pymeshlab.MeshSet()
    pass

#   PyMeshLab
#   All rights reserved.
#
#   VCGLib  http://www.vcglib.net                                     o o
#   Visual and Computer Graphics Library                            o     o
#                                                                  _   O  _
#   Paolo Cignoni                                                    \/)\/
#   Visual Computing Lab  http://vcg.isti.cnr.it                    /\/|
#   ISTI - Italian National Research Council                           |
#   Copyright(C) 2020       
