import errno
import os
import pathlib
import subprocess
import sys


def collect_files(extensions):
    result = []
    for (directory, _, files) in os.walk("."):
        for f in files:
            path = os.path.join(directory, f)
            if pathlib.Path(path).suffix in extensions:
                result.append(path)

    return result


def format(file):
    format_base = ["clang-format", "-i"]
    command = format_base + [f]
    print("Formatting", f)
    subprocess.run(command)


if __name__ == "__main__":
    extensions = [".c", ".h"]

    try:
        if len(sys.argv) > 1:
            for f in sys.argv[1:]:
                format(f)
        else:
            for f in collect_files(extensions):
                format(f)
    except OSError as e:
        if e.errno == errno.ENOENT:
            print("Error: clang-format is not available!")
