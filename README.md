<div align="center">

<h1>Tasks for RabbitMQ</h1>

<p>CLI app that demonstrates an example of working with RabbitMQ</p>

[![Maintainability](https://api.codeclimate.com/v1/badges/0722f14501e6bcb34598/maintainability)](https://codeclimate.com/github/KsyushaKI/tasks-for-rabbitmq/maintainability)

</div>

## About

CLI app that demonstrates an example of working with RabbitMQ. Tasks for RabbitMQ include the following programs:

* [X] **_file_generation.py_**: every 5 seconds generates a file with an arbitrary name in the folder "data", the content of the file is equal to the file name (for example "1052.txt"). The program runs within 2 minutes;
* [X] **_publisher.py_**: every 15 seconds will send the current list of files in the "data" folder in json format to RabbitMq;
* [X] **_consumer.py_**: reads messages from RabbitMq. Messages are read as soon as the "publisher" sends them to RabbitMq. The received message is processed for 35 seconds (imitation of file processing), namely: the contents of the files are combined and a text file is created in the "result" folder. The filename is equal to the RabbitMq message ID. The original files are deleted.

#### Example:

```bash
>> consumer

 [*] Waiting for messages. To exit press CTRL+C
 [x] Received b'{"files": ["1052.txt", "6717.txt", "3336.txt", "3962.txt", "3248.txt", "4292.txt"], "message_id": 1}'
 [x] Done
 [x] Received b'{"files": ["9341.txt", "8918.txt", "7139.txt"], "message_id": 4}'
 [x] Done
 [x] Received b'{"files": ["1297.txt", "1425.txt", "5703.txt"], "message_id": 7}'
 [x] Done
 [x] Received b'{"files": [], "message_id": 10}'
 [x] Done
^CInterrupted

### Built With

* [Python](https://www.python.org/)
* [RabbitMQ](https://www.rabbitmq.com/)
* [Pika](https://pika.readthedocs.io/en/stable/)
* [interruptingcow](https://pypi.org/project/interruptingcow/)
* [Poetry](https://python-poetry.org/)
* [Flake8](https://flake8.pycqa.org/en/latest/)

---

## Installation

### Prerequisites

#### Python

Before installing the package make sure you have Python version 3.8 or higher installed:

```bash
>> python --version
Python 3.8.0+
```

#### Poetry

The project uses the Poetry dependency manager. To install Poetry use its [official instruction](https://python-poetry.org/docs/#installation).

#### RabbitMQ

The project uses the RabbitMQ message broker. To install RabbitMQ use its [official instruction](https://www.rabbitmq.com/download.html).

### Package

To use the package, you need to clone the repository to your computer. This is done using the ```git clone``` command. Clone the project:

```bash
>> git clone https://github.com/KsyushaKI/tasks-for-rabbitmq
```

Then you have to build the package and install it:

```bash
>> cd tasks-for-rabbitmq
```

```bash
>> make install
>> make build
>> make package-install
```
---

## Usage

To start working with the installed program do the following:

1. To start RabbitMQ server:
```bash
>> brew services start rabbitmq
```
2. Open three terminal windows and in each of them run the command: 
```bash
>> consumer
```
3. In a new terminal window, run the command:
```bash
>> file_generation
```
4. In a new terminal window, run the command:
```bash
>> publisher
```
5. To stop running programs use the fillowing in each open window:
```bash
>> CTRL+C
```
6. To stop RabbitMQ server:
```bash
>> brew services stop rabbitmq
```

---

## Additionally

### Dependencies

* python = "^3.11"
* pika = "^1.3.2"
* interruptingcow = "^0.8"
* rabbitmq = "^0.2.0"

### Dev Dependencies

* flake8 = "^6.0.0"

---

> GitHub [@KsyushaKI](https://github.com/KsyushaKI) &nbsp;&middot;&nbsp;
> LinkedIn [@Oksana Karshakevich](https://www.linkedin.com/in/oksana-karshakevich/)
