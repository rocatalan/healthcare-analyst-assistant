from google.adk.agents import LlmAgent
from os import getenv

from .prompt import INSTRUCTIONS

GEMINI_2_5_FLASH = str(getenv("GEMINI_2_5_FLASH"))

completeness_agent = LlmAgent(
    model=GEMINI_2_5_FLASH,
    name="completeness_agent",
    description="Analyze the provided Idea Summary strictly from the perspective of completeness and clear scope definition for an IT project at [City General Hospital]. Your goal is to identify potential gaps, unaddressed high-level scenarios, or ambiguities regarding the boundaries of the proposed idea",
    instruction=INSTRUCTIONS,
    output_key="completeness_review",
)
