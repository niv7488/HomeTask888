docker pull apache/kafka:3.7.0
docker run --rm apache/kafka:3.7.0 kafka-topics.sh --create --zookeeper localhost:2181 --topic 888wh --partitions 10
docker run --rm apache/kafka:3.7.0 kafka-topics.sh --describe --zookeeper localhost:2181 --topic 888wh

#create 888wh topic using the console producer script
docker run --rm -it apache/kafka:3.7.0 kafka-console-producer.sh --broker-list localhost:9092 --topic 888wh

#present the messege using the console consumer script 
docker run --rm -it apache/kafka:3.7.0 kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic 888wh --from-beginning

