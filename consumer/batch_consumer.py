from confluent_kafka import Consumer


class BatchMessageConsumer:
    def __init__(
        self,
        topic: str,
        group_id: str,
        bootstrap_servers: list[str],
    ):

        self.conf = {
            "group.id": group_id,
            "enable.auto.commit": False,
            "auto.offset.reset": "earliest",  # will be ignored for existing group.id
            "bootstrap.servers": bootstrap_servers,
            # "debug": "consumer,cgrp,topic"
        }
        print(f"Configuring consumer: {self.conf} ...")

        self.consumer = Consumer(self.conf)
        self.consumer.subscribe([topic])

    def run(self, num_messages: int = 10, poll_interval: int = 1):
        try:
            while True:
                print("Polling brokers ...")
                messages = self.consumer.consume(num_messages, poll_interval)
                valid_messages = [msg for msg in messages if msg and not msg.error()]
                if valid_messages:
                    print(f"Got {len(valid_messages)}/{len(messages)} valid messages")
                    for msg in messages:
                        if msg is None:
                            print("Msg is None")
                        elif msg.error():
                            print(f"ERROR: {msg.error()}")
                        else:
                            print(
                                f"(partition, offset)=('{msg.partition()}', {msg.offset()} => key='{msg.key()}', value={msg.value()}"
                            )
                    self.consumer.commit(asynchronous=False)

        except KeyboardInterrupt:
            print("Stopped")
        finally:
            print("Closing consumer ...")
            self.consumer.close()
            print("Consumer closed cleanly")