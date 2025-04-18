# message_bus.py

from queue import Queue
import uuid
import datetime

class Message:
    def __init__(self, patient_id, task, payload, status="pending", feedback=None, retries=0, history=None):
        self.message_id = str(uuid.uuid4())
        self.timestamp = datetime.datetime.now().isoformat()
        self.patient_id = patient_id
        self.task = task
        self.payload = payload
        self.status = status
        self.feedback = feedback
        self.retries = retries
        self.history = history or []

    def to_dict(self):
        return {
            "message_id": self.message_id,
            "timestamp": self.timestamp,
            "patient_id": self.patient_id,
            "task": self.task,
            "status": self.status,
            "payload": self.payload,
            "feedback": self.feedback,
            "retries": self.retries,
            "history": self.history
        }

class MessageBus:
    def __init__(self):
        self.queue = Queue()

    def send(self, message):
        self.queue.put(message)

    def receive(self):
        if not self.queue.empty():
            return self.queue.get()
        return None
