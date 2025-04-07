from confluent_kafka import Consumer

class SingleMessageConsumer:
    def __init__(
        self,
        topic: str,
        group_id: str,
        bootstrap_servers: list[str],
    ):

        self.conf = {
            "group.id": group_id,             # Group id to parallelize workloads in the same group
            "enable.auto.commit": False,      # Handle commits manually
            "auto.offset.reset": "earliest",  # will be ignored for existing group.id
            "bootstrap.servers": bootstrap_servers,
            # "debug": "consumer,cgrp,topic"
        }
        print(f"Configuring consumer: {self.conf} ...")

        self.consumer = Consumer(self.conf)
        self.consumer.subscribe([topic])

    def run(self, poll_interval: int = 1):
        try:
            while True:
                msg = self.consumer.poll(poll_interval)
                if msg is None:
                    print("Waiting new messages ...")
                elif msg.error():
                    print(f"ERROR: {msg.error()}")
                else:
                    print(
                        f"Msg from '{msg.topic()}': partition='{msg.partition()}' key='{msg.key()}', value={msg.value()}"
                    )
                    self.consumer.commit(msg, asynchronous=False)

        except KeyboardInterrupt:
            print("Stopped")
        finally:
            print("Closing consumer ...")
            self.consumer.close()
            print("Consumer closed cleanly")