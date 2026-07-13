from agents.supervisor import AssistantSupervisor, default_config


def test_supervisor_routes_profile_to_memory_agent(tmp_path):
    supervisor = AssistantSupervisor(default_config(), log_path=tmp_path / "DailyLog.md")

    result = supervisor.route_and_execute("Open my portfolio profile")

    assert result.agent == "Memory_Agent"
    assert result.status == "SUCCESS"
    assert "Memory_Agent" in (tmp_path / "DailyLog.md").read_text(encoding="utf-8")


def test_supervisor_routes_latest_to_search_agent(tmp_path):
    supervisor = AssistantSupervisor(default_config(), log_path=tmp_path / "DailyLog.md")

    result = supervisor.route_and_execute("Search latest agent workflows")

    assert result.agent == "Web_Search_Agent"
    assert "Live Search" in result.output


def test_supervisor_routes_unknown_to_action_agent(tmp_path):
    supervisor = AssistantSupervisor(default_config(), log_path=tmp_path / "DailyLog.md")

    result = supervisor.route_and_execute("Send a notification")

    assert result.agent == "System_Action_Agent"
    assert "Action complete" in result.output
