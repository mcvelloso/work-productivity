#!/usr/bin/env python3.13
import argparse
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
    parser = argparse.ArgumentParser(description="Calculate workdays between two dates.")

    parser.add_argument("--start-date", type=str, required=True, help="Start date in YYYY-MM-DD format")
    parser.add_argument("--end-date", type=str, default=None,
                        help="End date in YYYY-MM-DD format (optional; defaults to today's date)")

    args = parser.parse_args()

    try:
        workdays = calculate_workdays(args.start_date, args.end_date)
        print(f"Number of workdays: {len(workdays)}")
        # print("Workdays:", [d.date() for d in workdays])
    except Exception as e:
        print(f"Error: {e}")
        print("Please provide valid dates in YYYY-MM-DD format.")


if __name__ == "__main__":
    main()
