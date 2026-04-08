import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from calculator import *

def test_add():
    assert add(2, 3) == 5
