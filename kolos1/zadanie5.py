""" Wykorzystując python comprehensions (wyrażenie listowe) napisz funkcję, która będzie zawierała wartość funkcji sinus dla n w
zakresie <0, 360> z krokiem 30. """

import math
sin = [math.sin(x) for x in range(0,360,30)]
print(sin)