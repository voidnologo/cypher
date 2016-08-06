
def system_dictionary():
    with open('/usr/share/dict/words', 'r') as f:
        return set(f.read().split('\n'))


def iwp_dictionary():
    with open('dictionary.txt', 'r') as f:
        return set(f.read().split('\n'))
