from advent_of_code.year_2019 import day2
from pathlib import Path
import pytest


def test_day2_part1_perform_opr_add():
    # Setup
    data = [1,2,3,2]
    expected = [1,2,5,2]

    # Exercise
    result = day2.perform_opr(data,0)

    # Verify
    assert result == expected

    # Cleanup - none necessary


def test_day2_part1_perform_opr_mult():
    # Setup
    data = [2,2,3,2]
    expected = [2,2,6,2]

    # Exercise
    result = day2.perform_opr(data,0)

    # Verify
    assert result == expected

    # Cleanup - none necessary


def test_day2_part1_perform_opr_fail():
    # Setup
    data = [11,2,3,2]

    # Exercise
    with pytest.raises(ValueError) as e:
        day2.perform_opr(data,0)

    # Verify
    assert e.type == ValueError
    assert "Did not recognize opr=11 as '1', '2', or '99'" == str(e.value)

    # Cleanup - none necessary


day2_provided_data = [
    # data                         , expected
    ([1,9,10,3,2,3,11,0,99,30,40,50], [3500,9,10,70,2,3,11,0,99,30,40,50]),
    ([1,0,0,0,99], [2,0,0,0,99]),
    ([2,3,0,3,99], [2,3,0,6,99]),
    ([2,4,4,5,99,0], [2,4,4,5,99,9801]),
    ([1,1,1,4,99,5,6,0,99], [30,1,1,4,2,5,6,0,99]),
]


@pytest.mark.parametrize('data,expected', day2_provided_data)
def test_day2_part1_update_list_provided_exercises(data, expected):
    # Setup - none necessary

    # Exercise
    result = day2.update_list(data)

    # Verify
    assert result == expected

    # Cleanup - none necessary


def test_day2_part1_answer():
    # Setup
    data_path = Path('advent_of_code/year_2019/data/day2_puzzle.txt')
    expected = 3516593

    # Exercise
    result = day2.part_1_answer(data_path)

    # Verify
    assert result == expected

    # Cleanup - none necessary


def test_day2_part2_with_part1_answer():
    # Setup
    data_path = Path('advent_of_code/year_2019/data/day2_puzzle.txt')
    expected = (12, 2, 1202)

    # Exercise
    result = day2.part_2_answer(data_path, 3516593)

    # Verify
    assert result == expected

    # Cleanup - none necessary


def test_day2_part2_answer():
    # Setup
    data_path = Path('advent_of_code/year_2019/data/day2_puzzle.txt')
    expected = (77, 49, 7749)

    # Exercise
    result = day2.part_2_answer(data_path, 19690720)

    # Verify
    assert result == expected

    # Cleanup - none necessary


