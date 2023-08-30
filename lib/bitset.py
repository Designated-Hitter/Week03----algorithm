from math import ceil


class Bitset:
    bs: list[int]

    BUCKET_BITS = 32
    N: int
    MAX_BUCKET_SIZE: int

    def __init__(self, MAXN: int) -> None:
        self.N = MAXN
        self.MAX_BUCKET_SIZE: int = ceil(self.N / self.BUCKET_BITS)
        self.bs = [0 for _ in range(self.MAX_BUCKET_SIZE)]

    @classmethod
    def bucket_no(cls, idx: int) -> int:
        return idx // cls.BUCKET_BITS

    @classmethod
    def bucket_offset(cls, idx: int) -> int:
        return idx % cls.BUCKET_BITS

    def get(self, idx: int) -> bool:
        return self.bs[self.bucket_no(idx)] >> self.bucket_offset(idx) & 1 == 1

    def set(self, idx: int, to: bool = True):
        if to:
            self.bs[self.bucket_no(idx)] |= 1 << self.bucket_offset(idx)
        else:
            self.bs[self.bucket_no(idx)] ^= 1 << self.bucket_offset(idx)

    def all(self) -> bool:
        """check if all bits are set"""
        # check prev bucket
        if any(x ^ ((1 << self.BUCKET_BITS) - 1) for x in self.bs[:-1]):
            return False

        # last bucket
        offset = self.bucket_offset(self.N)
        check = self.BUCKET_BITS if offset == 0 else offset
        check = (1 << check) - 1
        return self.bs[-1] == check

    def any(self) -> bool:
        """check if any bits are set"""
        return any(self.bs)

    def bulk_set(self, bulk: list[int]):
        """set all from bucket 0"""
        for idx, bucket in enumerate(bulk):
            self.bs[idx] = bucket

    def bulk_get(self, bucket_no: int) -> int:
        return self.bs[bucket_no]
