import numpy as np
import pandas as pd
import json
import time


def read_df_from_json(dest):
    """ Original data json files need to be loaded a line at a time. """
    arr = []
    with open(dest, 'r') as f:
        for line in f:
            arr.append(json.loads(line))
    return pd.DataFrame(arr)
    

def write_nz(arr, fname):
    """Write the given array in packed binary format to the given file.
    
    arr: The NumPy array to write.
    """
    arr.tofile(fname)


def read_nz(fname, dtype):
    """Read an array with the given datatype from the given .nz file.
    
    fname: The name of the file to read.  Should be a .nz file as written by
           np.ndarray.tofile or storage.write_nz.
    dtype: The NumPy datatype of the file to read.
    """
    return np.fromfile(fname, dtype)