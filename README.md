# AI-Powered Requirements Refinement Framework

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Multi-agent AI framework designed to transform ambiguous initial ideas into clear, robust, and well-structured requirements documents through a guided, conversational process.**

---

## The Problem

In complex and regulated industries like healthcare IT, creating clear, complete, and unambiguous business requirements is a significant challenge. Initial ideas are often ill-defined, leading to a development lifecycle plagued by misunderstandings, scope creep, and rework. Business Analysts (BAs) need a more structured and supportive process to explore concepts deeply and ensure all critical facets—from clinical workflow impact to data security—are considered from the outset.

## Our Solution: Project Synapse

Project Synapse provides a sophisticated, multi-phase conversational AI framework that assists Business Analysts in navigating the entire requirements engineering lifecycle. By leveraging specialized AI agents with distinct roles, Synapse guides the BA from a raw concept to a refined, well-documented specification ready for technical implementation.

The framework is built to ensure that final documents are not only clear but also comprehensively analyzed from multiple critical perspectives, drastically improving the quality of requirements and reducing project risk.

## How It Works: The 4-Phase Process

Synapse operates through a structured, four-phase workflow, with each phase building upon the last to progressively refine the initial idea.

### Phase 1: Socratic Idea Elicitation
* An AI dialogue partner, engages the Business Analyst using the **Socratic method.**
* Through a pragmatic, step-by-step conversational exploration, the AI helps the BA to fully articulate, explore, and clarify their initial, unformed idea.
* **Outcome:** A concise, Business Analyst-approved summary that captures the foundational essence, goals, stakeholders, and high-level context of the concept, specifically tailored for a complex environment like healthcare IT.

### Phase 2: Parallel Topic Analysis
* The approved summary from Phase 1 is fed into a set of parallel, specialized AI **"Topic Guides."**
* Each guide is an expert in a specific domain and analyzes the summary *exclusively through that lens*. Core topic guides include:
* **Clarity & Unambiguity**
* **Completeness & Scope Definition**
* **Verifiability & Testability**
* **Healthcare Data & Security** (HIPAA, PHI)
* **Clinical Workflow & Usability**
* **Regulatory & Compliance Prudence**
* **Technical Feasibility & Integration**
* **Outcome:** Seven concise, independent reports detailing potential issues, risks, and critical questions from each specialist perspective.

### Phase 3: Intelligent Synthesis
* A **"Synthesizer"** AI ingests the seven analytical reports from Phase 2.
* It intelligently processes these reports to identify thematic overlaps, consolidate related questions, and prioritize the most critical issues.
* **Outcome:** A single, cohesive **"Refinement Guide."** This guide serves as a structured, prioritized agenda for the next crucial conversation with the BA.

### Phase 4: Guided Refinement & Drafting
* A **"Refinement Facilitator"** AI uses the Refinement Guide to lead a targeted dialogue with the BA.
* This conversation is focused on collaboratively resolving all the identified issues, clarifying ambiguities, and filling in the gaps from the previous analysis.
* As issues are resolved, the AI drafts the final requirements document.
* **Outcome:** A final, well-structured requirements document, formatted in version-control-friendly **Markdown (`.md`)**.

## Key Features

* **Conversational Interface:** An intuitive, AI-led dialogue that feels more like a collaborative partnership than a documentation tool.
* **Socratic Exploration:** Moves beyond simple question-answering to facilitate deep, critical thinking at the project's inception.
* **Multi-Agent Specialist Analysis:** Ensures a 360-degree review of the concept, covering critical angles that might otherwise be missed.
* **Domain-Aware:** Designed with the complexities of regulated industries in mind, using Healthcare IT as a primary model.
* **Structured Markdown Output:** Produces clean, version-control-friendly documents that are easy to integrate into modern development workflows (e.g., Git, Jira, Confluence).

## Who Is This For?

* **Business Analysts** working in complex or regulated environments (Healthcare).
* **Product Managers & Project Managers** seeking to improve the quality and clarity of initial project specifications.
* **Systems Analysts & Requirements Engineers** looking for tools to support a more rigorous elicitation and analysis process.
* **Engineering Leads** who need to ensure that requirements are clear, testable, and well-understood before development begins.

## Getting Started

1. Clone the repository:
```bash
git clone https://github.com/rocatalan/healthcare-analyst-assistant.git
```
2. Set up environment variables
```bash
GOOGLE_CLOUD_PROJECT=<gcp-project>
GOOGLE_CLOUD_LOCATION=<gcp-location>
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_API_KEY=<gemini-api-key>
GEMINI_2_5_PRO="gemini-2.5-pro-preview-05-06"
GEMINI_2_5_FLASH="gemini-2.5-flash-preview-05-20"

```
3. Build the Docker container:
```bash
docker build . -t healthcare-analyst-assistant
```
4. Run the generated container:
```bash
docker run -d -p 8080:8080 healthcare-analyst-assistant
```
4. Open your browser at:
```
http://localhost:8080
```

## Technology Stack

* [**Python 3**](https://www.python.org/) 
* [**Gemini**](https://ai.google.dev/gemini-api/docs)
* [**Google ADK**](https://google.github.io/adk-docs/)

## Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request.

1. Fork the Project.
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the Branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.
