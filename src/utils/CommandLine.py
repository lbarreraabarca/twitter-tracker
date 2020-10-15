import subprocess
from src.utils.logger import logging

LOG = logging.getLogger(__name__)

class CommandLine():
    def __init__(self,
                 cmd: str,
                 capture_output: bool):
        self._cmd = cmd
        self._capture_output = capture_output

    def run(self):
        return subprocess.run(self.cmd,
                              shell=True,
                              check=True,
                              capture_output=self.capture_output)

    @property
    def cmd(self):
        return self._cmd

    @property
    def capture_output(self):
        return self._capture_output
