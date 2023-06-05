#!/usr/bin/env python
import sys
import os
from tasks_for_rabbitmq.send import publisher


def main():
    try:
        publisher()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)


if __name__ == '__main__':
    main()
