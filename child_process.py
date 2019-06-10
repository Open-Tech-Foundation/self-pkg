import subprocess
import sys
from chalk import red


def spawn(args, shell=False, input=None, err_msg='', verbose=False):
    stdout = None if verbose else subprocess.PIPE
    try:
        subprocess.run(
            args,
            input=input,
            shell=shell,
            check=True,
            stdout=stdout,
            stderr=stdout,
        )
    except BaseException as err:
        print(red(err))
        sys.exit(red(err_msg))
