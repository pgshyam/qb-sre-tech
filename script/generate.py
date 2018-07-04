import string
import random
import argparse
import sys
from os import path

class Generate:
  dirpath = None
  filename_prefix = None

  #compose filename
  @classmethod
  def filename(self, index): 
    return "{}/{}_{}.txt".format(Generate.dirpath, Generate.filename_prefix, str(index))

  #generates a random size random string of printable chars
  @staticmethod
  def str_generator(max_strlen=65):
    return "".join(random.choice(string.printable) for _ in range(random.randint(1,max_strlen)))

  #appends content from src_index file to file handler, dest_fh as many number of times as in times value
  @classmethod
  def add_content(self, src_index, dest_fh, times=1):
    for _ in range(times):
      with open(Generate.filename(src_index), "r") as fh:
        for line in fh:
          dest_fh.write(line)
  '''
  writes content from multiple files prior to file_index to a file_index file. 
  cIndex is the file_index of the file which has content of all earlier files prior to it
  '''
  @classmethod
  def concat_content(self, file_index, cindex=7):
    
    with open(Generate.filename(file_index), "w") as fmain:
      '''
      optimization: since cIndex file is the last file which is aggregate of all the content from 
      its previous index files, write content of the cIndex file twice and concatenate the content
      from the rest of index files

      for example :
        content for 7th index file = content of [1..6] index files
        content for 14th index file = content of [1..6] + [7] + [8..13]  index files
                                    =  [ content for 7th index file ] * 2 +  content of [8..13] index files
      '''
      if file_index > cindex:
        Generate.add_content(file_index-cindex, fmain, 2)
      for i in xrange(file_index-cindex+1,file_index):
        Generate.add_content(i, fmain, 1)

  @classmethod
  def generate(self, max_file_count, file_5_addition):
    for i in xrange(1, max_file_count+1):
      with open(Generate.filename(i), "w") as fh:
        if i%7 == 0 :
          #concatenate content from previous index files
          Generate.concat_content(i)
        else:
          #write the generated content
          fh.write(Generate.str_generator())
          if i%5 == 0:
            #add additional special content
            fh.write(file_5_addition)

def main():
    parser = argparse.ArgumentParser(description = 'Generate Files')
    parser.add_argument('-d', default="/tmp/data", action="store", help='directory path that hosts generated files')
    parser.add_argument('-f', default="file", action="store", help='prefix of the filename of generated file')
    parser.add_argument('-n', default=100, action="store", help='number of files to generate')
    args = parser.parse_args()

    if not path.isdir(args.d):
      sys.exit("ERROR: directory,{} does not exist.".format(args.d))

    Generate.dirpath = args.d
    Generate.filename_prefix = args.f
    file_5_addition = "This is every 5th file!"

    Generate.generate(int(args.n), file_5_addition)

if __name__ == "__main__":
    main()  