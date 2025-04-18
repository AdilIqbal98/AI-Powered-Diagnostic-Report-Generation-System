# report_finalization_agent.py
# RFA with Clinical Explanation

class ReportFinalizationAgent:
    def finalize(self, data, context):
        diagnosis = data["diagnosis"].replace(" (Adjusted)", "")
        explanation = {
            "Pneumonia": "A respiratory infection causing inflammation in the lungs.",
            "Infection": "Likely systemic immune response.",
            "Asthma": "Inflammatory airway disease often triggered by allergens."
        }

        rationale = explanation.get(diagnosis, "Further investigation needed.")
        suggestions = "CT scan, CBC blood panel recommended."

        return f"""
==== FINAL REPORT ====
Diagnosis     : {diagnosis}
Confidence    : {data['confidence']:.2f}
Detected Tags : {', '.join(data['tags'])}
Explanation   : {rationale}
Recommendations: {suggestions}
=======================
"""
