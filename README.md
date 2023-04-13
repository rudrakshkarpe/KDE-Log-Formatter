### Parquet format for log files :)


- To format a CSV log file and save the output as CSV:

```
python format_log_file.py input.csv -o output.csv
```

- To format a CSV log file and display the output in the terminal:

```
python format_log_file.py input.csv
```
- To format a CSV log file and save the output as Parquet:
  
```
python format_log_file.py input.csv -o output.parquet -f parquet
```

- To format a Parquet log file and save the output as CSV:

```
python format_log_file.py input.parquet -o output.csv
```

- To format a Parquet log file and display the output in the terminal:

```
python format_log_file.py input.parquet
```

- To format a Parquet log file and save the output as Parquet:

```
python format_log_file.py input.parquet -o output.parquet -f parquet
```