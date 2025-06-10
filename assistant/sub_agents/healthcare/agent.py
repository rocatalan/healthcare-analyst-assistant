from google.adk.agents import LlmAgent
from os import getenv

from .prompt import INSTRUCTIONS

GEMINI_2_5_FLASH = str(getenv("GEMINI_2_5_FLASH"))

healthcare_agent = LlmAgent(
    model=GEMINI_2_5_FLASH,
    name="healthcare_agent",
    description="Analyze the provided Idea Summary strictly from the perspective of its implications for patient data (PHI), data security, integrity, and HIPAA compliance within the [City General Hospital] environment. Your goal is to flag areas requiring careful data governance and security consideration",
    instruction=INSTRUCTIONS,
    output_key="healthcare_review",
)
