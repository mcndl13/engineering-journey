### *args: Positional argument
```python
def add(*args):
    #args --> tuple --> {a, b, c, ...}
    sum = 0
    for n in args:
        sum += n

add(1, 2, 3, 4)
```

### **kwargs: Key word argument
```python
def calculate(n, **kargs):
    #kargs --> dictonary --> {a:b, c:d, ...}
    n += kargs.get("add") #return None if doesn't exist
    n *= kargs.get("multiply")
    print(n)

calculate(1, add=2, multiply=8)
```

### Using kwargs for classes allowing for more freedom 
```python
class Car:
    
    def __init__(self, *kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = car(make="Nissan", model="Skyline")

```