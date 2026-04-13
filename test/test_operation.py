from src.math_operations import add, sub
def test_add():
    assert add(2,3)==5
    assert add(-4,5)==1
    assert add(-5,2)==-3
    
    
def test_sub():
    assert sub(4,5)==-1
    assert sub(5,1)==4
    assert sub(0,0)==0
    assert sub(5,5)==0