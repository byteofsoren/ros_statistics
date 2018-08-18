# ros_statistics
A statistical tool for analyzing ros logs

´´´
ROS - log analyzer and statistic generator
stat.py [file] [keyword] [axis=0]

:file:           is the log file you want to analyze
:keyword:        is a key word you want to search for
:axis:           is in what 'direction' you want to analyse
  Default is 0 and generate statistic for columns
   wile 1 is statistics of the current row
This will analyze the [file] for string containing:
keyword 13, 24, 42
Then reduce the information to:
13, 24, 42
´´´
