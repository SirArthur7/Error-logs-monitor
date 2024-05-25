import sys
from collections import defaultdict

import time
from collections import defaultdict

class LogMonitor:
    def __init__(self):
        self.logs_by_type = defaultdict(list)
        self.logs_stack = []

    def add_log(self, timestamp, log_type, severity):
        # Update logs_by_type
        self.logs_by_type[log_type].append((timestamp, severity))
        
        # Update logs_stack
        left, right = 0, len(self.logs_stack)
        while left < right:
            mid = (left + right) // 2
            if self.logs_stack[mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid
        self.logs_stack = self.logs_stack[:left]
        self.logs_stack.append((timestamp, severity))

    def get_stats(self, logs):
        count = len(logs)
        if count == 0:
            return (0.0, 0.0, 0.0)
        min_severity = min(log[1] for log in logs)
        max_severity = max(log[1] for log in logs)
        mean_severity = sum(log[1] for log in logs) / count
        return (min_severity, max_severity, mean_severity)

    def compute_log_type_stats(self, log_type):
        return self.get_stats(self.logs_by_type[log_type])

    def compute_before_timestamp_stats(self, timestamp):
        left, right = 0, len(self.logs_stack)
        while left < right:
            mid = (left + right) // 2
            if self.logs_stack[mid][0] < timestamp:
                left = mid + 1
            else:
                right = mid
        logs_before = self.logs_stack[:left]
        return self.get_stats(logs_before)

    def compute_after_timestamp_stats(self, timestamp):
        left, right = 0, len(self.logs_stack)
        while left < right:
            mid = (left + right) // 2
            if self.logs_stack[mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid
        logs_after = self.logs_stack[left:]
        return self.get_stats(logs_after)

    def compute_before_timestamp_log_type_stats(self, log_type, timestamp):
        logs = self.logs_by_type[log_type]
        left, right = 0, len(logs)
        while left < right:
            mid = (left + right) // 2
            if logs[mid][0] < timestamp:
                left = mid + 1
            else:
                right = mid
        logs_before = logs[:left]
        return self.get_stats(logs_before)

    def compute_after_timestamp_log_type_stats(self, log_type, timestamp):
        logs = self.logs_by_type[log_type]
        left, right = 0, len(logs)
        while left < right:
            mid = (left + right) // 2
            if logs[mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid
        logs_after = logs[left:]
        return self.get_stats(logs_after)


def main():
    log_monitor = LogMonitor()
    
    input = sys.stdin.read
    data = input().splitlines()
    
    with open('./output.txt', 'w') as output_file:
        for line in data:
            parts = line.split()
            command_type = parts[0]
            
            if command_type == "1":
                _, log_entry = parts
                timestamp, log_type, severity = log_entry.split(';')
                log_monitor.add_log(int(timestamp), log_type, float(severity))
                output_file.write("No output\n")
                # print("No output")
            
            elif command_type == "2":
                _, log_type = parts
                min_severity, max_severity, mean_severity = log_monitor.compute_log_type_stats(log_type)
                output_file.write(f"Min: {round(min_severity, 6)}, Max: {round(max_severity, 6)}, Mean: {round(mean_severity, 6)}\n")
                # print(f"Min: {round(min_severity, 6)}, Max: {round(max_severity, 6)}, Mean: {round(mean_severity, 6)}")

            elif command_type == "3":
                if parts[1] == "BEFORE":
                    timestamp = parts[2]
                    min_severity, max_severity, mean_severity = log_monitor.compute_before_timestamp_stats(int(timestamp))
                    output_file.write(f"Min: {round(min_severity, 6)}, Max: {round(max_severity, 6)}, Mean: {round(mean_severity, 6)}\n")
                    # print(f"Min: {round(min_severity, 6)}, Max: {round(max_severity, 6)}, Mean: {round(mean_severity, 6)}")
                
                elif parts[1] == "AFTER":
                    timestamp = parts[2]
                    min_severity, max_severity, mean_severity = log_monitor.compute_after_timestamp_stats(int(timestamp))
                    output_file.write(f"Min: {round(min_severity, 6)}, Max: {round(max_severity, 6)}, Mean: {round(mean_severity, 6)}\n")
                    # print(f"Min: {round(min_severity, 6)}, Max: {round(max_severity, 6)}, Mean: {round(mean_severity, 6)}") 
            
            elif command_type == "4":
                if parts[1] == "BEFORE":
                    log_type = parts[2]
                    timestamp = int(parts[3])
                    min_severity, max_severity, mean_severity = log_monitor.compute_before_timestamp_log_type_stats(log_type, timestamp)
                    output_file.write(f"Min: {round(min_severity, 6)}, Max: {round(max_severity, 6)}, Mean: {round(mean_severity, 6)}\n")
                    # print(f"Min: {round(min_severity, 6)}, Max: {round(max_severity, 6)}, Mean: {round(mean_severity, 6)}") 

                elif parts[1] == "AFTER":
                    log_type = parts[2]
                    timestamp = int(parts[3])
                    min_severity, max_severity, mean_severity = log_monitor.compute_after_timestamp_log_type_stats(log_type, timestamp)
                    output_file.write(f"Min: {round(min_severity, 6)}, Max: {round(max_severity, 6)}, Mean: {round(mean_severity, 6)}\n")
                    # print(f"Min: {round(min_severity, 6)}, Max: {round(max_severity, 6)}, Mean: {round(mean_severity, 6)}") 
    
    output_file.close()

    with open('./output.txt', 'r') as f:
        file_contents = f.read()
        print(file_contents)
    f.close()
    
    print("Successfully wrote output to output.txt")
        
if __name__ == "__main__":
    main()
