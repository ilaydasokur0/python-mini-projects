from .db import init_db
from .constants import STATUSES
from .services import add_application, list_applications, top_skills


def print_apps(rows):
    if not rows:
        print("No records.")
        return
    for r in rows:
        print(f"[{r['id']}] {r['company']} - {r['role']} | {r['status']} | {r['created_at']}")


def main():
    init_db()

    while True:
        print("\n--- Job Tracker ---")
        print("1) Add application")
        print("2) List applications")
        print("3) Top skills")
        print("0) Exit")

        choice = input("Choose: ").strip()

        if choice == "1":
            company = input("Company: ").strip()
            role = input("Role: ").strip()
            print("Statuses:", ", ".join(STATUSES))
            status = input("Status (enter=Applied): ").strip() or "Applied"

            print("\nPaste requirements (finish with empty line):")
            lines = []
            while True:
                line = input()
                if line == "":
                    break
                lines.append(line)
            req_text = "\n".join(lines)

            app_id = add_application(company, role, status, requirements_text=req_text)
            print(f"Added application. id={app_id}")

        elif choice == "2":
            rows = list_applications()
            print_apps(rows)

        elif choice == "3":
            rows = top_skills(10)
            if not rows:
                print("No skills yet.")
            else:
                for r in rows:
                    print(f"{r['skill']}: {r['freq']}")

        elif choice == "0":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()