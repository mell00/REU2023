from skan.csr import skeleton_to_csgraph
from skan import Skeleton, summarize
from skan import draw
import numpy as np
from data import *
from segskeleton import *


spacing_nm = 1 * 1e9  # nm per pixel
pixel_graph, coordinates = skeleton_to_csgraph(skeleton)
branch_data = summarize(Skeleton(skeleton, spacing=spacing_nm))
print(branch_data.head())

def main():
    print(pixel_graph)
    print(getSkeletonIntersection(skeleton))

if __name__ == "__main__":
    main()