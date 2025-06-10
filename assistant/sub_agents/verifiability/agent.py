from google.adk.agents import LlmAgent
from os import getenv

from .prompt import INSTRUCTIONS

GEMINI_2_5_FLASH = str(getenv("GEMINI_2_5_FLASH"))

verifiability_agent = LlmAgent(
    model=GEMINI_2_5_FLASH,
    name="verifiability_agent",
    description="Analyze the provided Idea Summary strictly from the perspective of ensuring that the proposed outcomes and core functionalities can be objectively verified and tested. Your goal is to identify elements that are currently too subjective or ill-defined for clear success measurement",
    instruction=INSTRUCTIONS,
    output_key="verifiability_review",
)
