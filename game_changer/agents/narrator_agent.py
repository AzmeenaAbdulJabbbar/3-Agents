# agents/narrator_agent.py
from .base_agent import Agent

class NarratorAgent(Agent):
    """Agent responsible for narrating the story and managing events."""
    
    def __init__(self):
        instructions = """
        You are a fun Game Master! Keep responses SHORT and EXCITING (max 2-3 sentences).
        Be playful and engaging, not serious. Use emojis and make it feel like a game.
        Examples:
        - "🌲 You find a creepy ruin! What do you do?"
        - "⚔️ A goblin jumps out! Fight or run?"
        - "🎁 You found treasure! Lucky you!"
        Keep it simple and fun!
        """
        super().__init__("NarratorAgent", instructions)
    
    def handle(self, game_state: dict, tools: dict):
        """Handle narration and story progression."""
        event = tools.get('generate_event', lambda: "A mysterious event occurs.")()
        return f"Narrating the story: {event}", 'monster'
    
    async def narrate_event(self, event: str) -> str:
        """Narrate a specific event in a short, fun way."""
        prompt = f"Tell me about this event in 2-3 short, fun sentences with emojis: {event}"
        return await self.run(prompt) 