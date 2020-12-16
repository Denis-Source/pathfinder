from PIL import Image
from astar import *


class ImageMap:
    def __init__(self, file_path, start_color=(255, 0, 0), finish_color=(0, 0, 255), path_color=255):
        self.file_path = file_path
        self.path_color = path_color
        self.start_color = start_color
        self.finish_color = finish_color
        self.image = Image.open(self.file_path, "r")
        self.pixels = list(self.image.getdata())
        self.pixel_map, self.pixel_map_binary,\
            self.start, self.finish, self.node_amount = self.pm_pmb_s_f_nc()

    def __str__(self):
        string = f"Map created from {self.file_path}\n"
        rows = []

        for i in self.pixel_map_binary:
            row = []
            for j in i:
                row.append(j)
            rows.append(row)

        sy, sx = self.start
        fy, fx = self.finish

        rows[sy][sx] = "s"
        rows[fy][fx] = "f"

        for y in rows:
            string_row = ""
            for x in y:
                if x == 0:
                    string_row += "   "
                elif x == 1:
                    string_row += " # "
                else:
                    string_row += f" {x} "
            string += f"{string_row}\n"

        string += f"Total of nodes: {self.node_amount}"
        return string



    def pm_pmb_s_f_nc(self):
        second_list = []
        second_list_b = []
        nav_counter = 0
        node_counter = 0
        start_cor = None
        finish_cor = None
        for y in range(self.image.height):
            first_list = []
            first_list_b = []
            for x in range(self.image.width):
                cur_pix = self.pixels[nav_counter]
                first_list.append(cur_pix)
                if cur_pix == (0, 0, 0):
                    first_list_b.append(1)
                else:
                    first_list_b.append(0)
                    node_counter += 1
                if cur_pix == self.start_color:
                    start_cor = (y, x)
                if cur_pix == self.finish_color:
                    finish_cor = (y, x)
                nav_counter += 1
            second_list.append(first_list)
            second_list_b.append(first_list_b)
        return second_list, second_list_b, start_cor, finish_cor, node_counter

    def find_path(self):
        path = astar(
            self.pixel_map_binary, self.start, self.finish
        )
        return path

    def save_path(self, path_color=(255, 142, 66), to_print=False):
        image_path = f"{self.file_path.split('.')[0]}_solved.png"
        path = self.find_path()[1:-1]
        data_to_put = self.pixels
        for cor in path:
            y, x = cor
            i = y * self.image.width + x
            data_to_put[i] = path_color
        new_image = Image.new(self.image.mode, self.image.size)
        new_image.putdata(data_to_put)
        new_image.save(image_path, self.image.format)
        if to_print:
            print(path)


if __name__ == '__main__':
    a = ImageMap("map1.png")
    print(a.find_path())