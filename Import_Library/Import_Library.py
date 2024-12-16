# การ Import library
"""
(ก่อนที่จะ import ต้องติดตั้งก่อน)
 * แบบที่ 1 : import library_name as var
 * แบบที่ 2 : import library_name
 * แบบที่ 3 : from library_name import method
 * แบบที่ 4 : from library_name import *
 
"""

# แบบที่ 1
# numpy 
import numpy as np
# เรีกยใช้
ืnp.zeros(10)

# แบบที่ 2 
import numpy
numpy.zeros(10)

# แบบที่ 3
from numpy import zeros
zeros(10)

# แบบที่ 4 
from numpy import *
zeros(10)