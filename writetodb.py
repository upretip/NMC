from scrape import get_doctor_info
import sqlite3

def write_to_sqlite(nmc_number):

    '''
    Use the scrape function from scrape.py and write the data on sqlite database
    @param nmc_number (int): doctor's nmc number
    @returns None

    '''
    with sqlite3.connect("nmc.db") as conn:
        conn.execute(
            """create table if not exists doctors (
            full_name text,
            nmc_number int primary key,
            location text,
            gender text,
            degree text
        )
        """
        )
        conn.execute(
            """insert into doctors values
            (?,?,?,?,?)

            """,
            get_doctor_info(nmc_number)
        )
if __name__ == "__main__":
    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=10) as pool:
        pool.map(write_to_sqlite, list(range(1,20387)))
