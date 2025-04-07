import os
import sys
import argparse
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from producer import DummyProducer


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", type=str, default=os.getenv("TOPIC"))
    parser.add_argument("--acks", choices=[0, 1, -1, "all"], default=os.getenv("ACKS"))
    parser.add_argument("--bootstrap_servers", type=str, default=os.getenv("KAFKA_BOOTSTRAP_SERVERS"))
    args = parser.parse_args()

    missing = []
    if not args.topic:
        missing.append("Set 'topic' cli arg or 'TOPIC' env var")
    if not args.acks:
        missing.append("Set 'acks' cli arg or 'ACKS' env var")
    if not args.bootstrap_servers:
        missing.append("Set 'bootstrap_servers' cli arg or 'KAFKA_BOOTSTRAP_SERVERS' env var")
    if missing:
        print(*missing, sep='\n')
        sys.exit(1)
    return args


if __name__ == "__main__":
    args = parse_args()
    DummyProducer(
        acks=args.acks,
        topic=args.topic,
        bootstrap_servers=args.bootstrap_servers,
    ).run()