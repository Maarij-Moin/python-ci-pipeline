from src.math_operations import add, div, sub
def test_add():
    assert add(2,3)==5
    assert add(-4,5)==1
    assert add(-5,2)==-3
    
    
def test_sub():
    assert sub(4,5)==-1
    assert sub(5,1)==4
    assert sub(0,0)==0
    assert sub(5,5)==0
    
def test_div():
    assert div(10,2)==5
    assert div(9,3)==3
    assert div(5,2)==2.5
