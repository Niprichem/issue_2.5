import subprocess

import os


if __name__ == '__main__':
    source = 'Source'
    result = 'Result'
    for img in os.listdir(source):
        subprocess.run(['convert.exe', os.path.join(source, img), '-resize', '200', os.path.join(result, img)])
