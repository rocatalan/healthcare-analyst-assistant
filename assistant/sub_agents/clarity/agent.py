from google.adk.agents import LlmAgent
from google.adk.agents.callback_context import CallbackContext
from google.genai import types
from typing import Optional
from os import getenv

from .prompt import INSTRUCTIONS

GEMINI_2_5_FLASH = str(getenv("GEMINI_2_5_FLASH"))

clarity_agent = LlmAgent(
    model=GEMINI_2_5_FLASH,
    name="clarity_agent",
    description="Analyze the provided Idea Summary strictly from the perspective of linguistic clarity and unambiguous communication within a hospital IT context. Your goal is to identify any terms or statements that could lead to misinterpretation, ensuring the concept is articulated with precision.",
    instruction=INSTRUCTIONS,
    output_key="clarity_review",
)
