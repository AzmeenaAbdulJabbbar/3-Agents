# agents/base_agent.py
import os
from openai import AsyncOpenAI

class Agent:
    """Base class for all game agents."""
    
    def __init__(self, name: str, instructions: str, model: str = "gpt-4o"):
        self.name = name
        self.instructions = instructions
        self.model = model
        self.client = AsyncOpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
            base_url="https://api.openai.com/v1"
        )
    
    async def run(self, prompt: str) -> str:
        """Run the agent with a given prompt."""
        response = await self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": self.instructions},
                {"role": "user", "content": prompt},
            ],
            temperature=0.7,
        )
        return response.choices[0].message.content
    
    def handle(self, game_state: dict, tools: dict):
        """Handle game state and tools - to be implemented by subclasses."""
        raise NotImplementedError("Subclasses must implement handle method") 