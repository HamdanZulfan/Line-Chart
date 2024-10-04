from bokeh.plotting import figure, show
from bokeh.io import output_file
import re
from datetime import datetime

file_path = 'soal_chart_bokeh.txt'

timestamps = []
bitrates = []

with open(file_path, 'r') as file:
    current_timestamp = None
    for line in file:
        
        timestamp_match = re.search(r'Timestamp: (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})', line)
        if timestamp_match:
            current_timestamp = datetime.strptime(timestamp_match.group(1), '%Y-%m-%d %H:%M:%S')
        
        bitrate_match = re.search(r'\[  5\] .*? (\d+\.\d+) Mbits/sec', line)
        if bitrate_match and current_timestamp:
            timestamps.append(current_timestamp)
            bitrates.append(float(bitrate_match.group(1)))

output_file("line_chart_speed.html")


p = figure(title="Line Chart of Bandwidth Speed", x_axis_label='Timestamp', y_axis_label='Speed (Mbits/sec)',
           x_axis_type='datetime', width=800, height=400) 

p.line(timestamps, bitrates, line_width=2)

show(p)
