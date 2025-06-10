from google.adk.agents import LlmAgent
from os import getenv

from .prompt import INSTRUCTIONS

GEMINI_2_5_FLASH = str(getenv("GEMINI_2_5_FLASH"))

regulatory_agent = LlmAgent(
    model=GEMINI_2_5_FLASH,
    name="regulatory_agent",
    description="Analyze the provided Idea Summary strictly from a high-level perspective of potential intersections with key healthcare regulations (beyond just HIPAA, e.g., FDA if it could be medical device software, data breach notification laws, consent laws) and critical internal [City General Hospital] compliance policies",
    instruction=INSTRUCTIONS,
    output_key="regulatory_review",
)
