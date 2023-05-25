# Python program that reads a CSV into memory and utilizes asycios to process each line in the CSV
import csv
import asyncio


async def display_line(reader_obj, writer):
    writer.writerow(["Passenger with id greater than 1000 who survived"])
    writer.writerow(["  - - - - - - - - - - - - - - - - - - - - - -  "])  # Seperator
    for row in reader_obj:
        print(row)
        await write_result(row, writer)


# This function taking the id and keeping only that id which is greater than 1000 which survived, to a results.csv file
async def write_result(result, writer):
    async with asyncio.Lock():  # lock for gracefully write to shared file object
        # id = -1 # Initialise with some invalid id
        # if result[0] != 'PassengerId':
        id = int(result[0])
        if id > 1000 and int(result[1]):
            writer.writerow([id])


async def process_csv(path):
    with open(path) as input_file, open("results.csv", "w") as csv_out:
        reader_obj = csv.reader(input_file)
        next(reader_obj)
        writer = csv.writer(csv_out, delimiter=",")

        await display_line(reader_obj, writer)


async def main():
    path = "data/titanic.csv"
    task1 = asyncio.create_task(process_csv(path))

    await task1


asyncio.run(main())
