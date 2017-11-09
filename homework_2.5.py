import subprocess

import os


def run_convert(source, img, result):
    subprocess.run(['convert.exe', os.path.join(source, img), '-resize', '200', os.path.join(result, img)])


def main():
    source = 'Source'
    result = 'Result'
    if not os.path.exists(result):
        os.mkdir(result)
    for img in os.listdir(source):
        run_convert(source, img, result)


if __name__ == '__main__':
    main()
