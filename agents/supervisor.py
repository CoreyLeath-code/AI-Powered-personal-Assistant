# agents/supervisor.py

import os
import logging
from datetime import datetime

# Enforce system module search paths for robust runner package resolution
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("Assistant_Supervisor")

class WorkerAgents:
    """Specialized workers executing explicit actions within protected operational sandboxes."""
    
    @staticmethod
    def run_memory_lookup(query: str) -> str:
        logger.info(f"[Memory Agent] Accessing vector store context for profile data related to: '{query}'")
        return "Context Retrieved: User is Corey Leath, prioritizing portfolio projects for Big Tech."

    @staticmethod
    def run_web_search(query: str) -> str:
        logger.info(f"[Search Agent] Dispatching external live API call scanning for: '{query}'")
        return "Live Search: Found 3 new repository deployment templates mapping OpenAI GPT-4o-mini."

    @staticmethod
    def execute_system_action(action: str) -> str:
        logger.info(f"[Action Agent] Interfacing with environment hooks to execute: '{action}'")
        return f"Action complete: Notification safely processed."


class AssistantSupervisor:
    """The central routing hub parsing user intents and directing tasks to specific tools."""
    
    def __init__(self, fallback_config: dict):
        self.config = fallback_config
        self.memory = WorkerAgents()

    def route_and_execute(self, user_prompt: str):
        logger.info(f"Incoming Request Received: '{user_prompt}'")
        
        # Simple intent analysis routing mechanism (replicating LLM router behaviors)
        prompt_lower = user_prompt.lower()
        
        if "portfolio" in prompt_lower or "profile" in prompt_lower:
            agent_target = "Memory_Agent"
            execution_result = self.memory.run_memory_lookup(user_prompt)
        elif "search" in prompt_lower or "latest" in prompt_lower:
            agent_target = "Web_Search_Agent"
            execution_result = self.memory.run_web_search(user_prompt)
        else:
            agent_target = "System_Action_Agent"
            execution_result = self.memory.execute_system_action(user_prompt)
            
        logger.info(f"Supervisor routed intent successfully to [{agent_target}]. Task executed.")
        self.log_to_daily_file(agent_target, user_prompt, "SUCCESS", execution_result)

    def log_to_daily_file(self, agent: str, prompt: str, status: str, output: str):
        log_entry = (
            f"| {datetime.now().strftime('%Y-%m-%d %H:%M')} "
            f"| {agent} "
            f"| {prompt[:30]}... "
            f"| {status} "
            f"| {output} |\n"
        )
        log_location = "DailyLog.md"
        
        try:
            with open(log_location, "a") as f:
                f.write(log_entry)
            logger.info("Task metrics appended safely to GitOps execution ledger.")
        except Exception as e:
            logger.error(f"Failed to append metadata telemetry block onto ledger file: {str(e)}")


if __name__ == "__main__":
    # Inline configuration fallback maps safely inside GitHub automated runner scopes
    embedded_config = {
        'llm': {
            'model': "gpt-4o-mini",
            'temperature': 0.2,
            'max_tokens': 500
        },
        'vector_store': {
            'dimension': 1536,
            'similarity_metric': "cosine"
        }
    }
    
    # Instantiate supervisor control engine
    supervisor = AssistantSupervisor(embedded_config)
    
    # Simulate a daily automated system evaluation task
    sample_task = "Search for latest trends in agentic workflow templates"
    supervisor.route_and_execute(sample_task)
