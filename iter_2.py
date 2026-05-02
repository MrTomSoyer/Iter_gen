
class FlatIterator:
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def combining_gen(self, list_of_list):
        for item in list_of_list:
            if isinstance(item, list):
                yield from self.combining_gen(item)
            else:
                yield item

    def __iter__(self):
        self.full_generator = self.combining_gen(self.list_of_list)
        return self

    def __next__(self):
        return next(self.full_generator)


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