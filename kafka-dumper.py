import praw
import configparser
import importlib

confparser = configparser.ConfigParser()
confparser.read('configuration.cfg')

client_id = confparser['praw']['client_id']
client_secret = confparser['praw']['client_secret']
user_agent = confparser['praw']['user_agent']
username = confparser['praw']['username']
password = confparser['praw']['password']

dumper_module = confparser['dumper']['module']
dumper_class  = confparser['dumper']['class']

module = importlib.import_module(dumper_module)
class_= getattr(module,dumper_class)
dumper = class_()

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent=user_agent, username=username, password=password)

subreddit = reddit.subreddit(confparser['praw']['subreddit'])

import avro.io
from confluent_kafka.avro import AvroProducer

# Relativ path to key and value avro schema
value_schema_path = confparser["avro"]["key_schema"]
key_schema_path = confparser["avro"]["value_schema"]

# Kafka topic to serialize
topic = confparser['kafka']['topic']

# Avro schema to serialize value in kafka
value_schema = avro.schema.Parse(open(value_schema_path).read())

# Avro schema to serialize key in kafka
key_schema = avro.schema.Parse(open(key_schema_path).read())

# Avro producer to serialize key value pair
# default key and value schema is provided
producer = AvroProducer({'bootstrap.servers': 'localhost:9092', 'schema.registry.url': 'http://localhost:8081'}, key_schema,
                        value_schema)

for submission in subreddit.stream.submissions():
    sub_name = submission.subreddit_name_prefixed
    sub_name = submission.subreddit_name_prefixed.split(sub_name[0]+"/")[1].lower()
    created_on = int(sukeybmission.created_utc)
    id = submission.id
    value = {"subreddit": sub_name, "created_on": created_on,
             "submission_id": id}
    key = {"id": sub_name + id}
    #if key and value schema is not provided then default one provided in contructor is used
    producer.produce(topic='test', key=key, key_schema=key_schema, value=value, value_schema=value_schema)
    producer.flush(30)
    print(sub_name + id)