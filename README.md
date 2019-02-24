# Reddit Kafka
* This repository consists of programs to stream reddit comments or submissions data into  a Apache Kafka cluster.

* It captures comments or submissions using praw (python reddit api wraper).
* Confluent schema-registry is used to provide avro schemas to all the nodes in the cluster.

## Configuration File

* The configuration file provides a way to control the data being collected.

### 1. Praw Section
+ client_id
    
        Provide client_id of reddit app
+ client_secret
        
        Provide client_secret of reddit app
+ user_agent
        
        Provide user_agent name
+ username
        
        Username of reddit account to use
+ password
        
        password of reddit account to use
+ subreddit
        
        reddit style multi-subreddit names. eg: india+showerthoughts

### 2. Kafka Section
+ topic
    
        Name of kafka topic to dump into

### 3. Avro
+ key_schema
        
        Schema location of key.    
+ value_schema
        
        Schema location of value.

### 4. Dumper Section
+ module
    
        Module name to get the class  to dump the data into kafka.
+ class
    
        Name of the class to use to dump the schema.