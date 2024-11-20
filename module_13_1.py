import asyncio


async def start_strongman(name, power): # name - имя силача, power - его подъёмная мощность
    print(f'Силач {name} начал соревнования')
    for i in range(5):
        number = i + 1
        await asyncio.sleep(i * 5 / power) # задержка поднятия шара обратно пропорциональна power
        print(f'Силач {name} поднял {number} шар')
    print(f'Силач {name} закончил соревнование')


async def start_tournament(): 
    task1 = asyncio.create_task(start_strongman('Pasha', 3))
    task2 = asyncio.create_task(start_strongman('Denis', 4))
    task3 = asyncio.create_task(start_strongman('Apollon', 5))
    await task1
    await task2
    await task3


asyncio.run(start_tournament())
