# python-multithread-example

Multi-threaded Python 3 script examples

These scripts are Python3-native and don't require any _pip install_.

## Simple multi-thread

The first example provided to you is a simple script prints the given figure and sleeps during `0.1` seconds.

See [`multithread.py`](./multithread.py)

You can adjust the number of workers [at line 15 `concurrent.futures.ThreadPoolExecutor(max_workers=4)`](./multithread.py#L15)

### Benchmark

- `multithread_benchmark.py`, 20 workers : `5.01298189163208 seconds`
- `no_multithread_benchmark.py` : `100.09807777404785 seconds`

## Multi-thread download (SQLite example)

Let's say you want to download files associated to each user listed in your SQLite database with that format :

```csv
user_id,file_url
1,https://i.imgur.com/XTOuirC.jpg
2,https://i.imgur.com/ddOusrC.jpg
```

Then, use the [`multithread_sqlite.py`](./multithread_sqlite.py) example !

You can adjust the number of workers [at line 34 `concurrent.futures.ThreadPoolExecutor(max_workers=4)`](./multithread_sqlite.py#L34)

## Multi-threaded asyncio subprocesses

OK so that's not enough of a speed for you... I understand. Let's try to mix Asyncio with multi-threads then !

Understanding multi-threading vs async processes :

- Thread 1, tasks A & B : task A1 is run, then task B1 is run
- Thread 1, async tasks A & B : task A1 is parallely run with task B1
- Theads 1 & 2, tasks A & B : task A1 is simultaneously run with task A2, then task B1 is run simultaneously with task B2
- Theads 1 & 2, async tasks A & B : task A1 is parallely run with task B1 simultaneously with task A2 parallely run with task B2

_TODO_
