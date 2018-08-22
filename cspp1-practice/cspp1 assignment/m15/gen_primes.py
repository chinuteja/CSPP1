#define the gen_primes function here
def genPrimes(a):
    n = 2
    x = 0
    while x < a:
        count = 0
        for i in range(1, n):
            if n%i == 0:
                count += 1
        if count == 1:
            yield n
            count += 1
        n += 1

def main():
    data = input()
    l = data.split()
    a = int(l[0])
    b = int(l[1])
    primeGenerator = genPrimes(a)
    for i in range(a):
        p = primeGenerator.__next__()
        if i%b == 0:
            print(p)
    
if __name__ == "__main__":
    main()
