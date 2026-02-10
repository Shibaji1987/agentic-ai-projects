def get_goal():
    goal = input("Enter your goal: ")
    return goal

def generate_actions(goal):
    actions = [
        f"Step 1: Work on '{goal}' for 30 minutes",
        f"Step 2: Review progress on '{goal}'",
        f"Step 3: Plan next action for '{goal}'"
    ]
    return actions

def provide_feedback():
    print("Discipline beats motivation. Show up tomorrow.")

def main():
    goal = get_goal()
    actions = generate_actions(goal)

    print("\nYour agent suggests:")
    for action in actions:
        print(action)

    provide_feedback()

if __name__ == "__main__":
    main()
