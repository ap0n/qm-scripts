#/bin/bash
# Run from ~/datasets
for d in */; do
	hdfs dfs -mkdir -p /user/storm/data/$d
	hdfs dfs -copyFromLocal $d/fixed/* /user/storm/data/$d/
done
