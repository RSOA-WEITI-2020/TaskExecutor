"""
Celery app that wraps calls to an external Python library 'lcs' into asynchronous tasks.
"""
import os
from celery import Celery
from rosatasks.quantum_sim_tasks import simulate_code


def make_celery():
    user = os.environ["BROKER_USER"]
    password = os.environ["BROKER_PASSWORD"]
    address = os.environ["BROKER_ADDRESS"]
    broker_address = f"amqp://{user}:{password}@{address}"
    return Celery("worker", broker=broker_address, backend=broker_address)


app = make_celery()

if __name__ == "__main__":
    app.worker_main()
