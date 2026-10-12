from molly import build_study_plan, recommend_breaks


def test_build_study_plan_prioritizes_focus():
    tasks = [
        {"name": "AP CSP review", "subject": "Computer Science", "minutes": 30, "priority": "High", "priority_score": 5},
        {"name": "Math quiz practice", "subject": "Math", "minutes": 25, "priority": "Medium", "priority_score": 3},
    ]
    plan = build_study_plan(tasks, 40, "Computer Science")
    assert plan[0]["name"] == "AP CSP review"
    assert sum(task["minutes"] for task in plan) <= 40


def test_build_study_plan_handles_time_limit():
    tasks = [
        {"name": "Biology vocabulary", "subject": "Science", "minutes": 20, "priority": "Medium", "priority_score": 2},
        {"name": "Chemistry equations", "subject": "Science", "minutes": 25, "priority": "High", "priority_score": 4},
    ]
    plan = build_study_plan(tasks, 30, "Science")
    assert sum(task["minutes"] for task in plan) <= 30


def test_recommend_breaks():
    assert recommend_breaks(100) == 2
    assert recommend_breaks(60) == 1
    assert recommend_breaks(20) == 0
