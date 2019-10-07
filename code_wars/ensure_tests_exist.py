from pathlib import Path


def collect_code_wars_files():
    cw_dir = Path(__file__).parent  # this files parent dir (code_wars)
    code_wars_files = [f.name for f in cw_dir.glob('*.py') if not str.startswith(f.stem, '_')]
    code_wars_files = sorted(code_wars_files)
    return code_wars_files

