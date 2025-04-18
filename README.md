#AIDR-GEN: AI Diagnostic Report Generator

**AIDR-GEN** is a simulation-based AI agent system designed to mimic how healthcare diagnostics can be automated using intelligent agents. This project demonstrates how multi-agent coordination, feedback loops, and memory can be used to generate accurate and explainable diagnostic reports based on patient input.

---

#How It Works

The pipeline involves three collaborating agents:

1. **Data Interpretation Agent (DIA)**  
   Analyzes patient input and generates an initial diagnosis with confidence scoring and symptom tagging.

2. **Validation Agent (VA)**  
   Validates the diagnosis against medical rules and ontology (e.g., valid diagnosis terms, minimum confidence threshold, required symptom tags).

3. **Report Finalization Agent (RFA)**  
   If validation is successful, this agent generates a structured diagnostic report with rationale and recommendations.

If validation fails, the system retries with improved confidence and revised output — simulating a learning loop. This continues for up to **10 attempts**, with the system guaranteed to succeed at least once.

---

## 🔁 Key Features

- Multi-agent architecture (Interpret → Validate → Report)
- Retry loop with confidence boost and feedback tracking
- Memory system for confidence and validation feedback
- Guaranteed successful result in 10 attempts
- Structured clinical-style report output

---

## 🚀 Getting Started

1. Clone this repo:
   ```bash
   git clone https://github.com/AdilIqbal98/AI-Powered-Diagnostic-Report-Generation-System
   cd aidr-gen-pipeline
# AI-Powered-Diagnostic-Report-Generation-System
