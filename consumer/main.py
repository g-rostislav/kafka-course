import os
import sys
import argparse
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from batch_consumer import BatchMessageConsumer
from single_consumer import SingleMessageConsumer


dispatch_consumer = {
    "batch": BatchMessageConsumer,
    "single": SingleMessageConsumer
}


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["batch", "single"], default=os.getenv("MODE"))
    parser.add_argument("--topic", type=str, default=os.getenv("TOPIC"))
    parser.add_argument("--group_id", type=str, default=os.getenv("GROUP_ID"))
    parser.add_argument("--bootstrap_servers", type=str, default=os.getenv("KAFKA_BOOTSTRAP_SERVERS"))
    args = parser.parse_args()

    missing = []
    if not args.mode:
        missing.append("Set 'mode' cli arg or MODE env var")
    if not args.topic:
        missing.append("Set 'topic' cli arg or TOPIC env var")
    if not args.group_id:
        missing.append("Set 'group_id' cli arg or GROUP_ID env var")
    if not args.bootstrap_servers:
        missing.append("Set 'bootstrap_servers' cli arg or KAFKA_BOOTSTRAP_SERVERS env var")
    if missing:
        print(*missing, sep='\n')
        sys.exit(1)
    return args


if __name__ == "__main__":
    args = parse_args()

    consumer = dispatch_consumer[args.mode](
        topic=args.topic,
        group_id=args.group_id,
        bootstrap_servers=args.bootstrap_servers,
    )
    consumer.run()




