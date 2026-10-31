
import psycopg
import csv
from pathlib import Path


def get_connection():
    connection = psycopg.connect(
        host="localhost",
        port=5432,
        dbname="smart_hospital_db",
        user="postgres",
        password="hhhgoulwlh"
    )

    return connection


def load_data():
    project_dir = Path(__file__).resolve().parent.parent
    csv_file = project_dir / "data" / "cleaned_emergency_visits.csv"

    connection = get_connection()

    try:
        with open(csv_file, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            with connection.cursor() as cursor:
                for row in reader:
                    cursor.execute(
                        """
                        INSERT INTO emergency_visits (
                            visit_id,
                            patient_id,
                            department,
                            arrival_time,
                            assessment_time,
                            urgency_level,
                            diagnosis_category,
                            outcome,
                            waiting_time_minutes
                        )
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                        ON CONFLICT (visit_id) DO NOTHING
                        """,
                        (
                            row["visit_id"],
                            row["patient_id"],
                            row["department"],
                            row["arrival_time"],
                            row["assessment_time"],
                            row["urgency_level"],
                            row["diagnosis_category"],
                            row["outcome"],
                            float(row["waiting_time_minutes"])
                        )
                    )

        connection.commit()
        print("SUCCESS: Data loaded into PostgreSQL!")

    except Exception as error:
        connection.rollback()
        print("Error:", error)

    finally:
        connection.close()


if __name__ == "__main__":
    load_data()
