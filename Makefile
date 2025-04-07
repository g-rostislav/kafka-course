build-consumer:
	docker build -t kafka_course_consumer:local -f ./consumer/Dockerfile .
build-producer:
	docker build -t kafka_course_producer:local -f ./producer/Dockerfile .
run-cluster:
	docker-compose up -d zookeeper kafka1 kafka2 kafka3 kafka-ui
stop-cluster:
	docker-compose down zookeeper kafka1 kafka2 kafka3 kafka-ui
create-topic:
	docker exec -it kafka1 kafka-topics.sh --create --topic my_topic --bootstrap-server localhost:9092 --partitions 3 --replication-factor 2
describe-topic:
	docker exec -it kafka1 kafka-topics.sh --describe --bootstrap-server localhost:9092
run-producer:
	docker-compose up -d --force-recreate producer-dummy
run-consumer-single:
	docker-compose up -d --force-recreate consumer-single
run-consumer-batch:
	docker-compose up -d --force-recreate consumer-batch