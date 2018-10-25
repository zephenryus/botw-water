import colorsys
import math

from PIL import Image

from .Water import Water

material_colors = [
    (81, 116, 130),  # Water
    (45, 199, 130),  # Hot Water
    (114, 67, 142),  # Poison Water
    (238, 20, 1),  # Lava
    (21, 38, 54),  # Ice Water
    (76, 61, 38),  # Bog
    (120, 172, 193),  # Clear Water
    (72, 137, 135)  # Ocean Water
]


def generate_height_map(data: list, outfile: str, image_base_color=(0, 0, 0)):
    if len(data) != 4096:
        if len(data) < 4096:
            print("Error 2001: Data list is not long enough. Expected 4096 but saw {}".format(len(data)))
            exit(2001)

        print("Error 2002: Data list is too long. Expected 4096 but saw {}".format(len(data)))
        exit(2002)

    height_map_image = Image.new("RGB", (64, 64), image_base_color)

    for index in range(4096):
        x = index % 64
        y = index // 64

        color_value = round(data[index].height / 800.0 * 255)
        color = (color_value, color_value, color_value)

        height_map_image.putpixel((x, y), color)

    print("Saving {}...".format(outfile))
    height_map_image.save(outfile)


def generate_material_map(data: list, outfile: str, image_base_color=(0, 0, 0)):
    if len(data) != 4096:
        if len(data) < 4096:
            print("Error 2001: Data list is not long enough. Expected 4096 but saw {}".format(len(data)))
            exit(2001)

        print("Error 2002: Data list is too long. Expected 4096 but saw {}".format(len(data)))
        exit(2002)

    height_map_image = Image.new("RGB", (64, 64), image_base_color)

    for index in range(4096):
        x = index % 64
        y = index // 64
        color = material_colors[data[index].material_index]

        height_map_image.putpixel((x, y), color)

    print("Saving {}...".format(outfile))
    height_map_image.save(outfile)


def generate_x_flow_map(data: list, outfile: str, image_base_color=(0, 0, 0)):
    if len(data) != 4096:
        if len(data) < 4096:
            print("Error 2001: Data list is not long enough. Expected 4096 but saw {}".format(len(data)))
            exit(2001)

        print("Error 2002: Data list is too long. Expected 4096 but saw {}".format(len(data)))
        exit(2002)

    height_map_image = Image.new("RGB", (64, 64), image_base_color)

    for index in range(4096):
        x = index % 64
        y = index // 64
        color_value = round((data[index].x_axis_flow_rate + 1) / 2 * 255)
        color = (color_value, color_value, color_value)

        height_map_image.putpixel((x, y), color)

    print("Saving {}...".format(outfile))
    height_map_image.save(outfile)


def generate_z_flow_map(data: list, outfile: str, image_base_color=(0, 0, 0)):
    if len(data) != 4096:
        if len(data) < 4096:
            print("Error 2001: Data list is not long enough. Expected 4096 but saw {}".format(len(data)))
            exit(2001)

        print("Error 2002: Data list is too long. Expected 4096 but saw {}".format(len(data)))
        exit(2002)

    height_map_image = Image.new("RGB", (64, 64), image_base_color)

    for index in range(4096):
        x = index % 64
        y = index // 64
        color_value = round((data[index].z_axis_flow_rate + 1) / 2 * 255)
        color = (color_value, color_value, color_value)

        height_map_image.putpixel((x, y), color)

    print("Saving {}...".format(outfile))
    height_map_image.save(outfile)


def generate_xz_flow_map(data: list, outfile: str, image_base_color=(0, 0, 0)):
    if len(data) != 4096:
        if len(data) < 4096:
            print("Error 2001: Data list is not long enough. Expected 4096 but saw {}".format(len(data)))
            exit(2001)

        print("Error 2002: Data list is too long. Expected 4096 but saw {}".format(len(data)))
        exit(2002)

    height_map_image = Image.new("RGB", (64, 64), image_base_color)

    for index in range(4096):
        x = index % 64
        y = index // 64
        hue = math.atan(data[index].z_axis_flow_rate / data[index].x_axis_flow_rate)
        speed = math.sqrt(data[index].x_axis_flow_rate ** 2 + data[index].z_axis_flow_rate ** 2)
        rgb = colorsys.hsv_to_rgb(hue, 1, speed)
        color = (round(rgb[0] * 255), round(rgb[1] * 255), round(rgb[2] * 255))

        height_map_image.putpixel((x, y), color)

    print("Saving {}...".format(outfile))
    height_map_image.save(outfile)
