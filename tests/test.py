import filecmp
import hashlib
import json

import water


def water_to_json():
    """
    Tests reading of water file and exports data as a json file
    """
    data = water.read_water("assets/5000000000.water.extm")

    print("Saving file output/5000000000.water.extm.json...")
    with open("output/5000000000.water.extm.json", "w+") as outfile:
        out_obj = []
        for entry in data:
            out_obj.append(entry.__dict__)

        outfile.write(json.dumps(out_obj, indent=4, separators=(',', ': ')))


def water_to_binary_string():
    """
    Tests that data is recompiled correctly and matches the original file
    """
    data = water.read_water("assets/5000000000.water.extm")
    binary_data = water.compile_water(data)

    hash_md5 = hashlib.md5()
    with open("assets/5000000000.water.extm", "rb") as infile:
        for chunk in iter(lambda: infile.read(4096), b""):
            hash_md5.update(chunk)

    file_hash = hash_md5.hexdigest()

    hash_md5 = hashlib.md5()
    pos = 0
    for chunk in iter(lambda: binary_data[pos:pos + 4096], b""):
        pos += 4096
        hash_md5.update(chunk)

    string_hash = hash_md5.hexdigest()

    print("The file and binary string are the same: {0}".format(file_hash == string_hash))


def water_to_binary_file():
    """
    Tests reading data from water file then writes the same data back as a binary
    """
    data = water.read_water("assets/5000000000.water.extm")
    water.write_water(data, "output/5000000000.water.extm")
    print("The files are the same: {0}".format(
        filecmp.cmp("assets/5000000000.water.extm", "output/5000000000.water.extm")))


def water_to_image():
    """
    Tests reading data from water file then generating waterrial map images
    """
    data = water.read_water("assets/5000000000.water.extm")
    water.generate_height_map(data, 'output/5000000000.water.extm.height.tiff')
    water.generate_material_map(data, 'output/5000000000.water.extm.mate.tiff')
    water.generate_x_flow_map(data, 'output/5000000000.water.extm.x-flow.tiff')
    water.generate_z_flow_map(data, 'output/5000000000.water.extm.z-flow.tiff')
    water.generate_xz_flow_map(data, 'output/5000000000.water.extm.xz-flow.tiff')


def main():
    water_to_json()
    water_to_binary_string()
    water_to_binary_file()
    water_to_image()


if __name__ == "__main__":
    main()
