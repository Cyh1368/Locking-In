import time
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from src.decision_engine import DecisionEngine

def run_test_scenario(scenario, app_opens):
    engine = DecisionEngine()
    
    switches = 0
    session_times = []
    start_time = time.time()
    
    for app in app_opens:
        engine.record_app_open(app)
        action, _ = engine.evaluate_action(app, scenario)
        if action == "allow":
            switches += 1
            session_times.append(1)  # Mock session time
    
    total_time = time.time() - start_time
    return {
        "scenario": scenario,
        "app_switches": switches,
        "total_session_time": sum(session_times),
        "total_time": total_time
    }

def run_metrics():
    scenarios = ["normal", "no_unread", "urgent_message", "focus_meeting"]
    app_sequence = ["Instagram", "Gmail", "Instagram", "Texts"]
    
    results = []
    for scenario in scenarios:
        result = run_test_scenario(scenario, app_sequence)
        results.append(result)
        print(f"Scenario {scenario}: Switches={result['app_switches']}, Session Time={result['total_session_time']}")
    
    # Save metrics
    with open("metrics.json", "w") as f:
        import json
        json.dump(results, f, indent=2)

if __name__ == "__main__":
    run_metrics()