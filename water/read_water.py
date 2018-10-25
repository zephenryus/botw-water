import os
import struct

from .Water import Water


def read_water(path: str, verbose=False) -> list:
    """
    Decompiles terrain water files to a list of Water objects

    :param path:        Path to .water.extm file to be compiled
    :param verbose:     Print messages to console
    :return:            List of Water objects
    """
    water_array = []

    if os.path.exists(path):
        if verbose:
            print("Reading {}...".format(path))

        with open(path, 'rb') as infile:
            # Each file contains 4,096 entries (64 * 64)
            for _ in range(4096):
                height, x_axis_flow_rate, z_axis_flow_rate, material_check, material_index = \
                    struct.unpack('<3H2B', infile.read(8))
                water_array.append(Water(
                    Water.actual_height(height),
                    Water.normalize_flow(x_axis_flow_rate),
                    Water.normalize_flow(z_axis_flow_rate),
                    material_check,
                    material_index
                ))

    return water_array
