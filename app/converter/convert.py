import subprocess


class Converter():
  def __init__(self):
    pass
  

  def convert(self, url, configLoc):
    command_string = f"a2v -u {url} -c {configLoc}"
    process = subprocess.Popen(command_string,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return (stdout, stderr)


