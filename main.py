import os
from src.adapters.FileReader import FileReader
from src.adapters.YamlParser import YamlParser
from src.models.QualityRequest import QualityRequest
from src.services.BigQuery import BigQuery
from src.services.Storage import Storage
from src.services.TwitterSearchAPI import TwitterSearchAPI
from src.utils.logger import logging


if __name__ == '__main__':
    LOG = logging.getLogger(__name__)
    input_file = FileReader().load_file('request.yaml')
    LOG.info("Parsing to Yaml.")
    parsed_request = YamlParser().parse(input_file)
    LOG.info("Generating request Object.")
    request = QualityRequest.from_dict(parsed_request)

    LOG.info('Connect TwitterSearchAPI')
    twitter_api = TwitterSearchAPI(api_key=os.environ.get('TW_API_KEY'),
                                   api_secret=os.environ.get('TW_API_SECRET'))

    twitter_api.connect()
    twitter_api.get_tweets(search_query=request.twitter_query,
                           lang=request.twitter_lang,
                           date=request.twitter_date,
                           max_tweets=1e4,
                           tweets_batch=1e3)
    exit()

    LOG.info('Get DAGs content.')
    view = View(filename='view_list.json')
    dag_reader = DAGReader(folder_reader=request.dags_folder,
                           composer_name=request.read_composer,
                           bucket_name=request.read_bucket_config,
                           project_name=request.read_project_name,
                           bucket_raw_data=request.read_bucket_raw_data,
                           jars_dict=jars_dict,
                           view=view.views_dict)

    LOG.info('Get entities partitions.')
    entity = Entity(project_id=request.read_project_name)
    entity.get_all_entities()

    LOG.info('Get entities columns description.')
    entity.get_all_columns()


    LOG.info('Join source data.')
    json = Json(dag_info=dag_reader.dags_dataframe,
                partition=entity.df_entities,
                columns=entity.df_columns)
    LOG.info('Write JSON file %s', request.file_entity)
    json.dataframe_to_json(filename=request.file_entity)

    big_query = BigQuery(project_id=request.write_project_name)
    table_dag = request.write_dataset + '.' + request.write_view
    big_query.load(table_name=table_dag,
                   file=request.file_entity,
                   schema='schema.json')

    LOG.info('Process ended successfully.')
