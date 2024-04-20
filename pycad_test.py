from pycad.visualization import STLVisualizer
from glob import glob
stl_paths = glob("./data/*.stl")

visualizer = STLVisualizer(stl_paths)
visualizer.visualize()