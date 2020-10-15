import pandas as pd
import pandavro as pdx
from src.utils.logger import logging

LOG = logging.getLogger(__name__)

class Avro():
    def __init__(self,
                 data_type: str):
        self._data_type = data_type

    def write(self,
              avro_file: str,
              pandas_df: pd.DataFrame) -> None:
        if self.data_type in avro_file:
            pdx.to_avro(avro_file,
                        pandas_df)

    def read(self,
             avro_file: str) -> pd.DataFrame:
        return pdx.read_avro(avro_file)

    @property
    def data_type(self):
        return self._data_type
