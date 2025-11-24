def add(x: int, y: int) ->:
   if not isinstance(x,int) or not isinstance(y,int):
       raise TypeError("Both arguments must be integers")
   return x + y
