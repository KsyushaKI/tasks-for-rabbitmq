#!/usr/bin/env python
import sys
import os
from tasks_for_rabbitmq.receive import rmq_receiver_messages


def main():
    try:
        rmq_receiver_messages()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
    


if __name__ == '__main__':
    main()
