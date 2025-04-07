import time
from confluent_kafka import Producer, Message



class DummyProducer:
    def __init__(self, topic: str, bootstrap_servers: str, acks: str):
        self.topic = topic
        self.conf = {
            "bootstrap.servers": bootstrap_servers,
            "acks": acks
        }
        print(f"Configuring producer: {self.conf} ...")
        self.producer = Producer(self.conf)

    @staticmethod
    def acked(err: str, msg: Message) -> None:
        if err:
            log = f"ERROR: {err} for msg='{msg.value()}'"
        else:
            log = "Saved {msg} into (topic,partition)=({topic},{partition}) with offset: {offset}".format(
                msg=msg.value(),
                offset=msg.offset(),
                topic=msg.topic(),
                partition=msg.partition(),
            )
        print(log)

    def run(self):
        try:
            cnt = 0
            while True:
                msg = {
                    "topic": self.topic,
                    # "key": "key-1",
                    "value": str(cnt),
                    "callback": self.acked,
                }
                self.producer.produce(**msg)
                self.producer.poll(1)
                cnt += 1
                time.sleep(0.3)

        except KeyboardInterrupt:
            print("Stopped")
        finally:
            print("Flushing producer ...")
            self.producer.flush()
            print("Done")