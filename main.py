'''
5.Determină dacă un număr dat este palindrom.
'''

def is_palindrome(n) -> bool:
    '''
    Verifica daca un numar este palindrom ( daca numarul este egal cu oglinditul sau)
    :param n: un numar natural
    :return: True daca n este palindrom si False, altfel
    '''
    cn=n
    og=0
    while n!=0:
        og=og*10+n%10
        n=n//10
    if cn==og:
        return True
    return False

def test_is_palindrome():
    assert is_palindrome(121) == True
    assert is_palindrome(168) == False
    assert is_palindrome(1001) == True
test_is_palindrome()

'''
1.Găsește ultimul număr prim mai mic decât un număr dat.
'''
def get_largest_prime_below(n):
    '''
    Scade din numarul dat pana ajunge la primul numar prim
    :param n: un numar natural
    :return: numar natural -reprezinta ultimul numar prim mai mic decat un numar dat
    '''

    x=0
    for d in range (2,n-1):
        ok=1
        for i in range (2,d//2):
            if d%i==0:
                ok==0
        if ok==1 and d>x:
            x=d
    return x

def test_get_largest_prime_below():
    assert get_largest_prime_below(18)==17
    assert get_largest_prime_below(5)==3
    assert get_largest_prime_below(36)==31
test_get_largest_prime_below()
