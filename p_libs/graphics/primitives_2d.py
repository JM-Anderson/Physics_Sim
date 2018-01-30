from pyglet.graphics import vertex_list


def square(v_list, x=0, y=0, r=5):
    v_list.vertices = [x-r, y-r,
                       x+r, y-r,
                       x+r, y+r,
                       x-r, y+r]
    v_list.colors = [255, 0, 0,
                     255, 0, 0,
                     255, 0, 0,
                     255, 0, 0]
    return v_list
