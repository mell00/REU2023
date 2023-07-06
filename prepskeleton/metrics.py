from skan.csr import skeleton_to_csgraph
from skan import Skeleton, summarize
from skan import draw
import numpy as np
import pandas as pd
from data import *
from segskeleton import *

def euclidean_length(skeleton, spacing_nm=1*1e9):
    total_distance = 0
    pixel_graph, coordinates = skeleton_to_csgraph(skeleton)
    branch_data = summarize(Skeleton(skeleton, spacing=spacing_nm))
    for i in range(len(branch_data['euclidean-distance'])):
        total_distance += branch_data['euclidean-distance'][i]
    print(branch_data.columns)
    print(total_distance)

def main():
    euclidean_length(skeleton, 1*1e9)

if __name__ == "__main__":
    main()
