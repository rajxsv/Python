x = y = z = 10


fruits = ["a","c","d"]
x,y,z = fruits

str = "1" + "1"
print(str)
print(x,y,z)

x = "global,x"

def fn(message):
  global x 
  # x = "fn,x"
  print(x,message)

fn("Hi")

x = 5 + 1j

print(x)

x = complex(1)
print(x)

x = bytearray(10)
print(x)
