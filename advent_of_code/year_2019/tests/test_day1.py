from advent_of_code.year_2019 import day1
from pathlib import Path
import pytest


@pytest.mark.parametrize('data,expected',[(12,2), (14,2), (1969,654), (100756, 33583)])
def test_day1_part1_calc_fuel_provided_examples(data, expected):
    # Setup - none necessary

    # Exercise
    result = day1.calc_fuel(data)

    # Verify
    assert result == expected

    # Cleanup - none necessary


@pytest.mark.parametrize('data,expected',[(12,2), (14,2), (1969,654), (100756, 33583)])
def test_day1_part1_calc_fuel_provided_examples_types(data, expected):
    # Setup - none necessary

    # Exercise
    result = day1.calc_fuel(data)

    # Verify
    assert isinstance(result,int)

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


@pytest.mark.parametrize('data,expected',[(12,2), (14,2), (1969,654), (100756, 33583)])
def test_day1_part2_calc_single_fuel_provided_examples(data, expected):
    # Setup - none necessary

    # Exercise
    result = day1.calc_single_fuel(data)

    # Verify
    assert result == expected

    # Cleanup - none necessary


@pytest.mark.parametrize('data,expected',[(14,2), (1969,966), (100756, 50346)])
def test_day1_part2_calc_recursive_fuel_provided_examples(data, expected):
    # Setup - none necessary

    # Exercise
    result = day1.calc_recursive_fuel(data)

    # Verify
    assert result == expected

    # Cleanup - none necessary


def test_day1_partw_answer():
    # Setup
    expected = 5069241

    # Exercise
    data_path = Path('advent_of_code/year_2019/data/day1_puzzle.txt')
    result = day1.part_2_answer(data_path)

    # Verify
    assert result == expected

    # Cleanup - none necessary


