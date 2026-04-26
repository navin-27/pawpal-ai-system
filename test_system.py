from pawpal_system import Owner, Pet, Task, Scheduler

def run_tests():
    owner = Owner("Test")

    dog = Pet("Dog")
    owner.add_pet(dog)

    # Test 1: no conflict
    dog.add_task(Task("Feed", "08:00"))
    dog.add_task(Task("Walk", "09:00"))

    scheduler = Scheduler(owner)
    schedule, _ = scheduler.build_schedule()

    print("Test 1 Passed" if len(schedule) == 2 else "Test 1 Failed")

    # Test 2: conflict
    dog.tasks.clear()
    dog.add_task(Task("Feed", "08:00"))
    dog.add_task(Task("Walk", "08:00"))

    scheduler = Scheduler(owner)
    schedule, _ = scheduler.build_schedule()
    print("Test 2 Passed" if len(schedule) == 1 else "Test 2 Failed")


if __name__ == "__main__":
    run_tests()
