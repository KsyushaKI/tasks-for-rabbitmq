#!/usr/bin/env python
from tasks_for_rabbitmq.generate import file_generation
import sys
import os


def main():
    try:
        file_generation()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)


if __name__ == '__main__':
    main()
