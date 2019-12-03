import subprocess


class Converter():
  def __init__(self):
    pass
  

  def convert(self, url=None, config_location=None, project_id=None, out_dir=None):
    try:
      command_string = f"a2v -u {url} -c {config_location} --id {project_id} -o {out_dir} "
      process = subprocess.Popen(command_string,stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=True)
      stdout, stderr = process.communicate()
      return (stdout, stderr)
    except Exception as e:
      return str(e)

