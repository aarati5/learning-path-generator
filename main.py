from src.curriculum import generate_learning_path
from src.quiz import generate_quiz, run_quiz
from src.progress import start_new_path, record_score, get_current_module, get_progress_summary

def show_menu():
    print("\n" + "=" * 60)
    print("PERSONAL LEARNING PATH GENERATOR")
    print("=" * 60)
    print("1. Create new learning path")
    print("2. View progress")
    print("3. Take quiz for current module")
    print("4. Exit")

def run():
    print(get_progress_summary())

    while True:
        show_menu()
        choice = input("\nChoose an option (1-4): ").strip()

        if choice == "1":
            goal = input("\nWhat do you want to learn? ").strip()
            level = input("Your current level (beginner/intermediate/advanced): ").strip()
            print("\nGenerating your learning path...")
            modules = generate_learning_path(goal, level)
            if modules:
                start_new_path(goal, level, modules)
                print(f"\nCreated a {len(modules)}-module learning path:")
                for i, m in enumerate(modules):
                    print(f"  {i+1}. {m['module']} (~{m['estimated_hours']} hrs)")
                    print(f"     {m['description']}")
            else:
                print("Could not generate a learning path. Try again.")

        elif choice == "2":
            print("\n" + get_progress_summary())
            current = get_current_module()
            if current:
                print(f"\nCurrent module: {current['module']}")
                print(f"Description: {current['description']}")
            else:
                print("\nAll modules completed! Consider creating a new path for the next goal.")

        elif choice == "3":
            current = get_current_module()
            if not current:
                print("\nNo current module. Create a learning path first, or you've completed all modules.")
                continue

            print(f"\nGenerating quiz for: {current['module']}...")
            questions = generate_quiz(current['module'], current['description'])
            if questions:
                score = run_quiz(questions)
                print(f"\nYour score: {score*100:.0f}%")
                message = record_score(score)
                print(message)
            else:
                print("Could not generate quiz. Try again.")

        elif choice == "4":
            print("Goodbye! Keep learning.")
            break

        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    run()