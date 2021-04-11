# python-multithread-example

Multi-threaded Python 3 script examples

These scripts are Python3-native and don't require any _pip install_.

## Simple multithread

The first example provided to you is a simple script printing the square of a list of numbers.

See [`multithread.py`](./multithread.py)

You can adjust the number of workers [at line 13 `concurrent.futures.ProcessPoolExecutor(max_workers=4)`](./multithread.py#L13)

## Multithread download (SQLite example)

Let's say you want to download files associated to each user listed in your SQLite database with that format :

```csv
user_id,file_url
1,https://i.imgur.com/XTOuirC.jpg
2,https://i.imgur.com/ddOusrC.jpg
```

Then, use the [`multithread_sqlite.py`](./multithread_sqlite.py) example !

You can adjust the number of workers [at line 34 `concurrent.futures.ProcessPoolExecutor(max_workers=4)`](./multithread_sqlite.py#L34)
