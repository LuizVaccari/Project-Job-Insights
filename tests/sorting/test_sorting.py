from src.sorting import sort_by


def test_sort_by_criteria():
    jobs = [
        {
            "min_salary": 300,
            "max_salary": 400,
            "date_posted": "2021-12-01",
        },
        {
            "min_salary": 200,
            "max_salary": 500,
            "date_posted": "2021-12-04",
        },
        {
            "min_salary": 400,
            "max_salary": 800,
            "date_posted": "2021-12-07",
        },
    ]

    sorted_by_min_salary = [jobs[1], jobs[0], jobs[2]]

    sort_by(jobs, "min_salary")
    assert jobs == sorted_by_min_salary

    pass
