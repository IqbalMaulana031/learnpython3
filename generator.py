# list comprehension
values = [x * 2 for x in range(100)]
print("values = ", values)

# generator expression
gen_values = (x * 2 for x in range(100))
print("gen_values = ", gen_values)
print("first evaluation = ", list(gen_values))
print("second evaluation = ", list(gen_values))

# generator = function which return a generator iterator
# every generator is iterator


def simple_gen():
    yield 3
    yield 2
    yield 1
    yield "boom"


simple = simple_gen()
print(next(simple))
print(next(simple))
print(next(simple))
print(next(simple))
try:
    print(next(simple))
except StopIteration:
    print("done")


def square_range(n):
    for i in range(n):
        yield i * i


print("square_range(10) = ", list(square_range(10)))
