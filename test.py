from salish import *
import itertools

def display1(item):
    print("Display1:", item)
    return item, item

def display2(item1, item2):
    print("Display2:", item1, item2)
    return {"item1": item1, "item2": item2}

def display3(item1, item2):
    print("Display3:", item1, item2)
    return item1 + item2

def combinations(items):
    yield from itertools.combinations(items, 2)


pipeline = Channel([1, 2, 3]) | display1 | Bind(display2, how="*") | Bind(display3, how="**") | Bind(combinations, how="collect") | display1
pipeline.join()