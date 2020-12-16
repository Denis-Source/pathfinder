from PIL import Image
import random
import time


def open_image(image_name):
    image = Image.open(image_name)
    pixels = list(image.getdata())
    image.close()
    return pixels, image.size


def is_not_two_connections(current_node, twod_list):
    counter = 0
    try:
        if twod_list[current_node.cory + 1][current_node.corx] != 0:
            counter += 1
        if twod_list[current_node.cory - 1][current_node.corx] != 0:
            counter += 1
        if twod_list[current_node.cory][current_node.corx + 1] != 0:
            counter += 1
        if twod_list[current_node.cory][current_node.corx - 1] != 0:
            counter += 1
    finally:
        if counter == 2:
            return False
        else:
            return True


def find_node_by_cor(cory, corx, basic_nodes):
    for i in basic_nodes:
        if i.cory == cory and i.corx == corx:
            return i


class Image_Map(object):
    def __init__(self, file_name, start=144, finish=206):
        self.file_name = file_name
        self.start = start
        self.finish = finish

        self.image = Image.open(file_name)
        self.pixels = list(self.image.getdata())
        self.image_size = self.image.size
        self.width, self.height = self.image_size

        counter = 0
        twod_list = []
        for i in range(self.height):
            column = []
            for j in range(self.width):
                column.append(self.pixels[counter])
                counter += 1
            twod_list.append(column)
        self.twod_list = twod_list
        counter = 0
        basic_nodes = []
        for i in range(len(twod_list)):
            for j in range(len(twod_list[i])):
                if twod_list[i][j] == 0:
                    pass
                else:
                    node_name = "node:" + str(counter)
                    if twod_list[i][j] == 255:
                        node_type = "Regular"
                    elif twod_list[i][j] == self.start:
                        node_type = "Start"
                    elif twod_list[i][j] == self.finish:
                        node_type = "Finish"
                    else:
                        node_type = "Other"
                    counter += 1
                    temp_node = Node_basic(node_name, j, i, node_type)
                    basic_nodes.append(temp_node)
        self.basic_nodes = basic_nodes

        advanced_nodes = []

        # for i in self.basic_nodes:
        #     connections = []
        #     try:
        #         for j in self.basic_nodes:
        #             if j.cory == i.cory + 1 and j.corx == i.corx:
        #                 connections.append(j.name)
        #     except:
        #         pass
        #     try:
        #         for j in self.basic_nodes:
        #             if j.cory == i.cory - 1 and j.corx == i.corx:
        #                 connections.append(j.name)
        #     except:
        #         pass
        #     try:
        #         for j in self.basic_nodes:
        #             if j.cory == i.cory and j.corx == i.corx + 1:
        #                 connections.append(j.name)
        #     except:
        #         pass
        #     try:
        #         for j in self.basic_nodes:
        #             if j.cory == i.cory and j.corx == i.corx - 1:
        #                 connections.append(j.name)
        #     except:
        #         pass
        #
        #     advanced_node = Node_advanced(i.name, i.corx, i.cory, i.type, connections)
        #     advanced_nodes.append(advanced_node)
        # self.advanced_nodes = advanced_nodes

        visited_nodes = []
        not_visited_nodes = self.basic_nodes
        nodes_graph = []
        nodes_to_check = []
        nodes_anvanced = []
        counter = 0
        x_counter = 0
        y_counter = 0



        # for i in self.basic_nodes:
        #     if i.type == "Start":
        #         current_node = Node_basic(str(counter), i.corx, i.cory, "Start")
        #         counter += 1
        #
        #         while len(not_visited_nodes) != 0:
        #             try:
        #                 find_node_by_cor(current_node.cory +1, current_node.corx, self.basic_nodes)
















        # current_node = Node_advanced("Start")


















    def __str__(self):
        return_str = ""
        counter = 0
        for i in range(self.height):
            column_str = ""
            for j in range(self.width):
                if len(str(str(self.pixels[counter]))) == 1:
                    column_str += "00"
                elif len(str(str(self.pixels[counter]))) == 2:
                    column_str += "0"
                column_str += str(self.pixels[counter]) + " "
                counter += 1
            return_str += column_str + "\n"
        return return_str




class Node_basic(object):
    def __init__(self, name, corx, cory, node_type):
        self.name = name
        self.corx = corx
        self.cory = cory
        self.type = node_type

    def __str__(self):
        return f"{self.type} {self.name}, located at {self.corx}:{self.cory}"


class Node_advanced(object):
    def __init__(self, name, corx, cory, node_type, connections):
        self.name = name
        self.corx = corx
        self.cory = cory
        self.type = node_type
        self.connections = connections

    def __str__(self):
        return f"{self.type} {self.name}, located at {self.corx}:{self.cory}" \
            f" and has connections with {str(self.connections)}"







if __name__ == "__main__":
    log_time = time.time()
    test_image = Image_Map("map.bmp")

    print(f"It took {time.time()-log_time} seconds")