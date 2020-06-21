'''
sudo su
wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py
pip install confluent_kafka
'''

from confluent_kafka.admin import AdminClient, NewTopic, NewPartitions, ConfigResource, ConfigSource
from confluent_kafka import KafkaException
import json

broker = "kafka101-blackhole.careem-engineering.com:9092"
admin = AdminClient({'bootstrap.servers': broker})

partitions_for_reassignment = []
_test_partitions_for_reassignment = []


batch_size = 10
start_index = 0
out_dir = "/home/ec2-user/partition_reassignment"


# {KEY: [FIRST_CHOICE_FOR_REPLACEMENT, SECOND_CHOICE_FOR_REPLACEMENT]}

brokers_map = {104: [102, 103], 105: [102, 103], 204: [201, 202], 205: [202, 201], 304: [301, 303], 305: [303, 301]}

cluster_metadata = admin.list_topics(timeout=10)
for topic in iter(cluster_metadata.topics.values()):
    for partition in iter(topic.partitions.values()):
        replicas = partition.replicas
        new_replicas = []
        need_rebalance = False
        for replica in replicas:
            if replica in brokers_map:
                need_rebalance = True
                first_choice, second_choice = brokers_map[replica]
                if first_choice in replicas and second_choice in replicas:
                    raise Exception("No valid substitute for topic {}, partition: {}, current replicas: {}".format(topic, partition.id, partition.replicas))
                elif first_choice in replicas:
                    new_replicas.append(second_choice)
                else:
                    new_replicas.append(first_choice)
            else:
                new_replicas.append(replica)
        log_dirs = ["any" for i in range(0, len(new_replicas))]
        if need_rebalance:
            _test_partitions_for_reassignment.append({"topic": str(topic), "partition": partition.id, "old_replicas": replicas, "replicas": new_replicas, "log_dirs": log_dirs})
            partitions_for_reassignment.append({"topic": str(topic), "partition": partition.id, "replicas": new_replicas, "log_dirs": log_dirs})



import os
if not os.path.exists(out_dir):
    os.makedirs(out_dir)


num_partitions_to_reassign = len(partitions_for_reassignment)
while(start_index < num_partitions_to_reassign):
    end_index = num_partitions_to_reassign if start_index+batch_size >= num_partitions_to_reassign else start_index+batch_size
    partitions_to_reassign = partitions_for_reassignment[start_index:end_index]
    json_str = json.dumps({'version': 1, 'partitions': partitions_to_reassign}, indent=4)
    with open('{}/partition_reassignment_{}_{}'.format(out_dir, start_index, end_index), 'w') as out_file:
        out_file.write(json_str)
    start_index = end_index



# Reassignment Files 
'''
/home/ec2-user/partition_reassignment/partition_reassignment_10_20
/home/ec2-user/partition_reassignment/partition_reassignment_20_30
/home/ec2-user/partition_reassignment/partition_reassignment_30_40
/home/ec2-user/partition_reassignment/partition_reassignment_40_50
/home/ec2-user/partition_reassignment/partition_reassignment_50_60
/home/ec2-user/partition_reassignment/partition_reassignment_60_70
/home/ec2-user/partition_reassignment/partition_reassignment_70_80
/home/ec2-user/partition_reassignment/partition_reassignment_80_90
/home/ec2-user/partition_reassignment/partition_reassignment_90_91
'''

# Running the reassignment
'''
/opt/confluent/bin/kafka-reassign-partitions \
    --zookeeper zookeeper100-blackhole.careem-engineering.com:2181 \
    --reassignment-json-file /home/ec2-user/partition_reassignment/partition_reassignment_90_91 \
    --execute
'''

# Verifying the reassignment
'''
/opt/confluent/bin/kafka-reassign-partitions \
    --zookeeper zookeeper100-blackhole.careem-engineering.com:2181 \
    --reassignment-json-file /home/ec2-user/partition_reassignment/partition_reassignment_90_91 \
    --verify | grep -i 'in progress'
'''
