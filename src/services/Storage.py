from src.utils.logger import logging
from src.utils.CommandLine import CommandLine

LOG = logging.getLogger(__name__)

class Storage():
    def __init__(self,
                 bucket_name: str,
                 folder_writer: str):
        self._bucket_name = bucket_name + 'dags/*'
        self._folder_writer = folder_writer

    def copy(self):
        LOG.info('Copy dags from : %s', self.bucket_name)
        cmd = 'gsutil --quiet cp -r ' \
                + self.bucket_name + ' ' \
                + self.folder_writer
        cmd_line = CommandLine(cmd=cmd,
                               capture_output=False)
        cmd_line.run()

    @property
    def bucket_name(self):
        return self._bucket_name

    @property
    def folder_writer(self):
        return self._folder_writer
