import config

from http_checker import check_http_log
from rotate_checker import check_rotate_log


def main():
    check_rotate_log()
    check_http_log()


if __name__ == '__main__':
    main()
