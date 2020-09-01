from collections import namedtuple
from matplotlib import pyplot as plt
import numpy as np

Point = namedtuple('Point', ['x', 'y'])


def move_right(instr, curr_pos):
    spaces = int(instr.replace('R', ''))
    new_pos = Point(curr_pos.x + spaces, curr_pos.y)
    return new_pos


def move_left(instr, curr_pos):
    spaces = int(instr.replace('L', ''))
    new_pos = Point(curr_pos.x - spaces, curr_pos.y)
    return new_pos


def move_up(instr, curr_pos):
    spaces = int(instr.replace('U', ''))
    new_pos = Point(curr_pos.x, curr_pos.y + spaces)
    return new_pos


def move_down(instr, curr_pos):
    spaces = int(instr.replace('D', ''))
    new_pos = Point(curr_pos.x, curr_pos.y - spaces)
    return new_pos


def collect_wire_points(wire_instr_list):

    curr_pos = Point(0,0)
    points = [curr_pos]

    for instr in wire_instr_list:
        if instr.startswith('R'):
            new_pos = move_right(instr, curr_pos)

        if instr.startswith('L'):
            new_pos = move_left(instr, curr_pos)

        if instr.startswith('U'):
            new_pos = move_up(instr, curr_pos)

        if instr.startswith('D'):
            new_pos = move_down(instr, curr_pos)

        points.append(new_pos)
        curr_pos = new_pos

    return points


def collect_wire_metapoints(wire_points):
    lines = [*zip(wire_points[:-1], wire_points[1:])]

    metapoints = []
    for line in lines:
        s,e = line

        if s.x == e.x:
            s_i = min(s.y, e.y)
            e_i = max(s.y, e.y)

            for i in range(s_i, e_i + 1):
                metapoints.append(Point(s.x, i))

        else:
            s_i = min(s.x, e.x)
            e_i = max(s.x, e.x)
            for i in range(s_i, e_i + 1):
                metapoints.append(Point(i, s.y))

    return set(metapoints)


def find_intersections(wire1_metapoints, wire2_metapoints):
    intersections = wire1_metapoints.intersection(wire2_metapoints)

    # Ignore central point
    intersections.discard(Point(0,0))

    return list(intersections)


def find_closest_point_to_center(intersections):
    pt_index = np.argmin([abs(p.x) + abs(p.y) for p in intersections])
    pt = intersections[pt_index]
    dist = abs(pt.x) + abs(pt.y)
    return pt, dist


def plot_wires(wire1_points, wire2_points, intersections, pt):
    """ Use fig.show() to show image. """

    w1_x = [p.x for p in wire1_points]
    w1_y = [p.y for p in wire1_points]

    w2_x = [p.x for p in wire2_points]
    w2_y = [p.y for p in wire2_points]

    int_x = [p.x for p in intersections]
    int_y = [p.y for p in intersections]

    fig = plt.figure()

    ax = fig.add_subplot(1,1,1)

    ax.plot(w1_x, w1_y, marker='o', color='b', label='wire1', alpha=0.5, markersize=2)
    ax.plot(w2_x, w2_y, marker='o', color='orange', label='wire2', alpha=0.5, markersize=2)
    ax.scatter(int_x, int_y, marker='x', color='r', label='intersection')
    ax.scatter(pt.x, pt.y, facecolors='none', edgecolors='g', label='closest', s=100)

    ax.grid(True)
    ax.set_xlim((min(w1_x + w2_x) - 1, max(w1_x + w2_x) + 1))
    ax.set_ylim((min(w1_y + w2_y) - 1, max(w1_y + w2_y) + 1))
    ax.legend()

    return fig
