from multiprocessing import Pool
import time
def f(x):
    return x*x

if __name__ == '__main__':
    dicts = {'max_position_embeddings': 512}
    print(dicts)

    # with Pool(2) as pool:
    #     # print(p.map(f, [1, 2, 3]))
    #     time.sleep(1)
    #     ret = pool.apply(f, (10,))
    #     print(ret)
    # print('hello')
