from dataclasses import dataclass, field
from typing import List
from datetime import datetime, timedelta


@dataclass
class Task:
    description: str
    time: str
    frequency: str = "once"
    completed: bool = False
    priority: int = 0

    def mark_complete(self):
        self.completed = True

        # Handle daily recurring tasks
        if self.frequency == "daily":
            time_obj = datetime.strptime(self.time, "%H:%M")
            next_time = time_obj + timedelta(days=1)

            return Task(
                description=self.description,
                time=next_time.strftime("%H:%M"),
                frequency=self.frequency
            )

        return None


@dataclass
class Pet:
    name: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        self.tasks.append(task)


class Owner:
    def __init__(self, name: str):
        self.name = name
        self.pets = []

    def add_pet(self, pet: Pet):
        self.pets.append(pet)

    def get_all_tasks(self):
        tasks = []
        for pet in self.pets:
            tasks.extend(pet.tasks)
        return tasks


class Scheduler:
    def __init__(self, owner: Owner):
        self.owner = owner

    def build_schedule(self):
        tasks = self.owner.get_all_tasks()

        schedule = []
        explanations = []
        used_times = set()

        # sort by priority first (AI decision)
        tasks.sort(key=lambda t: (-t.priority, t.time))

        for task in tasks:

            # 🔒 GUARDRAIL (validation)
            if not task.time or ":" not in task.time:
                explanations.append(f"{task.description} skipped due to invalid time")
                continue

            # Validate time format (HH:MM)
            try:
                parts = task.time.split(":")
                if len(parts) != 2:
                    raise ValueError("Invalid time format")
                hours, minutes = int(parts[0]), int(parts[1])
                if not (0 <= hours < 24 and 0 <= minutes < 60):
                    raise ValueError("Hours must be 0-23, minutes must be 0-59")
            except (ValueError, IndexError):
                explanations.append(f"{task.description} skipped due to invalid time")
                continue

            if task.time not in used_times:
                schedule.append(task)
                used_times.add(task.time)
                explanations.append(
                    f"{task.description} scheduled at {task.time} (priority {task.priority})"
                )
            else:
                explanations.append(
                    f"{task.description} skipped due to conflict at {task.time}"
                )

        return schedule, explanations

    # ✅ Improved sorting
    def get_sorted_tasks(self):
        return sorted(
            self.owner.get_all_tasks(),
            key=lambda t: tuple(map(int, t.time.split(":")))
        )

    # ✅ Filtering
    def filter_tasks(self, completed=None, pet_name=None):
        tasks = self.owner.get_all_tasks()

        if completed is not None:
            tasks = [t for t in tasks if t.completed == completed]

        if pet_name:
            tasks = [
                t for pet in self.owner.pets if pet.name == pet_name
                for t in pet.tasks
            ]

        return tasks

    # ✅ Better conflict detection
    def detect_conflicts(self):
        tasks = self.owner.get_all_tasks()
        time_map = {}
        conflicts = []

        for task in tasks:
            if task.time in time_map:
                conflicts.append((task, time_map[task.time]))
            else:
                time_map[task.time] = task

        return conflicts