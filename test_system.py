from pawpal_system import Owner, Pet, Task, Scheduler

def run_tests():
    tests_passed = 0
    tests_failed = 0

    print("\n" + "="*60)
    print("🧪 PawPal+ Test Harness - Evaluation Script")
    print("="*60 + "\n")

    # Test 1: No conflict
    print("Test 1: No Conflict (2 different time slots)")
    try:
        owner = Owner("Test")
        dog = Pet("Dog")
        owner.add_pet(dog)

        dog.add_task(Task("Feed", "08:00"))
        dog.add_task(Task("Walk", "09:00"))

        scheduler = Scheduler(owner)
        schedule, explanations = scheduler.build_schedule()

        if len(schedule) == 2:
            print("✅ PASSED - Both tasks scheduled")
            print(f"   Output: {explanations}")
            tests_passed += 1
        else:
            print(f"❌ FAILED - Expected 2 tasks, got {len(schedule)}")
            tests_failed += 1
    except Exception as e:
        print(f"❌ FAILED - Exception: {e}")
        tests_failed += 1

    print()

    # Test 2: Conflict resolution
    print("Test 2: Conflict Resolution (same time, different priority)")
    try:
        owner = Owner("Test")
        dog = Pet("Dog")
        owner.add_pet(dog)

        task1 = Task("Feed", "08:00")
        task1.priority = 5
        task2 = Task("Play", "08:00")
        task2.priority = 2

        dog.add_task(task1)
        dog.add_task(task2)

        scheduler = Scheduler(owner)
        schedule, explanations = scheduler.build_schedule()

        if len(schedule) == 1 and schedule[0].description == "Feed":
            print("✅ PASSED - High priority task selected, low priority skipped")
            print(f"   Output: {explanations}")
            tests_passed += 1
        else:
            print(f"❌ FAILED - Expected Feed at 08:00, got {[t.description for t in schedule]}")
            tests_failed += 1
    except Exception as e:
        print(f"❌ FAILED - Exception: {e}")
        tests_failed += 1

    print()

    # Test 3: Invalid time format
    print("Test 3: Invalid Time Format (guardrail validation)")
    try:
        owner = Owner("Test")
        dog = Pet("Dog")
        owner.add_pet(dog)

        task = Task("Invalid Task", "25:99")  # Invalid time
        dog.add_task(task)

        scheduler = Scheduler(owner)
        schedule, explanations = scheduler.build_schedule()

        if len(schedule) == 0 and any("invalid time" in e.lower() for e in explanations):
            print("✅ PASSED - Invalid time rejected with explanation")
            print(f"   Output: {explanations}")
            tests_passed += 1
        else:
            print(f"❌ FAILED - Expected rejection, got {schedule}")
            tests_failed += 1
    except Exception as e:
        print(f"❌ FAILED - Exception: {e}")
        tests_failed += 1

    print()

    # Summary
    print("="*60)
    print("📊 Test Summary")
    print("="*60)
    print(f"✅ Passed: {tests_passed}")
    print(f"❌ Failed: {tests_failed}")
    total = tests_passed + tests_failed
    score = (tests_passed / total * 100) if total > 0 else 0
    print(f"📈 Score: {score:.0f}% ({tests_passed}/{total})")
    print("="*60 + "\n")

    return tests_passed == total


if __name__ == "__main__":
    success = run_tests()
    exit(0 if success else 1)

