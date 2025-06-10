from google.adk.agents import (
    LlmAgent,
    ParallelAgent,
    SequentialAgent,
)
from .sub_agents.clarity import clarity_agent
from .sub_agents.clinical import clinical_agent
from .sub_agents.completeness import completeness_agent
from .sub_agents.feasibility import feasibility_agent
from .sub_agents.healthcare import healthcare_agent
from .sub_agents.regulatory import regulatory_agent
from .sub_agents.verifiability import verifiability_agent

from .prompt.root import INSTRUCTIONS as ROOT_INSTRUCTIONS
from .prompt.synthesis import INSTRUCTIONS as SYNTHESIS_INSTRUCTIONS

from os import getenv

GEMINI_2_5_PRO = str(getenv("GEMINI_2_5_PRO"))

synthesis_agent = LlmAgent(
    model=GEMINI_2_5_PRO,
    name="synthesis_agent",
    description="Gather topic-wise parallel analysis and synthesize into user instructions drafting documentation",
    instruction=SYNTHESIS_INSTRUCTIONS,
    output_key="synthesis_review",
)

parallel_agent = ParallelAgent(
    name="parallel_agent",
    description="Receives a document draft summary and process distinct topic-wise analysis",
    sub_agents=[
        clarity_agent,
        clinical_agent,
        completeness_agent,
        feasibility_agent,
        healthcare_agent,
        regulatory_agent,
        verifiability_agent,
    ],
)

sequential_agent = SequentialAgent(
    name="sequential_agent",
    description="Routes a document draft summary to further topic-wise analysis",
    sub_agents=[parallel_agent, synthesis_agent],
)

root_agent = LlmAgent(
    model=GEMINI_2_5_PRO,
    name="assistant_agent",
    description="Drives the user in drafting Functional Documents",
    instruction=ROOT_INSTRUCTIONS,
    sub_agents=[sequential_agent],
    output_key="document_draft",
)
