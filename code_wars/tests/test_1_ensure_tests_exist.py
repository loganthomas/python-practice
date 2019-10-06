"""
Ensure that all .py files in code_wars have a test file as well
"""

from pathlib import Path
from code_wars import ensure_tests_exist


def test_exists_for_all_files():
    """
    Ensure all code_wars .py files have an accompanying test file
    """
    # Setup
    code_wars_files = ensure_tests_exist.collect_code_wars_files()

    # Exercise
    test_dir = Path(__file__).parent  # this file's parent dir (tests/)
    test_files = [f.name for f in test_dir.glob('*.py') if not str.startswith(f.stem, '_')]
    test_files = sorted([f.replace('test_', '').replace('1_', '') for f in test_files])

    # Verify
    assert code_wars_files == test_files

    # Cleanup - none necessary

