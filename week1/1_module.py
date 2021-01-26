#   모듈
import mod2
from mod1 import *
from mod1 import add
import mod1
#   import mod1
print(mod1.add(3, 4))

#   from mod1 import add
print(add(3, 4))

#   from mod1 import *

#

#   import mod2
print(mod2.PI)

a = mod2.Math()
print(a.solv(2))
