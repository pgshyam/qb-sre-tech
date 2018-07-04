import string
import random

class Generate:
  dirpath = None
  filename_prefix = None

  @classmethod
  def filename(self, index): 
    return "{}/{}_{}.txt".format(Generate.dirpath, Generate.filename_prefix, str(index))

  @staticmethod
  def str_generator(max_strlen=65):
    return "".join(random.choice(string.printable) for _ in range(random.randint(1,max_strlen)))

  @classmethod
  def concat_content(self, file_index):
    with open(Generate.filename(file_index), "w") as fmain:
      for i in xrange(1,file_index):
        with open(Generate.filename(i), "r") as fh:
          for line in fh:
            fmain.write(line)

  @classmethod
  def generate(self, max_file_count, file_5_addition):
    for i in xrange(1, max_file_count+1):
      with open(Generate.filename(i), "w") as fh:
        if i%7 == 0 :
          Generate.concat_content(i)
        else:
          fh.write(Generate.str_generator())
          if i%5 == 0:
            fh.write(file_5_addition)

def main():
    Generate.dirpath = "/tmp/data"
    Generate.filename_prefix = "file"
    file_5_addition = "This is every 5th file!"

    Generate.generate(100, file_5_addition)

if __name__ == "__main__":
    main()  