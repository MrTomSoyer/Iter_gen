class FlatIterator:
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.combined = []

    def combining_lists(self, list_of_list):
        for item in list_of_list:
            if isinstance(item, list):
                self.combining_lists(item)
            else:
                self.combined.append(item)

    def __iter__(self):
        self.combining_lists(self.list_of_list)
        self.counter = 0
        return self

    def __next__(self):
        if self.counter == len(self.combined):
            raise StopIteration
        item = self.combined[self.counter]
        self.counter += 1
        return item


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()