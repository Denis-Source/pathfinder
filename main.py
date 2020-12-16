from image_map import ImageMap

if __name__ == '__main__':
    image_map = ImageMap("images/maze2.png")
    print(image_map)
    image_map.save_path(to_print=True)
