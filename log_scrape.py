import sqlite3
from nmc.writetodb import write_to_sqlite

with sqlite3.connect('nmc.db') as conn:
    cur = conn.cursor()
    cur.execute('select nmc_number from doctors')
    row = cur.fetchall()
    scraped = [id[0] for id in row]

to_scrape = [id for id in range(1,20390) if id not in scraped]

if __name__ == "__main__":
    from concurrent.futures import ThreadPoolExecutor

    with ThreadPoolExecutor() as pool:
        pool.map(write_to_sqlite, to_scrape)