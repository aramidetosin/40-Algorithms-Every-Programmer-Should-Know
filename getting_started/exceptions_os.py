import os
import sys


def make_at(path, dir_name):
    original_path = os.getcwd()
    os.chdir(path)
    try:
        os.mkdir(dir_name)
    except FileExistsError as e:
        print(f"Exception: {e!r}", file=sys.stderr)
        raise
    finally:
        os.chdir(original_path)
        print(os.getcwd())


make_at("/home/aramideo/Documents/", "test")
