"""Project Euler Problem 19"""
from datetime import datetime, timedelta


def problem_19() -> int:
    """Counting Sundays"""
    check_day = datetime(1901, 1, 1, 0, 0, 0)
    end_day = datetime(2000, 12, 31, 0, 0, 0)
    one_day = timedelta(days=1)
    sun_of_first_month_cnt = 0
    while check_day <= end_day:
        if check_day.day == 1 and check_day.strftime("%a") == "Sun":
            sun_of_first_month_cnt += 1
        check_day += one_day
    return sun_of_first_month_cnt


def judge_leap_year(year: int) -> bool:
    """
    うるう年かどうか判断する。
        True  -> うるう年である
        False -> うるう年ではない
    """
    if (year % 4 == 0) and not (year % 400 != 0 and year % 100 == 0):
        return True
    return False


if __name__ == "__main__":
    print(problem_19())
