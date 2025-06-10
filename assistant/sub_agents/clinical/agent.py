from google.adk.agents import LlmAgent
from os import getenv

from .prompt import INSTRUCTIONS

GEMINI_2_5_FLASH = str(getenv("GEMINI_2_5_FLASH"))

clinical_agent = LlmAgent(
    model=GEMINI_2_5_FLASH,
    name="clinical_agent",
    description="Analyze the provided Idea Summary strictly from the perspective of its potential impact on existing clinical workflows, the day-to-day experience of hospital staff (clinicians, nurses, technicians, admin), and overall patient safety",
    instruction=INSTRUCTIONS,
    output_key="clinical_review",
)
