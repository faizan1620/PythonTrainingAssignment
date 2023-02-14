# Python program that reads a CSV into memory and utilizes asycios to process each line in the CSV
import csv
import asyncio

async def display_line(reader_obj, writer):
    for row in reader_obj:
        print(row)
        await write_result(row, writer)


# This function taking the id and keeping only that id which is greater than 1000 and savong to a results.csv file
async def write_result(result, writer):
    async with asyncio.Lock():   # lock for gracefully write to shared file object
        res = [id for id in result if id != 'PassengerId' and id != 'Survived' and int(id) > 1000] 
        writer.writerow(res)

async def process_csv(path):
    with open(path) as input_file, open('results.csv', 'a') as csv_out:
        reader_obj = csv.reader(input_file)
        writer = csv.writer(csv_out, delimiter=',')
      
        await display_line(reader_obj, writer)

async def main():  
    path = 'data/titanic.csv' 
    task1 = asyncio.create_task(  
        process_csv(path))  

    await task1
  
asyncio.run(main()) 