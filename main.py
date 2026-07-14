"""
=========================================================
 Cognifyz Data Analysis Project
 Author : Abhinav Kadam
=========================================================
"""

import os

def print_header():
    print("=" * 60)
    print("        Cognifyz Data Analysis Project")
    print("=" * 60)


def show_project_structure():
    print("\nProject Structure")
    print("-" * 60)

    folders = [
        "data/raw",
        "data/processed",
        "notebooks",
        "src",
        "visuals",
        "outputs",
        "reports"
    ]

    for folder in folders:
        status = "✓" if os.path.exists(folder) else "✗"
        print(f"{status} {folder}")


def show_notebooks():
    print("\nProject Notebooks")
    print("-" * 60)

    notebooks = [
        "01_Data_Cleaning.ipynb",
        "02_Level_1_Analysis.ipynb",
        "03_Level_2_Analysis.ipynb",
        "04_Level_3_Analysis.ipynb"
    ]

    for notebook in notebooks:
        print(f"• {notebook}")


def show_completed_tasks():
    print("\nCompleted Internship Tasks")
    print("-" * 60)

    tasks = [
        "Level 1 - Top Cuisines",
        "Level 1 - City Analysis",
        "Level 1 - Price Range Distribution",
        "Level 1 - Online Delivery",

        "Level 2 - Restaurant Ratings",
        "Level 2 - Cuisine Combination",
        "Level 2 - Geographic Analysis",
        "Level 2 - Restaurant Chains",

        "Level 3 - Restaurant Reviews",
        "Level 3 - Votes Analysis",
        "Level 3 - Price Range vs Online Delivery & Table Booking"
    ]

    for task in tasks:
        print(f"✓ {task}")


def main():

    print_header()

    show_project_structure()

    show_notebooks()

    show_completed_tasks()

    print("\nProject Status : COMPLETED")

    print("=" * 60)


if __name__ == "__main__":
    main()