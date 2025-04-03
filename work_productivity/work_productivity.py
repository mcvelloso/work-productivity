#!/usr/bin/env python3.13

import sys
from datetime import date

import pandas as pd


def calculate_workdays(start_date, end_date=None):
    """
    Calculate total possible workdays between two dates, excluding weekends.

    :param start_date: The start date (YYYY-MM-DD)
    :param end_date: The end date (YYYY-MM-DD). Defaults to today's date if not provided.
    :return: A list of workdays.
    """
    if end_date is None:
        end_date = date.today()
    else:
        end_date = pd.to_datetime(end_date)

    start_date = pd.to_datetime(start_date)

    all_dates = pd.date_range(start_date, end_date, freq='D', inclusive='both')

    return [d for d in all_dates if d.weekday() < 5]


def main():
    if len(sys.argv) < 2:
        print("Usage: ./work_productivity.py <start_date> [end_date]")
        print("Example: ./work_productivity.py 2015-01-01 2025-01-13")

    start_date = sys.argv[1]
    end_date = sys.argv[2] if len(sys.argv) > 2 else None

    try:
        workdays = calculate_workdays(start_date, end_date)
        print(f"Number of workdays: {len(workdays)}")
        # print("Workdays:", [d.date() for d in workdays])
    except Exception as e:
        print(f"Error: {e}")
        print("Please provide valid dates in YYYY-MM-DD format.")


if __name__ == "__main__":
    main()
