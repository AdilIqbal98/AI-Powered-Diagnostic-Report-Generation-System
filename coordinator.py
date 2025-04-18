# coordinator.py
# Final Orchestrator with Guaranteed Succesfull Input

from data_interpretation_agent import DataInterpretationAgent
from validation_agent import ValidationAgent
from report_finalization_agent import ReportFinalizationAgent
from context import KnowledgeBase
import random
import time

def log(tag, text):
    print(f"[{tag}] {text}")

def main():
    context = KnowledgeBase()
    dia = DataInterpretationAgent()
    va = ValidationAgent()
    rfa = ReportFinalizationAgent()

    # One guaranteed valid input
    valid_input = "Patient has persistent cough and fever."
    distractors = [
        "No symptoms mentioned clearly.",
        "Reports only mild discomfort.",
        "Unusual back pain with fatigue.",
        "Patient has headache and dizziness.",
        "Minor skin irritation noted.",
        "Short-term memory loss observed.",
        "Random sleep cycle changes.",
        "Mild eye strain and blurred vision.",
        "Reports sore muscles after workout."
    ]

    all_inputs = random.sample(distractors, 9) + [valid_input]
    random.shuffle(all_inputs)

    context.log_confidence(round(random.uniform(4.0, 6.0), 2))

    max_attempts = 10
    validated = False
    last_feedback = None

    for attempt in range(1, max_attempts + 1):
        raw_input = all_inputs[attempt - 1]
        context.update("patient_raw", raw_input)
        log("INPUT", f"Attempt #{attempt} input: \"{raw_input}\"")

        output = dia.process(raw_input, feedback=last_feedback, context=context)
        log("DIA", f"Diagnosis: {output['diagnosis']}, Confidence: {output['confidence']:.2f}")

        valid, feedback = va.validate(output, context)

        if valid:
            log("VA", "Validation Passed ✅")
            report = rfa.finalize(output, context)
            log("RFA", report)
            log("TRACE", f"Execution completed in {attempt} attempt(s).")
            validated = True
            break
        else:
            log("VA", f"Validation Failed ❌ | Feedback: {feedback}")
            last_feedback = feedback
            time.sleep(0.5)

    if not validated:
        log("SYSTEM", "❌ Max retries (10) exceeded. Escalating to human clinician.")
        print("\nFEEDBACK HISTORY:")
        for i, fb in enumerate(context.get_feedback_trace(), 1):
            print(f"Attempt {i}: {fb}")
        print("\nCONFIDENCE HISTORY:")
        for i, c in enumerate(context.get_confidence_trace(), 1):
            print(f"Attempt {i}: {c:.2f}")

if __name__ == "__main__":
    main()
