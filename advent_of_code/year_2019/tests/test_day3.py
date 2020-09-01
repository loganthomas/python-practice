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


wire_metapoints_test_data = [
    #             wire_points           ,         expected_metapoints
    ( [day3.Point(0,0), day3.Point(5,0)], {day3.Point(i,0) for i in range(6)} ),
    ( [day3.Point(0,0), day3.Point(0,5)], {day3.Point(0,i) for i in range(6)} ),
    (
        [day3.Point(0,0), day3.Point(8,0), day3.Point(8,5), day3.Point(3,5), day3.Point(3,2)],
        ({day3.Point(i,0) for i in range(9)} |
         {day3.Point(8,i) for i in range(6)} |
         {day3.Point(i,5) for i in range(8,2,-1)} |
         {day3.Point(3,i) for i in range(5,1,-1)})
    ),
    (
        [day3.Point(0,0), day3.Point(0,7), day3.Point(6,7), day3.Point(6,3), day3.Point(2,3)],
        ({day3.Point(0,i) for i in range(8)} |
         {day3.Point(i,7) for i in range(7)} |
         {day3.Point(6,i) for i in range(7,2,-1)} |
         {day3.Point(i,3) for i in range(6,1,-1)})
    ),
    (
        [day3.Point(0,0), day3.Point(75,0), day3.Point(75,-30), day3.Point(158,-30),
         day3.Point(158,53), day3.Point(146,53), day3.Point(146,4), day3.Point(217,4),
         day3.Point(217,11), day3.Point(145,11)],
        {day3.Point(x,y) for x,y in zip(
            [180, 92, 155, 158, 216, 75, 183, 217, 9, 170, 158, 145, 75, 61, 146, 158, 96, 146, 158,
             16, 201, 158, 152, 103, 68, 158, 156, 116, 158, 192, 75, 142, 146, 197, 39, 208, 198,
             107, 146, 75, 120, 213, 133, 158, 179, 204, 46, 127, 158, 75, 79, 137, 158, 150, 146,
             175, 199, 1, 53, 158, 189, 83, 157, 140, 158, 8, 75, 193, 217, 158, 60, 75, 146, 82,
             144, 146, 163, 158, 189, 31, 200, 153, 67, 102, 158, 217, 158, 171, 75, 75, 146, 196,
             38, 74, 146, 164, 106, 158, 200, 167, 158, 154, 45, 158, 206, 154, 126, 158, 75, 146,
             78, 0, 146, 185, 210, 52, 158, 131, 176, 207, 181, 23, 158, 192, 182, 75, 59, 158, 197,
             151, 146, 163, 146, 188, 30, 158, 66, 93, 155, 76, 158, 75, 159, 217, 183, 158, 75, 37,
             146, 173, 97, 73, 146, 209, 80, 158, 177, 202, 44, 117, 158, 100, 158, 147, 75, 146,
             158, 173, 15, 184, 146, 51, 121, 210, 158, 104, 158, 155, 130, 180, 22, 150, 158, 58,
             75, 148, 146, 124, 184, 146, 151, 150, 29, 190, 214, 158, 158, 65, 141, 154, 158, 75,
             169, 194, 36, 158, 146, 72, 87, 145, 160, 146, 191, 165, 7, 176, 166, 43, 181, 91, 158,
             75, 217, 158, 147, 75, 172, 146, 14, 158, 50, 146, 111, 158, 167, 158, 203, 21, 158,
             206, 157, 57, 115, 151, 158, 75, 193, 146, 146, 161, 186, 28, 64, 158, 114, 204, 157,
             128, 168, 158, 75, 35, 146, 194, 146, 135, 86, 148, 164, 6, 158, 42, 147, 77, 155, 139,
             158, 168, 90, 152, 158, 13, 174, 198, 146, 49, 81, 146, 110, 158, 153, 178, 20, 158,
             56, 101, 217, 158, 146, 175, 158, 149, 160, 150, 146, 211, 27, 158, 105, 165, 201, 158,
             158, 156, 158, 34, 75, 125, 146, 108, 146, 151, 212, 134, 187, 5, 190, 158, 215, 41,
             202, 177, 112, 158, 75, 138, 170, 12, 158, 146, 48, 188, 84, 158, 152, 19, 178, 71,
             158, 149, 75, 217, 157, 158, 88, 75, 148, 146, 26, 146, 211, 95, 158, 152, 158, 182,
             207, 33, 158, 99, 75, 146, 146, 162, 4, 158, 40, 119, 158, 153, 129, 159, 158, 195, 75,
             11, 146, 149, 123, 63, 146, 185, 149, 132, 158, 18, 203, 70, 158, 153, 75, 196, 158,
             136, 171, 174, 146, 199, 25, 186, 146, 161, 94, 156, 154, 158, 32, 75, 217, 158, 75,
             172, 98, 146, 158, 208, 146, 3, 162, 158, 213, 55, 214, 118, 158, 158, 10, 195, 75,
             146, 109, 62, 158, 122, 146, 166, 191, 158, 17, 215, 113, 69, 205, 158, 143, 75, 146,
             24, 146, 209, 85, 147, 179, 148, 205, 47, 158, 216, 156, 169, 89, 158, 146, 146, 2,
             146, 187, 212, 54, 158],
            [11, -30, 11, 4, 11, -26, 4, 10, 0, 11, 46, 11, -4, 0, 16, 48, -30, 42, -23, 0, 4, -13,
             53, -30, 0, 15, 11, -30, 17, 11, -11, -30, 11, 4, 0, 4, 11, -30, 37, 0, -30, 11, -30,
             -6, 4, 4, 0, -30, 24, -22, -30, -30, 34, 4, 28, 4, 11, 0, 0, -3, 11, -30, -30, -30, 3,
             0, -29, 4, 7, 37, 0, -7, 23, -30, -30, 49, 11, -28, 4, 0, 4, 11, 0, -30, 10, 8, 44, 4,
             -2, -1, 14, 4, 0, 0, 40, 11, -30, -17, 11, 4, -15, 11, 0, 13, 11, 53, -30, 23, -9, 9,
             -30, 0, 35, 4, 4, 0, -8, -30, 11, 11, 4, 0, 30, 4, 11, -20, 0, 32, 11, -30, 26, 4, 52,
             4, 0, -29, 0, -30, -30, -30, 1, -27, 4, 5, 11, 43, -5, 0, 21, 11, -30, 0, 47, 11, -30,
             -22, 4, 4, 0, -30, 8, -30, 18, 11, -16, 12, 52, 4, 0, 4, 38, 0, -30, 11, -19, -30, -9,
             4, -30, 4, 0, 53, 21, 0, -23, 11, 7, -30, 11, 33, 4, -30, 0, 11, 4, -2, -1, 0, -30,
             -30, 28, -18, 4, 4, 0, 38, 24, 0, -30, -30, 11, 50, 11, 4, 0, 4, 11, 0, 11, -30, 7,
             -25, 11, 41, 4, -3, 4, 19, 0, 51, 0, 45, -30, -24, 11, -14, 11, 0, 14, 4, 11, 0, -30,
             53, 16, -14, 11, 10, 36, 4, 4, 0, 0, -11, -30, 11, 4, -30, 4, 27, -21, 0, 5, 11, 31,
             -30, -30, -30, 4, 0, -4, 0, 53, -30, 53, -30, 2, 11, -30, -30, 36, 0, 11, 4, 22, 0,
             -30, 48, -30, -25, 4, 4, 0, 5, 0, -30, 9, 47, 17, 11, 49, 4, 4, 11, 43, 11, 0, -18,
             -30, 11, 11, -16, 12, 4, 22, 0, -12, -30, 8, -30, 34, 11, 11, -30, 11, 0, 4, -5, 4, 0,
             11, 11, -30, 25, -19, -30, 4, 0, 35, 29, 0, 11, -30, -30, 4, 0, 11, 0, 0, 53, -30, 6,
             53, 42, -30, -8, 4, 20, 0, 46, 4, -30, -27, 11, 11, 4, 4, 0, 45, -30, -15, 15, 41, 4,
             0, -20, 0, -30, -10, 53, -30, 11, 20, 11, -10, 0, 6, 11, -30, 0, 32, 11, -30, -30, -7,
             0, 4, 0, 31, -30, -17, 11, 33, -30, 11, 4, 27, 4, 0, 11, 53, 11, -30, -30, 4, 6, 0,
             -28, 4, 40, -6, 11, -30, 18, 50, 11, 44, 0, 11, -21, 4, 0, 11, -30, 9, 19, 0, 4, -13,
             13, -30, 0, 53, -30, 39, 4, 4, -12, 0, 11, -30, 0, 11, 26, -30, -24, 4, 0, 30, 4, -30,
             -30, 11, 53, 4, 0, 29, 4, 53, 11, -30, 39, 25, -30, 0, 51, 4, 4, 0, -26]
        )}
    ),
    (
        [day3.Point(0,0), day3.Point(0,62), day3.Point(66,62), day3.Point(66,117),
         day3.Point(100,117), day3.Point(100,46), day3.Point(155,46), day3.Point(155,-12),
         day3.Point(238,-12)],
        {day3.Point(x,y) for x,y in zip(
            [100, 155, 177, 100, 152, 9, 155, 202, 100, 42, 155, 187, 212, 0, 66, 0, 103, 0, 53,
             155, 155, 60, 201, 100, 128, 155, 165, 18, 211, 134, 66, 175, 0, 100, 0, 100, 155, 29,
             155, 100, 237, 36, 117, 136, 66, 0, 100, 107, 124, 174, 66, 86, 0, 66, 47, 114, 168,
             100, 155, 75, 64, 100, 5, 100, 155, 12, 0, 90, 66, 0, 194, 66, 0, 155, 23, 204, 100,
             155, 155, 40, 81, 100, 111, 155, 0, 100, 101, 66, 0, 100, 51, 193, 218, 0, 157, 58,
             203, 155, 142, 155, 155, 228, 167, 100, 16, 132, 66, 0, 100, 66, 0, 27, 217, 66, 100,
             155, 181, 71, 155, 34, 227, 100, 115, 166, 191, 100, 122, 105, 66, 160, 0, 100, 66,
             112, 0, 66, 100, 3, 155, 100, 77, 10, 100, 190, 155, 78, 0, 184, 66, 0, 91, 66, 67, 21,
             0, 54, 155, 155, 100, 155, 210, 0, 66, 49, 0, 100, 220, 0, 56, 97, 73, 155, 30, 100,
             76, 209, 118, 151, 234, 66, 173, 0, 100, 25, 66, 108, 219, 141, 0, 183, 66, 32, 100,
             155, 100, 6, 120, 100, 155, 66, 233, 126, 0, 66, 197, 87, 1, 66, 182, 100, 207, 155,
             72, 8, 176, 155, 100, 155, 0, 45, 66, 145, 19, 102, 0, 52, 93, 0, 69, 206, 155, 155,
             100, 200, 155, 63, 164, 0, 83, 66, 0, 100, 0, 28, 100, 226, 155, 100, 116, 149, 236,
             163, 66, 39, 106, 139, 0, 100, 89, 66, 0, 46, 66, 100, 68, 155, 4, 225, 100, 66, 189,
             100, 235, 155, 199, 0, 66, 15, 0, 66, 100, 22, 155, 100, 74, 155, 153, 110, 100, 155,
             213, 43, 79, 0, 100, 198, 66, 223, 0, 50, 100, 192, 0, 156, 80, 155, 100, 61, 129, 66,
             135, 85, 0, 100, 222, 66, 26, 0, 170, 66, 216, 100, 155, 155, 180, 147, 99, 100, 37,
             104, 137, 66, 0, 100, 66, 125, 0, 66, 169, 2, 100, 155, 100, 65, 179, 100, 155, 13, 0,
             66, 84, 0, 146, 20, 66, 0, 205, 155, 100, 155, 155, 215, 41, 100, 155, 0, 48, 66, 0,
             100, 0, 229, 59, 155, 82, 95, 143, 100, 214, 17, 162, 150, 133, 208, 66, 0, 24, 100,
             172, 96, 140, 66, 0, 66, 100, 155, 155, 100, 35, 100, 238, 161, 66, 186, 123, 0, 232,
             66, 171, 0, 196, 113, 66, 94, 100, 155, 155, 100, 154, 11, 44, 0, 185, 144, 66, 0, 195,
             0, 159, 55, 155, 155, 100, 155, 62, 130, 0, 66, 221, 0, 92, 100, 0, 231, 57, 158, 100,
             70, 155, 100, 31, 148, 131, 38, 119, 66, 138, 0, 100, 66, 0, 109, 98, 66, 230, 100, 33,
             155, 178, 100, 224, 66, 7, 100, 121, 188, 155, 88, 66, 0, 14, 127, 66, 0, 66],
            [106, 21, -12, 112, 46, 62, 11, -12, 94, 62, 33, -12, -12, 17, 66, 55, 46, 45, 62, -4,
             0, 62, -12, 69, 46, 38, -12, 62, -12, 46, 93, -12, 14, 50, 36, 102, -11, 62, 25, 76,
             -12, 62, 46, 46, 84, 5, 57, 46, 46, -12, 78, 117, 59, 104, 62, 46, -12, 109, 30, 117,
             62, 75, 62, 81, 42, 62, 28, 117, 73, 50, -12, 99, 40, 23, 62, -12, 114, -7, 13, 62,
             117, 88, 46, 35, 19, 47, 46, 64, 9, 53, 62, -12, -12, 47, -12, 62, -12, -2, 46, -1, 2,
             -12, -12, 71, 62, 46, 91, 0, 60, 117, 38, 62, -12, 111, 96, -9, -12, 117, 27, 62, -12,
             78, 46, -12, -12, 84, 46, 46, 82, -12, 7, 59, 76, 46, 61, 102, 111, 62, 16, 117, 117,
             62, 83, -12, 44, 117, 30, -12, 71, 52, 117, 97, 117, 62, 42, 62, -5, 15, 90, 37, -12,
             21, 94, 62, 11, 55, -12, 33, 62, 117, 117, 4, 62, 65, 117, -12, 46, 46, -12, 89, -12,
             2, 62, 62, 115, 46, -12, 46, 56, -12, 109, 62, 98, 29, 72, 62, 46, 86, 41, 80, -12, 46,
             25, 74, -12, 117, 62, 100, -12, 105, -12, 18, 117, 62, -12, 8, 93, 46, 16, 62, 69, 46,
             62, 46, 54, 62, 117, 44, 117, -12, -3, 1, 68, -12, 39, 62, -12, 23, 117, 92, 13, 49,
             35, 62, 101, -12, 6, 67, 46, 46, -12, -12, 87, 62, 46, 46, 4, 56, 117, 113, 58, 62,
             107, 108, 117, 31, 62, -12, 74, 63, -12, 80, -12, 43, -12, 27, 72, 62, 49, 98, 107, 62,
             20, 113, 117, 10, 46, 46, 95, 32, -12, 62, 117, 18, 46, -12, 67, -12, 8, 62, 52, -12,
             46, -12, 117, 3, 70, 62, 46, 90, 46, 117, 15, 51, -12, 116, 62, 37, -12, 110, -12, 103,
             -12, 24, -12, 46, 117, 77, 62, 46, 46, 85, 6, 58, 79, 46, 60, 105, -12, 62, 110, 17,
             116, 62, -12, 82, 45, 62, 29, 70, 117, 51, 46, 62, 96, 41, -12, 22, 115, -8, 12, -12,
             62, 89, 34, 20, 62, 65, 10, 54, 32, -12, 62, 5, 117, 117, 46, 64, -12, 62, -12, 46, 46,
             -12, 88, 1, 62, 61, -12, 117, 46, 114, 39, 108, 97, -10, 26, 79, 62, 85, -12, -12, 83,
             -12, 46, 24, -12, 77, -12, 62, -12, 46, 103, 117, 104, 19, 9, 92, 46, 62, 62, 31, -12,
             46, 68, 53, -12, 43, -12, 62, -6, 14, 91, 36, 62, 46, 22, 95, -12, 12, 117, 48, 34,
             -12, 62, -12, 100, 117, 7, 66, 62, 46, 46, 62, 46, 86, 46, 3, 63, 112, 57, 46, 117,
             106, -12, 99, 62, 28, -12, 73, -12, 62, 62, 87, 46, -12, 40, 117, 81, 26, 62, 46, 75,
             48, 101]
        )}
    ),
    (
        [day3.Point(0,0), day3.Point(98,0), day3.Point(98,47), day3.Point(124,47),
         day3.Point(124,-16), day3.Point(157,-16), day3.Point(157,71), day3.Point(95,71),
         day3.Point(95,51), day3.Point(128,51), day3.Point(128,104), day3.Point(179,104)],
        {day3.Point(x,y) for x,y in zip(
            [157, 133, 134, 90, 157, 116, 143, 125, 128, 157, 9, 139, 124, 98, 128, 61, 157, 124,
             98, 137, 155, 95, 129, 97, 128, 102, 157, 124, 98, 145, 147, 95, 135, 157, 16, 160,
             157, 68, 140, 176, 157, 128, 157, 98, 95, 39, 124, 98, 101, 75, 109, 124, 155, 46, 157,
             146, 116, 82, 128, 157, 124, 106, 104, 124, 98, 131, 1, 102, 147, 124, 53, 163, 89,
             161, 128, 98, 157, 8, 128, 157, 124, 126, 60, 128, 142, 124, 98, 96, 124, 98, 103, 135,
             31, 133, 157, 67, 129, 128, 169, 157, 110, 157, 124, 139, 128, 157, 100, 98, 38, 128,
             149, 157, 154, 74, 98, 124, 148, 95, 157, 110, 45, 153, 100, 157, 81, 128, 157, 98, 95,
             0, 124, 98, 52, 154, 124, 88, 170, 157, 23, 128, 104, 157, 59, 125, 123, 124, 98, 156,
             124, 113, 30, 96, 146, 66, 128, 157, 120, 102, 128, 157, 124, 128, 37, 157, 124, 98,
             73, 128, 124, 98, 157, 128, 44, 157, 144, 141, 80, 157, 128, 157, 151, 98, 152, 95, 15,
             128, 157, 124, 98, 51, 145, 95, 113, 157, 155, 22, 157, 125, 166, 58, 128, 157, 98, 95,
             119, 124, 98, 109, 124, 29, 131, 129, 114, 65, 145, 128, 157, 128, 121, 157, 124, 36,
             124, 98, 72, 124, 98, 144, 7, 157, 157, 137, 151, 132, 43, 121, 111, 157, 95, 167, 117,
             128, 157, 142, 127, 124, 101, 128, 157, 124, 14, 98, 95, 136, 117, 128, 157, 50, 124,
             98, 152, 103, 132, 130, 95, 157, 168, 128, 157, 21, 110, 157, 118, 57, 173, 128, 157,
             98, 95, 124, 98, 95, 28, 124, 174, 157, 138, 64, 123, 97, 111, 157, 119, 117, 128, 113,
             35, 157, 124, 103, 95, 87, 124, 98, 107, 105, 153, 119, 124, 6, 148, 109, 42, 128, 94,
             157, 138, 96, 128, 157, 124, 13, 124, 98, 49, 106, 124, 98, 175, 134, 157, 20, 157,
             128, 99, 56, 111, 157, 124, 138, 115, 128, 157, 124, 98, 95, 101, 99, 128, 157, 124,
             98, 107, 148, 27, 105, 95, 79, 157, 150, 157, 140, 152, 34, 128, 157, 98, 86, 95, 130,
             100, 124, 98, 108, 124, 5, 41, 93, 115, 157, 122, 128, 157, 124, 124, 12, 105, 124, 48,
             98, 128, 124, 107, 114, 136, 19, 128, 135, 157, 71, 171, 128, 121, 127, 157, 142, 124,
             128, 157, 124, 98, 132, 26, 124, 98, 136, 78, 150, 157, 130, 128, 157, 141, 140, 157,
             33, 124, 122, 99, 177, 128, 85, 157, 98, 150, 114, 128, 157, 124, 98, 4, 95, 144, 157,
             40, 158, 156, 92, 154, 149, 172, 157, 123, 128, 11, 157, 98, 95, 63, 124, 98, 134, 124,
             18, 120, 164, 162, 128, 70, 157, 128, 178, 157, 126, 124, 124, 122, 124, 98, 25, 116,
             143, 112, 126, 124, 98, 77, 179, 159, 157, 106, 128, 131, 157, 151, 32, 128, 157, 124,
             84, 128, 141, 157, 124, 98, 95, 128, 157, 124, 98, 3, 127, 149, 55, 157, 165, 91, 128,
             157, 157, 10, 128, 112, 157, 98, 62, 157, 124, 98, 146, 118, 95, 112, 157, 156, 147,
             17, 108, 69, 157, 137, 128, 157, 118, 98, 153, 95, 143, 24, 98, 124, 108, 76, 124, 133,
             115, 128, 157, 139, 47, 120, 97, 128, 157, 83, 124, 124, 98, 2, 124, 98, 104, 54],
            [-3, -16, 104, 0, 23, 51, -16, -16, 87, 49, 0, 71, -15, 51, 77, 0, 43, 34, 45, -16, 71,
             55, 71, 0, 99, 47, 69, 24, 7, 71, -16, 68, 71, -10, 0, 104, 16, 0, 104, 104, 10, 68,
             36, 36, 60, 0, 23, 30, 51, 0, 51, 13, 104, 0, 3, 104, 47, 0, 91, 61, -3, 47, 51, 46,
             25, 71, 0, 51, 104, 4, 0, 104, 0, 104, 60, 71, 28, 0, 82, 54, -12, -16, 0, 72, 104, 37,
             16, 0, 3, 10, 51, -16, 0, 104, -5, 0, -16, 51, 104, 21, 47, 15, -13, -16, 79, 41, 47,
             43, 0, 101, -16, 67, 71, 0, 5, 26, 104, 70, -12, 71, 0, -16, 71, 8, 0, 70, 34, 34, 62,
             0, 17, 28, 0, 104, 15, 0, 104, 1, 0, 93, 47, 59, 0, 51, 47, 40, 23, 71, 6, 47, 0, 71,
             71, 0, 62, 26, 51, 71, 84, 52, -10, 74, 0, 46, 39, 46, 0, 96, 29, 8, -7, 53, 0, 19,
             104, -16, 0, 13, 65, 39, -16, 41, 71, 51, 0, 103, 65, 20, 3, 0, -16, 64, 51, -14, -16,
             0, 6, 71, 104, 0, 88, 32, 32, 56, 47, 19, 26, 47, 9, 0, 104, 104, 51, 0, 104, 57, 31,
             95, 47, 57, -7, 0, 42, 21, 0, 0, 15, 71, 0, -2, -1, 104, 104, -16, 0, 71, 71, 24, 0,
             104, 51, 86, 50, -16, 71, -16, 71, 76, 44, 33, 0, 44, 52, -16, 71, 98, 70, 0, 31, 6,
             104, 47, 104, 104, 69, -9, 104, 55, 17, 0, 51, 11, 51, 0, 104, 67, 37, 39, 61, 22, 1,
             66, 0, 12, 104, -16, 104, 0, 71, 71, 51, 4, 51, 47, 90, 71, 0, 62, -4, 71, 58, 0, 45,
             24, 47, 51, 104, 71, 11, 0, 71, 71, 0, 59, 0, 29, 71, 51, 81, 55, -5, 0, 36, 19, 0, 51,
             2, 13, 104, -16, -4, 0, 22, -16, 71, 0, 47, 48, -14, -16, 71, 78, 42, 35, 42, 54, 47,
             51, 100, 68, 25, 4, 51, -16, 0, 71, 71, 0, -11, 71, 9, 71, -16, 0, 69, 35, 37, 0, 63,
             71, 51, 16, 31, 51, 14, 0, 0, 0, 47, 2, 71, 92, 60, -2, -1, 0, 47, 47, 0, 22, 104, 5,
             71, 47, 71, 0, 61, 104, 27, 0, 104, 83, 51, -16, 53, 71, -11, 73, 47, 38, 17, 71, 0,
             28, 11, 104, 0, 104, -6, -16, 52, 20, 104, -16, 14, 0, 71, 51, 47, 104, 64, 0, 40, 40,
             -16, 71, 102, 66, 27, 2, 0, 65, -16, -13, 0, 104, 104, 0, -16, 71, 104, 7, 51, 71, 0,
             33, 35, 57, 0, 18, 29, 71, 8, 0, 71, 104, 104, 56, 0, 0, 94, 104, 58, 71, 51, -8, 47,
             41, 20, 0, 71, 104, 47, 51, 7, 14, 0, 104, 104, 104, 71, 63, -16, 25, 71, 0, 85, 51,
             -9, 0, 75, 71, 45, 32, 47, 53, 97, 71, 30, 9, 0, 51, 104, 0, -8, 104, 0, 54, 18, 12, 0,
             66, 71, 38, 38, 0, 64, 21, 0, -16, 71, 67, 51, -15, -16, 71, 0, 71, 0, 5, 71, 89, 63,
             47, 33, 71, 59, 71, 0, 27, 44, 47, 0, 10, 71, 51, 58, 30, 104, 0, 47, 51, 80, 56, 0,
             -6, 43, 18, 0, 1, 12, 71, 0]
        )}
    ),
    (
        [day3.Point(0,0), day3.Point(0,98), day3.Point(91,98), day3.Point(91,78),
         day3.Point(107,78), day3.Point(107,11), day3.Point(147,11), day3.Point(147,18),
         day3.Point(162,18), day3.Point(162,24), day3.Point(169,24)],
        {day3.Point(x,y) for x,y in zip(
            [0, 0, 0, 52, 145, 26, 0, 91, 107, 6, 88, 78, 0, 7, 42, 104, 107, 43, 0, 0, 147, 146,
             107, 151, 0, 91, 107, 0, 112, 0, 96, 118, 102, 28, 0, 92, 107, 64, 44, 0, 107, 18, 80,
             165, 0, 70, 119, 0, 33, 91, 107, 109, 162, 85, 0, 107, 0, 0, 0, 91, 107, 0, 107, 139,
             0, 107, 0, 129, 147, 19, 107, 120, 35, 0, 107, 9, 87, 126, 0, 107, 61, 140, 164, 0,
             154, 77, 130, 100, 0, 107, 161, 0, 107, 127, 0, 117, 0, 20, 56, 0, 91, 46, 107, 10, 0,
             107, 11, 62, 0, 63, 156, 0, 25, 158, 147, 0, 91, 107, 0, 137, 107, 0, 91, 107, 163,
             153, 0, 147, 107, 0, 32, 107, 12, 138, 84, 0, 48, 107, 38, 0, 74, 148, 27, 107, 1, 110,
             79, 94, 0, 91, 107, 53, 17, 162, 0, 89, 107, 69, 0, 155, 0, 0, 111, 0, 91, 107, 0, 107,
             0, 0, 76, 97, 2, 147, 169, 0, 91, 107, 3, 54, 103, 0, 55, 90, 107, 123, 93, 91, 0, 107,
             71, 45, 0, 113, 131, 81, 147, 159, 0, 107, 0, 124, 107, 0, 114, 132, 24, 107, 4, 0, 91,
             107, 40, 162, 30, 0, 107, 66, 0, 82, 0, 144, 168, 0, 91, 107, 0, 107, 0, 107, 0, 101,
             147, 107, 121, 0, 91, 107, 16, 0, 107, 68, 141, 0, 167, 107, 47, 21, 160, 0, 83, 107,
             122, 57, 162, 37, 0, 107, 73, 0, 0, 108, 0, 91, 107, 162, 0, 107, 0, 0, 22, 0, 91, 107,
             23, 58, 0, 107, 59, 39, 0, 13, 91, 107, 152, 75, 49, 0, 128, 166, 99, 134, 147, 107, 0,
             107, 105, 95, 0, 107, 0, 115, 135, 107, 8, 0, 91, 107, 60, 162, 34, 0, 107, 86, 0, 50,
             116, 0, 0, 150, 29, 0, 91, 107, 65, 0, 107, 0, 106, 0, 157, 0, 91, 107, 136, 0, 107,
             36, 0, 107, 142, 72, 0, 14, 98, 15, 107, 51, 31, 0, 5, 107, 67, 0, 41, 107, 125, 143,
             0, 133, 107, 149, 0, 91, 107, 162, 0, 107],
            [86, 76, 98, 98, 11, 98, 17, 80, 26, 98, 98, 98, 55, 98, 98, 78, 48, 98, 45, 67, 12, 11,
             19, 18, 14, 79, 41, 36, 11, 90, 78, 11, 78, 98, 5, 78, 46, 98, 98, 59, 68, 98, 98, 24,
             81, 98, 11, 28, 98, 93, 39, 11, 18, 98, 50, 61, 40, 78, 19, 82, 28, 9, 50, 11, 47, 72,
             69, 11, 14, 98, 21, 11, 98, 0, 43, 98, 98, 11, 38, 65, 98, 11, 24, 92, 18, 98, 11, 78,
             7, 32, 18, 61, 70, 11, 83, 11, 73, 98, 98, 30, 95, 98, 25, 98, 52, 63, 98, 98, 42, 98,
             18, 64, 98, 18, 11, 21, 84, 30, 11, 11, 52, 33, 96, 74, 24, 18, 71, 16, 23, 2, 98, 45,
             98, 11, 98, 56, 98, 67, 98, 94, 98, 18, 98, 12, 98, 11, 98, 78, 25, 88, 34, 98, 98, 23,
             63, 98, 56, 98, 85, 18, 75, 97, 11, 16, 81, 27, 54, 49, 44, 66, 98, 78, 98, 13, 24, 23,
             86, 16, 98, 98, 78, 13, 98, 98, 54, 11, 78, 98, 35, 76, 98, 98, 89, 11, 11, 98, 18, 18,
             4, 47, 58, 11, 69, 80, 11, 11, 98, 14, 98, 27, 90, 36, 98, 21, 98, 49, 58, 98, 87, 98,
             77, 11, 24, 18, 83, 29, 8, 51, 46, 73, 68, 78, 15, 18, 11, 15, 78, 40, 98, 37, 78, 98,
             11, 91, 24, 11, 98, 98, 18, 6, 98, 33, 11, 98, 24, 98, 60, 71, 98, 82, 72, 11, 29, 92,
             38, 19, 51, 60, 41, 79, 98, 20, 85, 31, 98, 98, 10, 53, 98, 98, 32, 98, 97, 75, 18, 98,
             98, 70, 11, 24, 78, 11, 17, 20, 1, 42, 78, 78, 39, 64, 93, 11, 11, 13, 98, 24, 89, 35,
             98, 22, 98, 62, 57, 98, 84, 98, 11, 74, 96, 18, 98, 31, 94, 24, 98, 53, 62, 43, 78, 65,
             18, 22, 87, 17, 11, 12, 55, 98, 34, 77, 11, 98, 88, 98, 78, 98, 22, 98, 98, 3, 98, 44,
             98, 57, 98, 66, 11, 11, 95, 11, 15, 18, 26, 91, 37, 20, 48, 59]
        )}
    )
]


@pytest.mark.parametrize(
    'wire_points, expected', wire_metapoints_test_data,
    ids=['only_x_vals', 'only_y_vals', 'provided_example_1_wire1', 'provided_example_1_wire2',
         'provided_example_2_wire1', 'provided_example_2_wire2', 'provided_example_3_wire1',
         'provided_example_3_wire2']
)
def test_collect_wire_metapoints(wire_points, expected):
    # Setup - none necessary

    # Exercise
    result = day3.collect_wire_metapoints(wire_points)

    # Verify
    assert result == expected

    # Cleanup - none necessary


intersection_test_data = [
    #   wire1_instr, wire2_instr, expected_intersections
    (
        ['R5', 'U5', 'L5'],
        ['U5'],
        [day3.Point(0,5)]
    ),
    (
        ['U5', 'R5'],
        ['R5', 'U5'],
        [day3.Point(5,5)]
    ),
    (
        ['R8', 'U5', 'L5', 'D3'],
        ['U7', 'R6', 'D4', 'L4'],
        [day3.Point(3,3), day3.Point(6,5)]
    ),
    (
        ['R75','D30','R83','U83','L12','D49','R71','U7','L72'],
        ['U62','R66','U55','R34','D71','R55','D58','R83'],
        [day3.Point(158,-12), day3.Point(146,46), day3.Point(155,4), day3.Point(155,11)]
    ),
    (
        ['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51'],
        ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7'],
        [day3.Point(107,71), day3.Point(157,18), day3.Point(124,11),
         day3.Point(107,47), day3.Point(107,51)]
    ),
]


@pytest.mark.parametrize(
    'wire1_instr, wire2_instr, expected', intersection_test_data,
    ids=['simple_inter_(0,5)', 'simple_inter_(5,5)', 'provided_example_1',
         'provided_example_2','provided_example_3']
)
def test_find_intersections(wire1_instr, wire2_instr, expected):
    # Setup
    wire1_points = day3.collect_wire_points(wire1_instr)
    wire2_points = day3.collect_wire_points(wire2_instr)

    wire1_metapoints = day3.collect_wire_metapoints(wire1_points)
    wire2_metapoints = day3.collect_wire_metapoints(wire2_points)

    # Exercise
    result = day3.find_intersections(wire1_metapoints, wire2_metapoints)

    # Verify
    assert result == expected

    # Cleanup - none necessary


closest_point_test_data = [
    # provided_intersections, expected_closest_point_dist
    (
        [day3.Point(0,5)],
        (day3.Point(0,5), 5)
    ),
    (
        [day3.Point(5,5)],
        (day3.Point(5,5), 10)
    ),
    (
        [day3.Point(0,5), day3.Point(5,5)],
        (day3.Point(0,5), 5)
    ),
    (
        [day3.Point(3,3), day3.Point(6,5)],
        (day3.Point(3,3), 6)
    ),
    (
        [day3.Point(158,-12), day3.Point(146,46), day3.Point(155,4), day3.Point(155,11)],
        (day3.Point(155,4), 159)
    ),
    (
        [day3.Point(107,71), day3.Point(157,18), day3.Point(124,11),
         day3.Point(107,47), day3.Point(107,51)],
        (day3.Point(124,11), 135)
    ),
]


@pytest.mark.parametrize(
    'intersections, expected', closest_point_test_data,
    ids=['simple_inter_(0,5)', 'simple_inter_(5,5)', 'simple_inter_(0,5)_(5,5)',
         'provided_example_1','provided_example_2','provided_example_3']
)
def test_find_closest_point_to_center(intersections, expected):
    # Setup - none necessary

    # Exercise
    result = day3.find_closest_point_to_center(intersections)

    # Verify
    assert result == expected

    # Cleanup - none necessary


@pytest.mark.mpl_image_compare(remove_text=True)
def test_plot_wires_provided_1():
    """
    Notes:
        - Remove text as pytest-mpl is finicky with text.
          This will remove (titles, axes, labels, etc.)
        - First run needs to specify where to store base image for
          comparison later on:
          pytest -k test_plot_wires_provided_1 --mpl-generate-path=advent_of_code/year_2019/tests/baseline
        - Above must have "baseline" as directory
    """
    # Setup
    wire1_points     = day3.collect_wire_points(['R8', 'U5', 'L5', 'D3'])
    wire2_points     = day3.collect_wire_points(['U7', 'R6', 'D4', 'L4'])
    wire1_metapoints = day3.collect_wire_metapoints(wire1_points)
    wire2_metapoints = day3.collect_wire_metapoints(wire2_points)
    intersections    = day3.find_intersections(wire1_metapoints,wire2_metapoints)
    pt, dist         = day3.find_closest_point_to_center(intersections)

    # Exercise
    fig = day3.plot_wires(wire1_points, wire2_points, intersections, pt)

    # Verify - image done by pytest-mpl
    assert pt   == day3.Point(3,3)
    assert dist == 6

    # Cleanup - none necessary

    # Required for pytest-mpl for image testing
    return fig


@pytest.mark.mpl_image_compare()
def test_plot_wires_provided_2():
    """ Need to write this test. See SciPy tutorial for using images..."""
    # Setup
    wire1_points     = day3.collect_wire_points(['R75','D30','R83','U83','L12','D49','R71','U7','L72'])
    wire2_points     = day3.collect_wire_points(['U62','R66','U55','R34','D71','R55','D58','R83'])
    wire1_metapoints = day3.collect_wire_metapoints(wire1_points)
    wire2_metapoints = day3.collect_wire_metapoints(wire2_points)
    intersections    = day3.find_intersections(wire1_metapoints,wire2_metapoints)
    pt, dist         = day3.find_closest_point_to_center(intersections)

    # Exercise
    fig = day3.plot_wires(wire1_points, wire2_points, intersections, pt)

    # Verify - imaged done by pytest-mpl
    assert pt   == day3.Point(155, 4)
    assert dist == 159

    # Cleanup - none necessary

    # Required for pytest-mpl for image testing
    return fig


@pytest.mark.mpl_image_compare()
def test_plot_wires_provided_3():
    """ Need to write this test. See SciPy tutorial for using images..."""
    # Setup
    wire1_points     = day3.collect_wire_points(['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51'])
    wire2_points     = day3.collect_wire_points(['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7'])
    wire1_metapoints = day3.collect_wire_metapoints(wire1_points)
    wire2_metapoints = day3.collect_wire_metapoints(wire2_points)
    intersections    = day3.find_intersections(wire1_metapoints,wire2_metapoints)
    pt, dist         = day3.find_closest_point_to_center(intersections)

    # Exercise

    fig = day3.plot_wires(wire1_points, wire2_points, intersections, pt)

    # Verify - image done by pytest-mpl
    assert pt   == day3.Point(124, 11)
    assert dist == 135

    # Cleanup - none necessary

    # Required for pytest-mpl for image testing
    return fig


@pytest.mark.mpl_image_compare()
def test_part_1_answer():
    # Setup
    data_path = Path('advent_of_code/year_2019/data/day3_puzzle.txt')
    text = data_path.read_text().strip().split('\n')
    wire1_text = text[0].split(',')
    wire2_text = text[1].split(',')

    # Exercise
    wire1_points = day3.collect_wire_points(wire1_text)
    wire2_points = day3.collect_wire_points(wire2_text)

    wire1_metapoints = day3.collect_wire_metapoints(wire1_points)
    wire2_metapoints = day3.collect_wire_metapoints(wire2_points)

    intersections = day3.find_intersections(wire1_metapoints,wire2_metapoints)

    pt, dist = day3.find_closest_point_to_center(intersections)

    fig = day3.plot_wires(wire1_points, wire2_points, intersections, pt)

    # Verify
    assert pt   == day3.Point(-330,2097)
    assert dist == 2427  # Answer to submit

    # Cleanup - none necessary

    # Required for pytest-mpl for image testing
    return fig
