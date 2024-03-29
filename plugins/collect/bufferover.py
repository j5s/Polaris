# -*-* coding:UTF-8


class Plugin(Base):
    __info__ = {
        "author": "doimet",
        "references": ["https://dns.bufferover.run"],
        "desc": "bufferover查询",
        "datetime": "2022-01-01"
    }

    def domain(self) -> dict:
        r = self.request(
            method='get',
            url=f'https://dns.bufferover.run/dns',
            params={'q': self.target.value}
        )
        if r.status_code == 200:
            response = r.json()['FDNS_A']
            data = []
            for i in response:
                ip, subdomain = i.split(',')
                data.append({'subdomain': subdomain, 'ip': ip})
            return {'SubdomainList': data}
