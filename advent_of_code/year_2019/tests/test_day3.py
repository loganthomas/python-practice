from advent_of_code.year_2019 import day3
from pathlib import Path
import pytest
import random


def make_rand_instrs(letter):
    """ Like a fixture but not..."""
    ints = [random.randint(0,100) for _ in range(3)]
    instrs = [f'{letter}{int}' for int in ints]

    return [*zip(instrs,ints)]


@pytest.mark.parametrize('instr,expected', make_rand_instrs('R'))
def test_move_right_from_center(instr, expected):
    # Setup
    center = day3.Point(0,0)

    # Exercise
    result = day3.move_right(instr,center)

    # Verify
    assert result.x == expected
    assert result.y == 0

    # Cleanup - none necessary


@pytest.mark.parametrize('instr,expected', make_rand_instrs('R'))
def test_move_right_from_random_x(instr, expected):
    # Setup
    pt_rand_x = day3.Point(random.randint(0,100),0)

    # Exercise
    result = day3.move_right(instr,pt_rand_x)

    # Verify
    assert result.x == pt_rand_x.x + expected
    assert result.y == 0

    # Cleanup - none necessary


@pytest.mark.parametrize('instr,expected', make_rand_instrs('L'))
def test_move_left_from_center(instr, expected):
    # Setup
    center = day3.Point(0,0)

    # Exercise
    result = day3.move_left(instr,center)

    # Verify
    assert result.x == -expected
    assert result.y == 0

    # Cleanup - none necessary


@pytest.mark.parametrize('instr,expected', make_rand_instrs('L'))
def test_move_left_from_random_x(instr, expected):
    # Setup
    pt_rand_x = day3.Point(random.randint(0,100),5)

    # Exercise
    result = day3.move_left(instr,pt_rand_x)

    # Verify
    assert result.x == pt_rand_x.x - expected
    assert result.y == 5

    # Cleanup - none necessary


@pytest.mark.parametrize('instr,expected', make_rand_instrs('U'))
def test_move_up_from_center(instr, expected):
    # Setup
    center = day3.Point(0,0)

    # Exercise
    result = day3.move_up(instr,center)

    # Verify
    assert result.x == 0
    assert result.y == expected

    # Cleanup - none necessary


@pytest.mark.parametrize('instr,expected', make_rand_instrs('U'))
def test_move_up_from_random_y(instr, expected):
    # Setup
    pt_rand_y = day3.Point(3,random.randint(0,100))

    # Exercise
    result = day3.move_up(instr,pt_rand_y)

    # Verify
    assert result.x == 3
    assert result.y == pt_rand_y.y + expected

    # Cleanup - none necessary


@pytest.mark.parametrize('instr,expected', make_rand_instrs('D'))
def test_move_down_from_center(instr, expected):
    # Setup
    center = day3.Point(0,0)

    # Exercise
    result = day3.move_down(instr,center)

    # Verify
    assert result.x == 0
    assert result.y == -expected

    # Cleanup - none necessary


@pytest.mark.parametrize('instr,expected', make_rand_instrs('D'))
def test_move_down_from_random_y(instr, expected):
    # Setup
    pt_rand_y = day3.Point(7,random.randint(0,100))

    # Exercise
    result = day3.move_down(instr,pt_rand_y)

    # Verify
    assert result.x == 7
    assert result.y == pt_rand_y.y - expected

    # Cleanup - none necessary


wire_test_data = [
    (
        ['R8', 'U5', 'L5', 'D3'],
        [day3.Point(0,0), day3.Point(8,0), day3.Point(8,5), day3.Point(3,5), day3.Point(3,2)]
    ),
    (
        ['U7', 'R6', 'D4', 'L4'],
        [day3.Point(0,0), day3.Point(0,7), day3.Point(6,7), day3.Point(6,3), day3.Point(2,3)]
    ),
    (
        ['R75','D30','R83','U83','L12','D49','R71','U7','L72'],
        [day3.Point(0,0), day3.Point(75,0), day3.Point(75,-30), day3.Point(158,-30),
         day3.Point(158,53), day3.Point(146,53), day3.Point(146,4), day3.Point(217,4),
         day3.Point(217,11), day3.Point(145,11)]
    ),
    (
        ['U62','R66','U55','R34','D71','R55','D58','R83'],
        [day3.Point(0,0), day3.Point(0,62), day3.Point(66,62), day3.Point(66,117),
         day3.Point(100,117), day3.Point(100,46), day3.Point(155,46), day3.Point(155,-12),
         day3.Point(238,-12)]
    ),
    (
        ['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51'],
        [day3.Point(0,0), day3.Point(98,0), day3.Point(98,47), day3.Point(124,47),
         day3.Point(124,-16), day3.Point(157,-16), day3.Point(157,71), day3.Point(95,71),
         day3.Point(95,51), day3.Point(128,51), day3.Point(128,104), day3.Point(179,104)]
    ),
    (
        ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7'],
        [day3.Point(0,0), day3.Point(0,98), day3.Point(91,98), day3.Point(91,78),
         day3.Point(107,78), day3.Point(107,11), day3.Point(147,11), day3.Point(147,18),
         day3.Point(162,18), day3.Point(162,24), day3.Point(169,24)]
    ),
]


@pytest.mark.parametrize('wire_instr_list,expected', wire_test_data)
def test_collect_wire_points(wire_instr_list, expected):
    # Setup - none necessary

    # Exercise
    result = day3.collect_wire_points(wire_instr_list)

    # Verify
    assert result == expected

    # Cleanup - none necessary

