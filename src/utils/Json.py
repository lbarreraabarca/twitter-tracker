import json
import pandas as pd
from src.utils.logger import logging

LOG = logging.getLogger(__name__)

class Json():
    def __init__(self,
                 dag_info: pd.DataFrame,
                 partition: pd.DataFrame,
                 columns: pd.DataFrame):
        self._dag_info = dag_info
        self._partition = partition
        self._columns = columns
        self._join_df = pd.DataFrame()
        self.join_info_partition()

    def join_info_partition(self):
        self._join_df = pd.merge(self.dag_info,
                                 self.partition,
                                 on='ENTITY')

    def dataframe_to_json(self,
                          filename: str):
        self.join_columns()
        with open('tmp.json', 'w', encoding='utf-8') as file_obj:
            self.join_df.to_json(file_obj,
                                 orient='records',
                                 force_ascii=False)

        with open('tmp.json') as file_obj:
            data = json.load(file_obj)

        with open(filename, 'w', encoding='utf-8') as file_obj:
            for row in data:
                file_obj.write(json.dumps(row) + '\n')

    def join_columns(self):
        self.transform_dict()
        self._join_df = pd.merge(self.join_df,
                                 self.columns,
                                 on='ENTITY')
        column_names = ["COUNTRY",
                        "COMPOSER_NAME",
                        "DAG_NAME",
                        "CRONTAB",
                        "WORDS_CRONTAB",
                        "PARAM_JAR",
                        "PARAM_REQUEST",
                        "RAW_DATA",
                        "BQ_TABLE",
                        "ENTITY",
                        "DATASET",
                        "TABLE_NAME",
                        "DATE_MIN",
                        "DATE_MAX",
                        "VIEW",
                        "ENTITY_COLUMN"]
        self._join_df = self.join_df.reindex(columns=column_names)

    def transform_dict(self):
        columns_list = []
        entities_list = []

        for column in self.columns.to_dict(orient='records'):
            if column['ENTITY'] not in entities_list:
                entities_list.append(column['ENTITY'])

        for entity in entities_list:
            column_desc = {
                'ENTITY': entity
            }
            column_field = []
            for column in self.columns.to_dict(orient='records'):
                if entity == column['ENTITY']:
                    column_field.append({'NAME': column['NAME'],
                                         'DATA_TYPE': column['DATA_TYPE']})
            column_desc['ENTITY_COLUMN'] = column_field
            columns_list.append(column_desc)
        self._columns = pd.DataFrame(columns_list)

    @property
    def dag_info(self):
        return self._dag_info

    @property
    def partition(self):
        return self._partition

    @property
    def columns(self):
        return self._columns

    @property
    def join_df(self):
        return self._join_df
