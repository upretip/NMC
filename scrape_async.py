import asyncio
import aiohttp
from codetiming import Timer
from bs4 import BeautifulSoup


async def task(name, work_queue):

    timer = Timer(text=f"Task {name} elapsed time: {{:.1f}}")

    async with aiohttp.ClientSession() as session:

        while not work_queue.empty():

            url = await work_queue.get()

            print(f"Task {name} getting URL: {url}")

            timer.start()

            async with session.get(url) as response:
                soup = BeautifulSoup(response.text, "html.parser")
                result = soup.find("tbody")
                # for row in result.find_all('tr'):
                #     td = row.find_all('td')

                values = await result
                print(values)

            timer.stop()


async def main():

    """

    This is the main entry point for the program

    """

    # Create the queue of work

    work_queue = asyncio.Queue()

    # Put some work in the queue

    for nmc_id in range(10):

        await work_queue.put(f"https://nmc.org.np/searchPractitioner?nmc_no={nmc_id}")

    # Run the tasks

    with Timer(text="\nTotal elapsed time: {:.1f}"):

        await asyncio.gather(
            asyncio.create_task(task("One", work_queue)),
            asyncio.create_task(task("Two", work_queue)),
        )


if __name__ == "__main__":

    asyncio.run(main())
