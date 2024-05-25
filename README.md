# Error Log Monitor

## Overview

`LogMonitor` is a Python class designed to monitor and analyze logs. It supports adding logs with timestamps, log types, and severity levels, and computing statistical summaries such as minimum, maximum, and mean severity for different conditions.

## Features

- Add logs with a specific timestamp, log type, and severity.
- Compute statistics (min, max, mean) for logs:
  - By log type.
  - Before a specific timestamp.
  - After a specific timestamp.
  - By log type before a specific timestamp.
  - By log type after a specific timestamp.

## Code Description

### LogMonitor Class

The `LogMonitor` class includes the following methods:

- `__init__`: Initializes various dictionaries to store logs and their statistics.
- `add_log`: Adds a new log entry and updates the corresponding statistics.
- `get_stats`: Computes statistics from the stored log data.
- `compute_log_type_stats`: Returns statistics for logs of a specific type.
- `compute_before_timestamp_stats`: Returns statistics for logs before a specific timestamp.
- `compute_after_timestamp_stats`: Returns statistics for logs after a specific timestamp.
- `compute_before_timestamp_log_type_stats`: Returns statistics for logs of a specific type before a specific timestamp.
- `compute_after_timestamp_log_type_stats`: Returns statistics for logs of a specific type after a specific timestamp.

### Main Function

The `main` function reads input from `stdin`, processes it, and writes the results to an output file (`output.txt`). It handles different commands to add logs or compute statistics based on the input.

## Functionality

### Input Format

The input consists of lines of commands. Each command can be one of the following types:

1. `1 timestamp;log_type;severity`: Add a new log entry.
2. `2 log_type`: Compute and output statistics for logs of the given log type.
3. `3 BEFORE timestamp`: Compute and output statistics for logs before the given timestamp.
4. `3 AFTER timestamp`: Compute and output statistics for logs after the given timestamp.
5. `4 BEFORE log_type timestamp`: Compute and output statistics for logs of the given log type before the given timestamp.
6. `4 AFTER log_type timestamp`: Compute and output statistics for logs of the given log type after the given timestamp.


### File I/O

The script reads input from `input.txt` or any of the 5 test input files in the folder `inputs` (this can be provided as a command line argument) and writes output to `output.txt`. The input format follows specific commands, and the output format includes statistics computed based on the commands.

### Prerequisities


In order to run this container you'll need docker installed.

* [Windows](https://docs.docker.com/windows/started)
* [OS X](https://docs.docker.com/mac/started/)
* [Linux](https://docs.docker.com/linux/started/)


## Usage

1. Ensure Python 3.x and Docker are installed on your system.
2. Build Docker image using the Dockerfile:
  ```shell
  docker build -t your_name/log_monitor .
  ```
3. Run the script using :
  ```shell
  docker run -i your_name/log_monitor < ./input.txt
  ```
4. Output will be written to `output.txt` and its contents will be printed on the Docker container logs.

## Example Input Format

The script expects input commands in the following format:
```
1 timestamp;log_type;severity
2 log_type
3 BEFORE timestamp
3 AFTER timestamp
4 BEFORE log_type timestamp
4 AFTER log_type timestamp
```

## Dependencies

This script requires the collections module, which is included in Python's standard library.

## Authors

* **Anannyo Dey** - [LinkedIn](https://www.linkedin.com/in/anannyo-dey-201b97200/)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.
