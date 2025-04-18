# data_interpretation_agent.py
# Smart DIA with Ontology Alignment

import random

class DataInterpretationAgent:
    def __init__(self):
        self.revision_memory = []

    def process(self, raw_data, feedback=None, context=None):
        confidence = context.last_confidence()
        diagnosis = "Unknown Condition"
        tags = []

        # Assign tags and choose from ontology-aligned diagnoses
        if "cough" in raw_data.lower():
            diagnosis = random.choice(["Pneumonia", "Asthma"])
            tags.append("respiratory")

        if "fever" in raw_data.lower():
            if diagnosis == "Unknown Condition":
                diagnosis = "Infection"
            tags.append("systemic")

        if "wheezing" in raw_data.lower():
            diagnosis = "Asthma"
            tags.append("airway")

        if "tight chest" in raw_data.lower():
            tags.append("respiratory")

        # Fallback: if tags exist but diagnosis was missed
        if diagnosis == "Unknown Condition" and tags:
            diagnosis = random.choice(["Pneumonia", "Infection", "Asthma"])

        # Confidence boost logic
        if feedback:
            diagnosis += " (Adjusted)"
            confidence += random.uniform(0.5, 1.0)
        else:
            confidence += random.uniform(0.2, 0.5)

        confidence = min(round(confidence, 2), 10.0)
        context.log_confidence(confidence)

        interpretation = {
            "diagnosis": diagnosis,
            "confidence": confidence,
            "tags": tags
        }

        if feedback:
            self.revision_memory.append(feedback)
            context.log_feedback(feedback)

        return interpretation
