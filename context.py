# context.py
# Shared Memory with Feedback + Confidence Logs

class KnowledgeBase:
    def __init__(self):
        self.data = {}
        self.feedback_history = []
        self.confidence_history = []

    def update(self, key, value):
        self.data[key] = value

    def get(self, key, default=None):
        return self.data.get(key, default)

    def all(self):
        return self.data

    def log_feedback(self, feedback):
        if feedback:
            self.feedback_history.append(feedback)

    def log_confidence(self, value):
        self.confidence_history.append(value)

    def get_feedback_trace(self):
        return self.feedback_history

    def get_confidence_trace(self):
        return self.confidence_history

    def last_feedback_reason(self):
        return self.feedback_history[-1] if self.feedback_history else None

    def last_confidence(self):
        return self.confidence_history[-1] if self.confidence_history else 0.0
