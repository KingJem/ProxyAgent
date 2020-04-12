from concurrent.futures import ThreadPoolExecutor

from requests import ConnectTimeout
from retrying import retry

from apis import db
from apis.models import RawProxy, UsefulProxy
from utils.utils import to_json

pool = ThreadPoolExecutor(20)


def fetch_proxies():
    proxies = RawProxy.query.filter().limit(5)

    data = to_json(proxies)
    for i in data:
        id_ = i['id']
        RawProxy.query.filter(RawProxy.id == id_).delete()
        db.session.commit()
    return data


def full_path_proxy(protocol, ip_port):
    if protocol.lower() == 'http':
        proxy = {"http": 'http://' + ip_port}
        return proxy
    if protocol.lower() == 'https':
        proxy = {"https": 'https://' + ip_port}
        return proxy


def schedule_tasks():
    data = fetch_proxies()
    for i in data:
        if i['protocol']:
            protocol = i['protocol']
            ip_port = i['ip_port']
            proxy = full_path_proxy(protocol, ip_port)
            ping(proxy, i)
        else:
            i1 = i2 = i
            i1['protocol'] = 'http'
            i2['protocol'] = 'https'
            data.append(i1, i2)
            data.remove(i)


def save_to_db(record):
    print(record)
    proxy_recode = UsefulProxy(**record)
    db.session.add(proxy_recode)
    db.session.commit()


@retry(stop_max_attempt_number=3)
def ping(proxy, record):
    try:
        # res = requests.get(random_target_web(), headers={"User-Agent": UserAgent().random}, timeout=VALIDATOR_TIMEOUT,
        #                    proxies=proxy)
        # if res.status_code == 200:
        record = dict(record)
        record.pop('id')
        save_to_db(record)
    except ConnectTimeout:
        pass


if __name__ == '__main__':
    pool.submit(schedule_tasks)
