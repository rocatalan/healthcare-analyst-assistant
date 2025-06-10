from google.adk.agents import LlmAgent
from os import getenv

from .prompt import INSTRUCTIONS

GEMINI_2_5_FLASH = str(getenv("GEMINI_2_5_FLASH"))

feasibility_agent = LlmAgent(
    model=GEMINI_2_5_FLASH,
    name="feasibility_agent",
    description="Analyze the provided Idea Summary strictly from a high-level technical perspective, considering potential feasibility challenges, dependencies on existing [City General Hospital] IT systems (EHR, LIS, PACS, etc.), and major integration points.",
    instruction=INSTRUCTIONS,
    output_key="feasibility_review",
)
