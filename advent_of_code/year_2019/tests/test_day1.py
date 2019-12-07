from advent_of_code.year_2019 import day1
from pathlib import Path
import pytest


@pytest.mark.parametrize('data,expected',[(12,2), (14,2), (1969,654), (100756, 33583)])
def test_day1_calc_fuel_part1_provided_examples(data, expected):
    # Setup - none necessary

    # Exercise
    result = day1.calc_fuel(data)

    # Verify
    assert result == expected

    # Cleanup - none necessary


@pytest.mark.parametrize('data,expected',[(12,2), (14,2), (1969,654), (100756, 33583)])
def test_day1_calc_fuel_part1_provided_examples_types(data, expected):
    # Setup - none necessary

    # Exercise
    result = day1.calc_fuel(data)

    # Verify
    assert type(result) == int

    # Cleanup - none necessary


def test_day1_part1_answer():
    # Setup
    expected = 3381405

    # Exercise
    data_path = Path('advent_of_code/year_2019/data/day1_puzzle.txt')
    result = day1.part_1_answer(data_path)

    # Verify
    assert result == expected

    # Cleanup - none necessary
