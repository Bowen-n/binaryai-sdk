from typing import List, Optional


class MatchedFunction(object):
    """Matched function entity by using similarity search.
    Differ from Function class, this class is a matched function result
    with only score, code and other fields, but no bytes and fileoffset
    which represents an function in a executable binary.
    So this is rather not an actual decompiled function.

    Note that this class is experiment and maybe changed in the future.
    """

    def __init__(
        self,
        score: float,
        code: str,
        name: Optional[str] = None,
        url: Optional[str] = None,
        algorithm: Optional[str] = None,
    ) -> None:
        super().__init__()
        self.score = score
        self.code = code
        self.name = name
        self.url = url
        self.algorithm = algorithm


class Function(object):
    """A function entity that represents a decompiled function."""

    def __init__(
        self, name: str,
        offset: int,
        pseudocode: str,
        embedding: Optional[List[float]] = None,
        match: Optional[List[MatchedFunction]] = None,
    ):
        self.name = name
        self.offset = offset
        self.pseudocode = pseudocode
        self.embedding = embedding
        self.match = match
