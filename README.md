## Project Evolution

This project is an extension of my PawPal+ system from Module 2. The original system only displayed tasks, but this version adds AI-like scheduling, conflict detection, and explanations.

---

## 🚀 Features

- Add pets and tasks
- View daily schedule
- Tasks sorted by time
- Filter tasks by status
- Detect scheduling conflicts
- Support for recurring (daily) tasks

---

## 🧠 Smarter Scheduling

- Tasks are sorted using time-based logic
- Conflicts are detected when tasks share the same time
- Recurring tasks automatically generate new instances
- Filtering allows viewing tasks by completion status

---

## 🧪 Testing PawPal+

Run tests using:

```bash
python -m pytest

## System Architecture

User → Streamlit UI → Scheduler → Tasks → Output

The Scheduler processes tasks, detects conflicts, and generates explanations.

## 🧩 System Design (UML)

```mermaid
classDiagram

class Owner {
  +name
  +pets
  +add_pet()
  +get_all_tasks()
}

class Pet {
  +name
  +tasks
  +add_task()
}

class Task {
  +description
  +time
  +frequency
  +completed
  +mark_complete()
}

class Scheduler {
  +owner
  +get_sorted_tasks()
  +filter_tasks()
  +detect_conflicts()
}

Owner --> Pet
Pet --> Task
Scheduler --> Owner

## Experiments Tried

### Scenario 1: No Conflict
- Tasks: Feed (08:00), Walk (09:00)
- Result: Both tasks scheduled
- Explanation: No conflicts detected

### Scenario 2: Conflict at Same Time
- Tasks: Feed (08:00), Walk (08:00)
- Result: Only one task scheduled
- Explanation: Lower priority task skipped due to conflict

### Scenario 3: Multiple Pets
- Dog: Feed (08:00)
- Cat: Feed (08:00)
- Result: Only one task scheduled
- Explanation: Conflict detected across pets, one task skipped

## Testing Summary

I tested the system using different scenarios:

- No conflict → all tasks scheduled correctly
- Same time tasks → one task skipped
- Multiple pets → conflicts handled across pets

All scenarios worked as expected. The system consistently avoided scheduling conflicts and provided explanations.

## Sample Interaction

Input:
- Feed dog at 08:00
- Walk dog at 08:00

Output:
- Feed scheduled
- Walk skipped due to conflict

Explanation:
"Walk skipped due to conflict at 08:00"

## Reflection

This project helped me understand how scheduling systems work and how conflicts can be resolved automatically.

I learned how to design a system that not only schedules tasks but also explains decisions. The explanation feature made it easier to understand why certain tasks were chosen or skipped.

I also realized that even simple systems can behave differently under different scenarios, which makes testing very important.