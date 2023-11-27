from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

def test_str():
    jar = Jar()
    assert str(jar) == ""

    jar.deposit(1)
    assert str(jar) == "🍪"

    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.size = 0
    jar.deposit(3)
    assert jar.size==3
    jar.deposit(5)
    assert jar.size==8



def test_withdraw():
    jar = Jar()
    jar.capacity = 12
    jar.size = 12
    jar.withdraw(6)
    assert jar.size == 6