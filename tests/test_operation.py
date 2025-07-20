from src.math_operations import add,sub,mul,div

def test_add():
    assert add(2,3)==5
    assert add(-1,1)==0
    assert add(99,5)==104
    
def test_sub():
    assert sub(5,3)==2
    assert sub(4,3)==1
    assert sub(3,3)==0
    assert sub(2,3)==-1

def test_mul():
    assert mul(2,3)==6
    assert mul(-1,1)==-1
    assert mul(0,0)==0
    assert mul(5,2)==10

def test_div():
    assert div(6,3)==2
    assert div(-1,1)==-1
    assert div(0,1)==0
    assert div(25,5)==5


