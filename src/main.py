
import csv
from pathlib import Path
from datetime import datetime


def calculate_waiting_time(arrival, assessment):
    if assessment < arrival:
        raise ValueError("Assessment before arrival")

    return (assessment - arrival).total_seconds() / 60


def main():
    # Locate the project folder
    project_dir = Path(__file__).resolve().parent.parent

    # Locate the hospital dataset
    data_file = project_dir / "data" / "emergency_visits.csv"

    # Read the CSV file
    with open(data_file, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        visits = list(reader)

    # Validate hospital data
    seen_visit_ids = set()
    valid_visits = []
    rejected_visits = []

    required_fields = [
        "visit_id",
        "patient_id",
        "arrival_time",
        "assessment_time",
        "urgency_level",
    ]

    allowed_urgency_levels = {"High", "Medium", "Low"}

    for visit in visits:
        errors = []

        # Check required fields
        for field in required_fields:
            if not visit.get(field, "").strip():
                errors.append(f"Missing {field}")

        visit_id = visit.get("visit_id", "").strip()

        # Check duplicate visit IDs
        if visit_id:
            if visit_id in seen_visit_ids:
                errors.append("Duplicate visit ID")
            else:
                seen_visit_ids.add(visit_id)

        # Check urgency level
        if visit.get("urgency_level") not in allowed_urgency_levels:
            errors.append("Invalid urgency level")

        # Validate timestamps and calculate waiting time
        try:
            arrival = datetime.strptime(
                visit["arrival_time"], "%Y-%m-%d %H:%M:%S"
            )
            assessment = datetime.strptime(
                visit["assessment_time"], "%Y-%m-%d %H:%M:%S"
            )

            waiting_time = calculate_waiting_time(arrival, assessment)

        except ValueError as error:
            if str(error) == "Assessment before arrival":
                errors.append("Assessment before arrival")
            else:
                errors.append("Invalid or missing timestamp")
            waiting_time = None

        except KeyError:
            errors.append("Invalid or missing timestamp")
            waiting_time = None

        # Separate valid and rejected records
        if errors:
            rejected_visits.append({
                "visit_id": visit_id or "UNKNOWN",
                "errors": errors,
            })
        else:
            visit["waiting_time_minutes"] = waiting_time
            valid_visits.append(visit)

    # Export valid visits to a new CSV file
    output_file = project_dir / "data" / "cleaned_emergency_visits.csv"

    if valid_visits:
        fieldnames = list(valid_visits[0].keys())

        with open(output_file, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(valid_visits)

    print(f"Cleaned data saved to: {output_file}")

    # Display data quality report
    print("SMART HOSPITAL DATA PLATFORM")
    print("----------------------------")
    print(f"Total records: {len(visits)}")
    print(f"Valid records: {len(valid_visits)}")
    print(f"Rejected records: {len(rejected_visits)}")

    for rejected in rejected_visits:
        print(f"Rejected {rejected['visit_id']}: {rejected['errors']}")

    # Display valid visits
    print("\nVALID EMERGENCY VISITS")

    for visit in valid_visits:
        print(
            f"Visit: {visit['visit_id']} | "
            f"Waiting time: {visit['waiting_time_minutes']:.0f} minutes"
        )

    # Calculate hospital performance indicators
    if valid_visits:
        waiting_times = [
            visit["waiting_time_minutes"]
            for visit in valid_visits
        ]

        average_waiting_time = sum(waiting_times) / len(waiting_times)
        maximum_waiting_time = max(waiting_times)
        minimum_waiting_time = min(waiting_times)

        print("\nHOSPITAL PERFORMANCE INDICATORS")
        print("-------------------------------")
        print(f"Average waiting time: {average_waiting_time:.1f} minutes")
        print(f"Maximum waiting time: {maximum_waiting_time:.0f} minutes")
        print(f"Minimum waiting time: {minimum_waiting_time:.0f} minutes")


if __name__ == "__main__":
    main()
