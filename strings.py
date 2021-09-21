name = "me"
other = "Motley"

# f string allows us to embed variables in strings.
greeting = f"Hello {name} and {other}"

print(greeting)

name = "them"

# or can do
print(f"Hello {name} and {other}")

# template string reuse
name = "Cherry"
greeting = "Hello, {} and {}"
with_name = greeting.format(name, other)
print(with_name)
