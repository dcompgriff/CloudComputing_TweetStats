hadoop jar /root/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar -input /data/twitter -output average_out -file *.py -mapper AverageMap.py -reducer AverageReduce.py
