
-- 1. Number of visits by urgency level

SELECT
    urgency_level,
    COUNT(*) AS total_visits
FROM emergency_visits
GROUP BY urgency_level;


-- 2. Average waiting time by urgency level

SELECT
    urgency_level,
    ROUND(AVG(waiting_time_minutes), 2) AS average_waiting_time
FROM emergency_visits
GROUP BY urgency_level
ORDER BY average_waiting_time DESC;


-- 3. Number of cases by diagnosis category

SELECT
    diagnosis_category,
    COUNT(*) AS total_cases
FROM emergency_visits
GROUP BY diagnosis_category
ORDER BY total_cases DESC;


-- 4. Number of patients by outcome

SELECT
    outcome,
    COUNT(*) AS total_patients
FROM emergency_visits
GROUP BY outcome
ORDER BY total_patients DESC;
