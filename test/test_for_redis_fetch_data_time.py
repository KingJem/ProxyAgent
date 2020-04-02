import time

import redis

conn = redis.ConnectionPool(host='127.0.0.1', port='6379')
db = redis.Redis(connection_pool=conn)


def count_time(func):
    def int_time(*args, **kwargs):
        start_time = time.time()  # 这个是程序开始时间
        func()
        over_time = time.time()  # 这个是程序结束时间
        total_time = over_time - start_time
        print('程序共计%s秒' % total_time)

    return int_time


@count_time
def main():
    proxies = db.smembers('raw_proxy')
    print(proxies)

if __name__ == '__main__':
    main()

    # 程序共计0.004836082458496094秒
    # 程序共计0.004379987716674805秒
    # 程序共计0.0049059391021728516秒
    # 程序共计0.004984140396118164秒