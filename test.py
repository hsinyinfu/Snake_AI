import snake
import numpy as np

a = np.zeros(64).astype('int')
a = a.reshape((8,8))
a[4][2] = 2
a[7][1] = -1
a[1][5] = -1
a[3][6] = -1
a[2][0] = 1
a[2][1] = 1
a[2][2] = 1
a[2][3] = 1
print(a)
score = 10

snake.init()
snake.draw(a, score, False)

a[4][3] = -1
score += 10
snake.draw(a, score, True)
