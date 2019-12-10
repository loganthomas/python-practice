from collections import namedtuple
from matplotlib import pyplot as plt
import numpy as np
from pathlib import Path

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

    w1_x = [p.x for p in wire1_points]
    w1_y = [p.y for p in wire1_points]

    w2_x = [p.x for p in wire2_points]
    w2_y = [p.y for p in wire2_points]

    int_x = [p.x for p in intersections]
    int_y = [p.y for p in intersections]

    plt.plot(w1_x, w1_y, marker='o', label='wire1', alpha=0.5, markersize=2)
    plt.plot(w2_x, w2_y, marker='o', label='wire2', alpha=0.5, markersize=2)
    plt.scatter(int_x, int_y, marker='x', color='r', label='intersection')
    plt.scatter(pt.x, pt.y, facecolors='none', edgecolors='g', label='closest', s=100)

    plt.grid(True)
    plt.xlim((min(w1_x + w2_x) - 1, max(w1_x + w2_x) + 1))
    plt.ylim((min(w1_y + w2_y) - 1, max(w1_y + w2_y) + 1))
    plt.legend()
    plt.show()


# Part 1 provided example 1
wire1_points = collect_wire_points(['R8', 'U5', 'L5', 'D3'])
wire2_points = collect_wire_points(['U7', 'R6', 'D4', 'L4'])
wire1_metapoints = collect_wire_metapoints(wire1_points)
wire2_metapoints = collect_wire_metapoints(wire2_points)
intersections = find_intersections(wire1_metapoints,wire2_metapoints)
pt, dist = find_closest_point_to_center(intersections)

plot_wires(wire1_points, wire2_points, intersections, pt)
print(f'Point: {pt} Dist: {dist}')


# Part 1 provided example 2
wire1_points = collect_wire_points(['R75','D30','R83','U83','L12','D49','R71','U7','L72'])
wire2_points = collect_wire_points(['U62','R66','U55','R34','D71','R55','D58','R83'])
wire1_metapoints = collect_wire_metapoints(wire1_points)
wire2_metapoints = collect_wire_metapoints(wire2_points)
intersections = find_intersections(wire1_metapoints,wire2_metapoints)
pt, dist = find_closest_point_to_center(intersections)

plot_wires(wire1_points, wire2_points, intersections, pt)
print(f'Point: {pt} Dist: {dist}')

# Part 1 provided example 3
wire1_points = collect_wire_points(['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51'])
wire2_points = collect_wire_points(['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7'])
wire1_metapoints = collect_wire_metapoints(wire1_points)
wire2_metapoints = collect_wire_metapoints(wire2_points)
intersections = find_intersections(wire1_metapoints,wire2_metapoints)
pt, dist = find_closest_point_to_center(intersections)

plot_wires(wire1_points, wire2_points, intersections, pt)
print(f'Point: {pt} Dist: {dist}')


# Part 1 answer
data_path = Path('advent_of_code/year_2019/data/day3_puzzle.txt')
text = data_path.read_text().strip().split('\n')
wire1_text = text[0].split(',')
wire2_text = text[1].split(',')

wire1_points = collect_wire_points(wire1_text)
wire2_points = collect_wire_points(wire2_text)
wire1_metapoints = collect_wire_metapoints(wire1_points)
wire2_metapoints = collect_wire_metapoints(wire2_points)
intersections = find_intersections(wire1_metapoints,wire2_metapoints)
pt, dist = find_closest_point_to_center(intersections)

plot_wires(wire1_points, wire2_points, intersections, pt)
print(f'Point: {pt} Dist: {dist}')

