from dataclasses import dataclass
import jiant.tasks.lib.senteval.base as base
from jiant.tasks.lib.templates.shared import labels_to_bimap


@dataclass
class Example(base.Example):
    @property
    def label_to_id(self):
        return SentEvalBigramShiftTask.LABEL_TO_ID


@dataclass
class TokenizedExample(base.TokenizedExample):
    pass


@dataclass
class DataRow(base.DataRow):
    pass


@dataclass
class Batch(base.Batch):
    pass


class SentEvalBigramShiftTask(base.BaseSentEvalTask):
    Example = Example
    TokenizedExample = TokenizedExample
    DataRow = DataRow
    Batch = Batch

    LABELS = ["I", "O"]
    LABEL_TO_ID, ID_TO_LABEL = labels_to_bimap(LABELS)
