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
    if n<=2:
        print ("Nu exista")
    else:
        while True:
            n = n - 1
            ok = True
            for i in range(2,n):
                if n%i == 0:
                    ok = False
                    break
            if ok == True:
                print (n)
                break


def test_get_largest_prime_below():
    assert get_largest_prime_below(18) == 17
    assert get_largest_prime_below(5) == 3
    assert get_largest_prime_below(36) == 31

test_get_largest_prime_below()

'''
11. Afișează toți anii bisecți între doi ani dați (inclusiv anii dați).
'''
def get_leap_years(year_1, year_2):
    '''
    Programul afiseaza toti anii bisecti cuprinsi intre cei doi ani dati (inclusiv anii dati)
    :param year_1: un numar natural, primul an dat
    :param year_2: un numar natural, al doilea an dat
    :return: anii bisecti cuprinsi intre cei doi ani dati
    '''
    list = []
    for year in range(year_1, year_2+1):
        if year % 4 == 0:
            list.append(year)
        year = year + 1
    return list

def test_get_leap_years():
    assert(get_leap_years(2002,2016))== [2004,2008,2012,2016]
    assert (get_leap_years(1953, 1980)) == [1956,1960,1964,1968,1972,1976,1980]
    assert (get_leap_years(2017, 2021)) == [2020]

test_get_leap_years()

def main():
    print('''
	    (5.) Palindrom
	    (1.) Largest prime below
	    (11.) Leap years
	''')
    while True:
        x = int(input("Comanda:"))
        if (x == 1):
            # Palindrom
            n = int(input("Introduceti n="))
            print(is_palindrome(n))
        if (x == 2):
            # Largest prime below
            n = int(input("Introduceti n="))
            print(get_largest_prime_below())
        if (x == 3):
            # Leap years
            start = int(input("Scrie primul an: "))
            end = int(input("Scrie al doilea an: "))
            _list = get_leap_years(start, end)
            print(f"Anii bisecti cuprinsi intre cei doi ani dati [{start}, {end}] sunt: " + ", ".join(str(pp) for pp in _list))
        if (x == x):
            break

if __name__ == '__main__':
    main()



