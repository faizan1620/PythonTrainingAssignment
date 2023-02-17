# Python program that reads a CSV into memory and utilizes asycios to process each line in the CSV
import csv, os, asyncio

async def display_line(reader_obj, writer):
    writer.writerow(['Passenger with id greater than 1000 who survived'])
    writer.writerow(['  - - - - - - - - - - - - - - - - - - - - - -  '])  # Seperator
    ignoreBelowThousand = lambda x: x if x>1000 else None       # Using lambda function
    for row in reader_obj:
        row = list(map(int,row ))       # Using map
        data = filter(ignoreBelowThousand, row)   # Using filter
        id = list(data)
        async with asyncio.Lock():
                writer.writerow(id) if id else None  

async def process_csv(path):
    with open(path) as input_file, open('results.csv', 'w') as csv_out:
        reader_obj = csv.reader(input_file)
        next(reader_obj)                        #  Using next
        writer = csv.writer(csv_out, delimiter=',')
        await display_line(reader_obj, writer)

async def main():  
    path = os.path.join('data','titanic.csv')
    await process_csv(path)


asyncio.run(main())