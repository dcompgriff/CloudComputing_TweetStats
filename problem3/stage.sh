hadoop jar /root/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar -input /user/griffid6/top_5_s2_out -output p3_out -file *.py -mapper SantaOnoMap.py -reducer SantaOnoReduce.py
