def make_callback_tracker():
    count = 0  # This is enclosed in the closure

    def callback(data):
        nonlocal count
        count += 1
        print(f"[{count}] Got data: {data}")

    return callback  # This is a closure, and also used as a callback


def process_items(items, callback):
    for item in items:
        callback(item)  # Call the passed-in function (callback)

tracker = make_callback_tracker()
process_items(["apple", "banana", "cherry"], tracker)
