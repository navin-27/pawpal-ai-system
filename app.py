from pawpal_system import Owner, Pet, Task, Scheduler
import streamlit as st

# ------------------ CONFIG ------------------
st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

# ------------------ SESSION STATE ------------------
if "owner" not in st.session_state:
    st.session_state.owner = Owner("Naveen")

# ------------------ ADD PET ------------------
st.header("🐶 Add a Pet")

pet_name = st.text_input("Pet Name")

if st.button("Add Pet"):
    if pet_name:
        new_pet = Pet(pet_name)
        st.session_state.owner.add_pet(new_pet)
        st.success(f"{pet_name} added!")
    else:
        st.warning("Please enter a pet name")

# ------------------ ADD TASK ------------------
st.header("📋 Add Task")

pet_names = [pet.name for pet in st.session_state.owner.pets]

if pet_names:
    selected_pet = st.selectbox("Select Pet", pet_names)
    task_desc = st.text_input("Task Description")
    task_time = st.text_input("Time (HH:MM)", placeholder="08:00")

    if st.button("Add Task"):
        if task_desc and task_time:
            task = Task(task_desc, task_time)

            for pet in st.session_state.owner.pets:
                if pet.name == selected_pet:
                    pet.add_task(task)

            st.success("Task added!")
        else:
            st.warning("Fill all fields")
else:
    st.warning("Add a pet first!")

# ------------------ DISPLAY SCHEDULE ------------------
st.header("📅 Today's Schedule")

scheduler = Scheduler(st.session_state.owner)
tasks = scheduler.get_sorted_tasks()

if tasks:
    for task in tasks:
        st.write(f"{task.time} - {task.description}")
else:
    st.info("No tasks scheduled yet.")

# ------------------ CONFLICT DETECTION ------------------
conflicts = scheduler.detect_conflicts()

if conflicts:
    st.warning("⚠ Task conflicts detected!")

# ------------------ AI SCHEDULE (NEW FEATURE) ------------------
st.header("🤖 Smart AI Schedule")

if st.button("Generate Smart Schedule"):
    scheduler = Scheduler(st.session_state.owner)
    schedule, explanations = scheduler.build_schedule()

    st.success("AI Schedule Generated!")

    st.write("### 📅 Final Schedule")
    for task in schedule:
        st.write(f"{task.time} - {task.description}")

    st.write("### 🧠 Explanations")
    for e in explanations:
        st.write(e)