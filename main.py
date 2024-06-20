from datetime import date, timedelta


def main() -> None:
    # given a date represented by (day, month, year) entered by the user
    # given the number of days from that given day
    # return the new date offseted from the given date

    def get_positive_int(tag: str) -> int:
        while True:
            try:
                inp:str = input(f"Enter a the {tag} (must be a positive number): ")
                ans:int = int(inp)
                if ans > 0:
                    return ans
            except:
                pass

    while True:
        day = get_positive_int(tag="day")
        month = get_positive_int(tag="month")
        year = get_positive_int(tag="year")
        days_offset = get_positive_int(tag="offset")
        curr_date:date = date(year, month, day)
        new_date:date = curr_date + timedelta(days=days_offset)

        print(f'{days_offset} days from {curr_date} is {new_date}')

        should_exit:bool = False
        while True:
            should_continue:str = input('Would you like to continue? (y/n): ')[0].lower()
            if should_continue in ('y', 'n'):
                if should_continue[0].lower() == 'n':
                    should_exit = True
                break

        if should_exit:
            break
            

        

if __name__ == "__main__":
   main() 
