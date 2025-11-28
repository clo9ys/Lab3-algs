import pytest
from src.stack_list import StackOnList

@pytest.mark.parametrize("value", [52, 17, 104, 23])
def test_push(value):
    st = StackOnList()
    st.push(value)
    assert value in st.lst

def test_pop():
    stack = [52, 17, 104, 23]
    st = StackOnList()
    for i in stack:
        st.push(i)
    popp = st.pop()
    assert popp == stack[-1] and popp not in st.lst

def test_min_peek_len():
    stack = [52, 17, 104, 23]
    st = StackOnList()
    for i in stack:
        st.push(i)
    assert st.min() == min(stack)
    assert st.peek() == stack[-1]
    assert st.__len__() == len(stack)

def test_is_empty():
    st = StackOnList()
    assert st.is_empty()
    st.push(52)
    assert not st.is_empty()

def test_min_peek_pop_exception():
    st = StackOnList()
    with pytest.raises(IndexError):
        st.pop()
    with pytest.raises(IndexError):
        st.peek()
    with pytest.raises(IndexError):
        st.min()