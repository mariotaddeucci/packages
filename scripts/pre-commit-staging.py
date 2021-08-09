import os
import shutil
from sys import argv

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TMP_DIRNAME = "tmp_pre_commit"
TMP_URI = os.path.join(BASE_DIR, TMP_DIRNAME)


def recursive_overwrite(src, dest, ignore=None):
    if os.path.isdir(src):
        if not os.path.isdir(dest):
            os.makedirs(dest)
        files = os.listdir(src)
        if ignore is not None:
            ignored = ignore(src, files)
        else:
            ignored = set()
        for f in files:
            if f not in ignored:
                recursive_overwrite(os.path.join(src, f), os.path.join(dest, f), ignore)
    else:
        shutil.copyfile(src, dest)


if len(argv) > 1:
    for file in argv[1:]:
        final_dir = os.path.join(TMP_URI, os.path.dirname(file))
        os.makedirs(final_dir, exist_ok=True)
        shutil.copy(os.path.join(BASE_DIR, file), final_dir)

elif len(argv) == 1:
    recursive_overwrite(TMP_URI, BASE_DIR)
    shutil.rmtree(TMP_URI)
