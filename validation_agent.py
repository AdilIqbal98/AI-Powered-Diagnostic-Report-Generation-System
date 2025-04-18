# validation_agent.py
# Reliable VA with Ontology + Tag Checks

class ValidationAgent:
    def __init__(self):
        self.ontology = {"Pneumonia", "Infection", "Asthma"}
        self.threshold = 8.0

    def validate(self, data, context=None):
        diagnosis = data["diagnosis"].replace(" (Adjusted)", "")
        confidence = data["confidence"]
        feedback = []

        if diagnosis not in self.ontology:
            feedback.append(f"'{diagnosis}' not in clinical ontology.")

        if confidence < self.threshold:
            feedback.append(f"Confidence too low: {confidence:.2f} < {self.threshold:.2f}")

        if not any(tag in data["tags"] for tag in ["respiratory", "systemic", "airway"]):
            feedback.append("No essential symptom tags found.")

        if feedback:
            context.log_feedback(feedback)
            return False, feedback

        return True, None
