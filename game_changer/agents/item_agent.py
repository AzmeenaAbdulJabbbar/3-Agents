# agents/item_agent.py
from .base_agent import Agent

class ItemAgent(Agent):
    """Agent responsible for managing rewards and inventory items."""
    
    def __init__(self):
        instructions = """
        You are a magical chest! Keep responses SHORT and FUN (1-2 sentences max).
        Be excited and playful about rewards. Use emojis and make it feel special.
        Examples:
        - "🎁 You found a Health Potion! Drink up!"
        - "⚔️ A Sword of Light! Shiny!"
        - "💎 Magic Ring! Fancy!"
        Keep it simple and exciting!
        """
        super().__init__("ItemAgent", instructions)
    
    def handle(self, game_state: dict, tools: dict):
        """Handle reward distribution."""
        reward = tools.get('get_reward', lambda: "Mysterious Item")()
        return f"You found a {reward}!", 'narrator'
    
    async def announce_reward(self, reward: str) -> str:
        """Announce a reward found by the player in a short, fun way."""
        prompt = f"Announce that the player found '{reward}' in 1 fun sentence with emojis!"
        return await self.run(prompt)
    
    async def describe_item(self, item_name: str) -> str:
        """Describe a specific item's properties in a fun way."""
        prompt = f"Describe '{item_name}' in 1 fun sentence with emojis!"
        return await self.run(prompt) 