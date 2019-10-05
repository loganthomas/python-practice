from pathlib import Path


def test_exists_for_all_files():
    """
    Ensure all code_wars .py files have an accompanying test file
    """
    # Setup
    code_wars_files = [f.name for f in Path('..').glob('*.py') if not str.startswith(f.stem, '_')]
    code_wars_files = sorted(code_wars_files)

    # Exercise
    test_files = [f.name for f in Path('.').glob('*.py') if not str.startswith(f.stem, '_')]
    test_files = sorted([f.replace('test_', '') for f in test_files])
    test_files.remove('1_ensure_tests_exist.py')

    # Verify
    assert code_wars_files == test_files

    # Cleanup - none necessary


