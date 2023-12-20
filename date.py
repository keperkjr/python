import datetime

def main():
    # Declare start date
    start_date = datetime.datetime.now()

    print(f'start_date: {start_date}')
    print(f'start_date date only: {start_date.date()}')
    print(f'start_date time only: {start_date.time()}')

    # Short date string
    print(f'start_date toShortDateString: {start_date.strftime("%m/%d/%Y %I:%M:%S %p")}')

    # Short date string with milliseconds
    print(f'start_date toShortDateString: {start_date.strftime("%m/%d/%Y %I:%M:%S.%f %p")}')

    # Add days to date
    end_date = start_date + datetime.timedelta(days=4)
    print(f'end_date: {end_date}')
    print(f'start_date > end_date: {start_date > end_date}')

    # Empty date check
    if not start_date and not end_date:
        print('start end end date are null')

if __name__ == "__main__":
    main()