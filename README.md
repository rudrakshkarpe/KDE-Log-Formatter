# KDE_SUS Log Formatter

KDE_SUS Log Formatter is a tool for automating the process of determining the elapsed time for Standard Usage Scenarios (SUS) logs generated by the KDE Eco Tester. The tool takes a log file in the CSV format as input and outputs the formatted log file with the elapsed time for each action.

## Installation

To install the KDE_SUS Log Formatter, clone the repository and install the required dependencies using pip:

- Clone the repository:
  
``` git clone https://invent.kde.org/rudrakshkarpe/sus-log-formatter.git ```


## Dependencies

- Python 3.6 or higher
- Install the required dependencies using pip:

``` pip install pandas ```


## Usage

- To use the tool, run the `log_formatter.py` script with the path to the log file as input:

``` 
python sus_log_formatter.py input_file_path [-o output_file_path]
```

- input_file_path: The path to the input log file in CSV format.
- -o or --output_file_path: (Optional) The path to save the formatted log file. If not provided, the formatted
  log will be displayed in the terminal.

### Example:

```
python sus_log_formatter.py /path/to/input/logfile.csv -o /path/to/output/formatted_logfile.csv
```

To format the log file located at /path/to/input/logfile.csv and display the formatted log in the terminal, run:

```
python sus_log_formatter.py /path/to/input/logfile.csv
```