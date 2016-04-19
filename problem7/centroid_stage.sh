hadoop jar /root/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar -input /data/twitter -output location_s1_out -file *.py -mapper LocationStage1Map.py -reducer LocationStage1Reduce.py
