from __future__ import print_function
import sys


class RiteAidRawFile(object):
    GOOD_LINE_LEN = 65
    FIRST_MSG_OFFSET = 272

    def __init__(self, pathname):
        self._load(pathname)

    def _load(self, pathname):
        self.buf = ''
        with open(pathname, 'rb') as f:
            for line in f:
                line = line.strip('\n')
                if len(line) == self.GOOD_LINE_LEN:
                    self.buf += line[-16:]

        self.buf = self.buf[self.FIRST_MSG_OFFSET:]
        print(self.buf)


def main(pathname):
    rawFile = RiteAidRawFile(pathname)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("usage: {app} pathname".format(app=sys.argv[0]))
        sys.exit(2)

    main(sys.argv[1])
