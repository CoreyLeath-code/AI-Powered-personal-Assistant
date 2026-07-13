"""Autonomous assistant supervisor and worker routing primitives."""

import logging
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger("Assistant_Supervisor")


@dataclass(frozen=True)
class RouteResult:
    """Structured result for a routed assistant task."""

    agent: str
    prompt: str
    status: str
    output: str


class WorkerAgents:
    """Specialized workers executing actions within protected operational sandboxes."""

    @staticmethod
    def run_memory_lookup(query: str) -> str:
        logger.info("[Memory Agent] Accessing vector store context for: %s", query)
        return "Context Retrieved: User profile context is available for portfolio planning."

    @staticmethod
    def run_web_search(query: str) -> str:
        logger.info("[Search Agent] Dispatching external search for: %s", query)
        return "Live Search: Found repository deployment templates for agentic workflows."

    @staticmethod
    def execute_system_action(action: str) -> str:
        logger.info("[Action Agent] Executing system action: %s", action)
        return "Action complete: Notification safely processed."


class AssistantSupervisor:
    """Central routing hub that parses user intent and directs tasks to workers."""

    def __init__(self, fallback_config: dict, log_path: str | Path = "DailyLog.md"):
        self.config = fallback_config
        self.memory = WorkerAgents()
        self.log_path = Path(log_path)

    def route_and_execute(self, user_prompt: str) -> RouteResult:
        logger.info("Incoming request received: %s", user_prompt)
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

        result = RouteResult(
            agent=agent_target,
            prompt=user_prompt,
            status="SUCCESS",
            output=execution_result,
        )
        logger.info("Supervisor routed intent successfully to [%s].", agent_target)
        self.log_to_daily_file(result)
        return result

    def log_to_daily_file(self, result: RouteResult) -> None:
        log_entry = (
            f"| {datetime.now().strftime('%Y-%m-%d %H:%M')} "
            f"| {result.agent} "
            f"| {result.prompt[:30]}... "
            f"| {result.status} "
            f"| {result.output} |\n"
        )

        try:
            self.log_path.parent.mkdir(parents=True, exist_ok=True)
            with self.log_path.open("a", encoding="utf-8") as file:
                file.write(log_entry)
            logger.info("Task metrics appended to GitOps execution ledger.")
        except OSError as exc:  # pragma: no cover
            logger.error("Failed to append metadata telemetry block: %s", exc)


def default_config() -> dict:
    """Return safe default supervisor configuration."""
    return {
        "llm": {"model": "gpt-4o-mini", "temperature": 0.2, "max_tokens": 500},
        "vector_store": {"dimension": 1536, "similarity_metric": "cosine"},
    }


if __name__ == "__main__":  # pragma: no cover
    supervisor = AssistantSupervisor(default_config())
    supervisor.route_and_execute("Search for latest trends in agentic workflow templates")
