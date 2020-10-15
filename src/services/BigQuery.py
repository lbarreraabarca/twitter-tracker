import pandas as pd
from google.cloud import bigquery
from src.utils.logger import logging
from src.utils.CommandLine import CommandLine


LOG = logging.getLogger(__name__)

class BigQuery():

    def __init__(self,
                 project_id: str):
        self._project_id = project_id

    def load(self,
             table_name: str,
             file: str,
             schema: str):
        cmd = """ bq load --quiet \\
                --project_id={project_id} \\
                --source_format=NEWLINE_DELIMITED_JSON \\
                --replace=True \\
                {table_name} \\
                {file} \\
                {schema}
            """.format(project_id=self.project_id,
                       table_name=table_name,
                       file=file,
                       schema=schema)
        LOG.info('Load bq to {}.{}'.format(self.project_id, table_name))
        cmd_line = CommandLine(cmd=cmd,
                               capture_output=False)
        cmd_line.run()

    def update_view(self,
                    project_id: str,
                    view_name: str,
                    query: str):
        cmd = """ bq update \\
                    --use_legacy_sql=false \\
                    --project_id {project_id} \\
                    --quiet \\
                    --view \\
                    '{query}' \\
                    {view_name}
            """.format(project_id=project_id,
                       query=query,
                       view_name=view_name)
        LOG.info('Updating VIEW {}.{}'.format(project_id, view_name))
        cmd_line = CommandLine(cmd=cmd,
                               capture_output=False)
        cmd_line.run()

    def query(self,
              query: str,
              max_rows: str):
        cmd = """bq query \\
                --use_legacy_sql=false \\
                --max_rows={max_rows} \
                '{query}' """.format(query=query,
                                     max_rows=max_rows)
        cmd_line = CommandLine(cmd=cmd,
                               capture_output=True)
        response = cmd_line.run()
        return  str(response.stdout, 'utf-8')

    def query_client(self,
                     query: str) -> pd.DataFrame:
        client = bigquery.Client(project=self.project_id)
        response = client.query(query)
        return response.to_dataframe()

    @property
    def project_id(self):
        return self._project_id
