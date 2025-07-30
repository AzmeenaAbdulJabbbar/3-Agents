# agents/monster_agent.py
from .base_agent import Agent

class MonsterAgent(Agent):
    """Agent responsible for managing combat encounters."""
    
    def __init__(self):
        instructions = """
        You are a goblin warrior! Keep responses SHORT and FUN (1-2 sentences max).
        Be silly and playful, not scary. Use emojis and make combat exciting.
        Examples:
        - "👹 Rawr! I hit you for 3 damage! Ouch!"
        - "😅 Oops! I missed! My bad!"
        - "💀 I'm defeated! Nooo!"
        Keep it light and fun!
        """
        super().__init__("MonsterAgent", instructions)
    
    def handle(self, game_state: dict, tools: dict):
        """Handle combat mechanics."""
        roll_result = tools.get('roll_dice', lambda: 10)()
        if roll_result > 8:
            return "You defeated the monster!", 'item'
        else:
            return "The monster defeated you!", 'end'
    
    async def describe_attack(self, hit: bool, damage: int = 0) -> str:
        """Describe a monster attack in a short, fun way."""
        if hit:
            prompt = f"Say you hit the player for {damage} damage in 1 fun sentence with emojis!"
        else:
            prompt = "Say you missed the player in 1 fun sentence with emojis!"
        return await self.run(prompt)
    
    async def describe_defeat(self) -> str:
        """Describe the monster's defeat in a fun way."""
        prompt = "Say you're defeated in 1 fun sentence with emojis!"
        return await self.run(prompt) 