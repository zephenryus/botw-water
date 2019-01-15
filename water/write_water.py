import struct

from .Water import Water


def compile_water(data: list, bom='little_endian') -> bytes:
    bom = '<' if bom == 'little_endian' else '>'

    if len(data) != 4096:
        if len(data) < 4096:
            print("Error 2001: Data list is not long enough. Expected 4096 but saw {}".format(len(data)))
            exit(2001)

        print("Error 2002: Data list is too long. Expected 4096 but saw {}".format(len(data)))
        exit(2002)

    water_binary = b''
    for index in range(4096):
        water_binary += struct.pack(
            '{}3H2B'.format(bom),
            Water.to_int(data[index].height),
            Water.denormalize_flow(data[index].x_axis_flow_rate),
            Water.denormalize_flow(data[index].z_axis_flow_rate),
            data[index].material_check,
            data[index].material_index
        )

    return water_binary


def write_water(data: list, outfile_name: str, bom='little_endian') -> None:
    if len(data) != 4096:
        if len(data) < 4096:
            print("Error 2001: Data list is not long enough. Expected 4096 but saw {}".format(len(data)))
            exit(2001)

        print("Error 2002: Data list is too long. Expected 4096 but saw {}".format(len(data)))
        exit(2002)

    with open(outfile_name, 'wb+') as outfile:
        binary_data = compile_water(data, bom)
        outfile.write(binary_data)
