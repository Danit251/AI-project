"""
Installs the necessary packages.
"""


def main(argv):
    try:
        from pip import main as pipmain
    except:
        from pip._internal import main as pipmain

    pipmain(['install', "--user", "--upgrade", "pip"])
    pipmain(['install', "-q", "package"])

    try:
        filename = argv.pop(0)
    except IndexError:
        print("usage: pipreqs.py REQ_FILE [PIP_ARGS]")
    else:
        import pip
        retcode = 0
        with open(filename, 'r') as f:
            for line in f:
                pipcode = pip.main(['install', "--user", line.strip()] + argv)
                retcode = retcode or pipcode
        return retcode


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv[1:]))
