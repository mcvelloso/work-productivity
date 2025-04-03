#!/usr/bin/env python3.13

import argparse
from datetime import date

import pandas as pd
import pandas_market_calendars as mcal


def calculate_workdays(start_date, end_date):
    """
    Calculate total possible workdays between two dates, excluding weekends.

    :param start_date: The start date (YYYY-MM-DD)
    :param end_date: The end date (YYYY-MM-DD)
    :return: Integer count of workdays.
    """

    if end_date is None:
        end_date = date.today()
    else:
        end_date = pd.to_datetime(end_date)

    start_date = pd.to_datetime(start_date)

    all_dates = pd.date_range(start_date, end_date, freq='D', inclusive='both')

    return len([d for d in all_dates if d.weekday() < 5])


def calculate_holidays(start_date, end_date):
    """
    Calculate the number of NYSE holidays between two dates (inclusive).

    :param start_date: The start date (YYYY-MM-DD)
    :param end_date: The end date (YYYY-MM-DD)
    :return: Integer count of the NYSE holidays within the range
    """

    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

    all_holidays = mcal.get_calendar('NYSE').holidays().holidays

    return len([d for d in all_holidays if start_date <= pd.to_datetime(d) <= end_date])


def calculate_work_performance(days_in_office, work_days, holidays, sick_days, days_off):
    """
        Calculate work performance.

        :param days_in_office: Number of days in office
        :param work_days: Number of possible work days
        :param holidays: Number of holidays
        :param sick_days: Number of sick days
        :param days_off: Number of days off
        :return: Work performance measured as a percentage
        """

    excluded_days = holidays + sick_days + days_off

    return round((days_in_office / (work_days - excluded_days)) * 100, 2)


def main():
    parser = argparse.ArgumentParser(description="Calculate workdays between two dates.")

    parser.add_argument("--days-in-office", type=int, required=True, help="Number of days in office")
    parser.add_argument("--start-date", type=str, required=True, help="Start date in YYYY-MM-DD format")
    parser.add_argument("--end-date", type=str, default=date.today(),
                        help="End date in YYYY-MM-DD format (optional; defaults to today's date)")
    parser.add_argument("--holidays", type=int, default=None,
                        help="Number of holidays (optional; defaults to NYSE holidays)")
    parser.add_argument("--sick-days", type=int, default=0,
                        help="Number of sick days (optional; defaults to 0)")
    parser.add_argument("--days-off", type=int, default=0,
                        help="Number of days off (optional; defaults to 0)")

    args = parser.parse_args()

    try:
        workdays = calculate_workdays(args.start_date, args.end_date)
        holidays = args.holidays if args.holidays is not None else calculate_holidays(args.start_date, args.end_date)
        work_performance = calculate_work_performance(args.days_in_office, workdays, holidays, args.sick_days,
                                                      args.days_off)

        print(f"Number of workdays: {workdays}")
        print(f"Number of holidays: {holidays}")
        print(f"Work Performance: {work_performance}%")
    except Exception as e:
        print(f"Error: {e}")
        print("Please provide valid dates in YYYY-MM-DD format.")


if __name__ == "__main__":
    main()
