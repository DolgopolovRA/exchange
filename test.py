import os
from time import perf_counter

folder = 'some_data'
start = perf_counter()
size_threshold = 15 * 2 ** 10
small_files = [item for item in os.listdir(folder) if os.stat(os.path.join(folder, item)).st_size < size_threshold]
print(len(small_files), perf_counter() - start)

start = perf_counter()
small_files_2 = [item.name for item in os.scandir(folder) if item.stat().st_size < size_threshold]
print(len(small_files_2), perf_counter() - start)
print(small_files == small_files_2)

