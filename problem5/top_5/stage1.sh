hadoop jar /root/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar -input /data/twitter -output top_5_s1_out -file *.py -mapper Top5Stage1Map.py -reducer Top5Stage1Reduce.py
