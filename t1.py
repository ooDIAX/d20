import multiprocessing
import time

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def chunk_sum(N):
    num_cores = multiprocessing.cpu_count()
    chunk_size = N // num_cores
    pool = multiprocessing.Pool(num_cores)
    terms = pool.starmap(sum_primes, [(k*chunk_size, (k+1)*chunk_size) for k in range(num_cores)])

    ans = 0
    for i in range(num_cores):
        ans += terms[i]

    return ans

    
def sum_primes(l ,r):
    total = 0
    for i in range(l, r):
        if is_prime(i):
            total += i
    return total


if __name__ == "__main__":

    num_cores = multiprocessing.cpu_count()
    #for simplicity make N divisible by num_cores
    start = time.time()
    print(sum_primes(1, num_cores*1000000))
    end = time.time()
    print("withouth multiprocessing : ", end-start)

    start = time.time()
    print(chunk_sum(num_cores*1000000))
    end = time.time()
    print("with multiprocessing : ", end-start)

