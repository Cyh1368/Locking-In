#!/usr/bin/env python3
"""
Demo Script: Locking-In Attention Assistant

This script demonstrates 3 scenarios:
1. Normal usage - allow access
2. Focus meeting - soft block
3. Urgent message - allow with nudge

Run: python demo_script.py
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.decision_engine import DecisionEngine

def demo_scenario(scenario_name, scenario_config, app_opens):
    print(f"\n--- Scenario: {scenario_name} ---")
    engine = DecisionEngine()
    
    for app in app_opens:
        engine.record_app_open(app)
        action, reason = engine.evaluate_action(app, scenario_config.get("scenario", "normal"))
        print(f"Opening {app}: {action.upper()} - {reason}")

def main():
    print("Locking-In Demo Script")
    print("======================")
    
    # Scenario 1: Normal
    demo_scenario("Normal Usage", {"scenario": "normal", "recency_threshold": 10}, ["Instagram", "Gmail"])
    
    # Scenario 2: Focus Meeting
    demo_scenario("Focus Meeting", {"scenario": "focus_meeting", "recency_threshold": 10}, ["Instagram"])
    
    # Scenario 3: Urgent Message
    demo_scenario("Urgent Message", {"scenario": "urgent_message", "recency_threshold": 10}, ["Texts"])

if __name__ == "__main__":
    main()