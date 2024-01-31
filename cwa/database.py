import certifi
import dns
import mongoengine as db


class DataBase:
    host_name = 'mongodb+srv://events.xfmhxnj.mongodb.net'
    username = 'admin'
    password = 'OGYN9OA6prBilDNK'

    def __init__(self):
        self.archive = None
        dns.resolver.default_resolver = dns.resolver.Resolver(configure=False)
        dns.resolver.default_resolver.nameservers = ['1.1.1.1']

        try:
            db.connect(db='operations',
                       alias='default',
                       host=self.host_name,
                       username=self.username,
                       password=self.password,
                       tlsCAFile=certifi.where())

            db.connect(db='test',
                       alias='test_db',  # custom alias for test database
                       host=self.host_name,
                       username=self.username,
                       password=self.password,
                       tlsCAFile=certifi.where())

            connection = True


        except Exception as e:
            print(e)


