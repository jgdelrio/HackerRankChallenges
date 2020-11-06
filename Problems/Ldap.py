
class LdapEntry:
    """
    This is a class for LDAP entries
    Expected behaviour when the key is not available is not very clear (error?, None?)
    Neither is the behaviour about the arrays. Get first entry for givenName or only transform
    from list to single entry when the arrays contain a unique value?

    This lack of definition in the requirements leads to a decoupling from the stakeholder expectations....
    """
    def __init__(self, ldap_object):
        # allocate dictionary of keys for case-insentitivity
        definition_dict = {
            'objectclass': ('objectclass', self.to_list),
            'cn': ('cn', self.get_first_string),
            'givenname': ('givenName', self.get_first_string),
            'sn': ('sn', self.get_first_string),
            'uidnumber': ('uidNumber', self.to_integer),
            'gidnumber':  ('gidNumber', self.to_integer),
            'mail': ('mail', self.to_list),
        }

        for key, val in ldap_object.items():
            key = key.lower()
            setattr(self, definition_dict[key][0], definition_dict[key][1](val))

        # Error if any of the keys is missing? None? Expected behaviour has not been defined in the requirements...
        for key, val in definition_dict.items():
            if val[0] not in self.__dict__:
                setattr(self, val[0], None)

    @staticmethod
    def to_list(val):
        return [k.decode("utf-8") for k in val]

    @staticmethod
    def get_first_string(val):
        # It is not clear If the first value is the expected or a different behaviour
        return val[0].decode("utf-8")

    @staticmethod
    def to_integer(val):
        return int(val[0])


def test_LdapEntry():
    ldapdict = {
        'objectclass': [b'inetOrgPerson', b'person'],
        'cn': [b'George Orwell'],
        'givenName': [b'George'],
        'sn': [b'Orwell'],
        'uidNumber': [b'1984'],
        'gidNumber': [b'1984'],
        'mail': [
            b'george.orwell@example.com',
            b'big.brother@example.com',
        ],
    }

    e = LdapEntry(ldapdict)
    assert (e.cn == 'George Orwell')
    assert (e.uidNumber == 1984)
    assert ('big.brother@example.com' in e.mail)
    assert (len(e.mail) == 2)


from itertools import islice, chain


def batch_iterator(items, size=10):
    """Works with lists and iterables"""
    iterator = iter(items)
    for i in range(0, len(items), size):
        batch = [k for k in islice(iterator, size)]
        idx = range(i, i+len(batch))
        yield list(idx), batch


def batch_iterator(items, size=10):
    """Works with generators"""
    iterator = iter(items)
    counter = 0
    for i in iterator:
        def batch():
            yield i
            for extra in islice(iterator, size-1):
                yield extra

        new_batch = [k for k in batch()]
        idx = range(counter, counter + len(new_batch))
        counter += size
        yield list(idx), new_batch

# def head(iterable, max=10):
#     first = next(iterable)  # raise exception when depleted
#
#     def head_inner():
#         yield first  # yield the extracted first element
#         for cnt, el in enumerate(iterable):
#             yield el
#             if cnt + 1 >= max:  # cnt + 1 to include first
#                 break
#
#     return head_inner()


if __name__ == '__main__':
    # items = iter(range(98, 0, -1))
    #
    # result = batch_iterator(items)
    # for k in result:
    #     print(k)
    test_LdapEntry()
