Python code to generate 100 files. Each file contains a line between 1 and 65 printable characters selected randomly
Line "This is every 5th file!" appears in every fifth file
Every 7th file contains the concated contents of all the previous files. If it is a common file (every 7th and also the 5th), applies only every 7th file rule.

Assumption:
  /tmp/data directory exists

- generate.py
    - module which hosts Generator class which has 2 class variables, dirpath and filename_prefix
      - functions
        - filename(index)
            generates the filename based of the index and using the class variables
        - str_generator(maxchars)
            generates a string of upto 65 printable random characters using the random module
        - concat_content(index)
            writes the contents of all the files generated prior to it to a file with index
        - generate(max_file_count, file_5_addition)
            main function that generates files and adds content as per the rules.
            max_file_count - number of files to be generated
            file_5_addition - additional text that needs to go into every fifth file

  usage:
    set the dirpath and filename_prefix class variables of Generator class   
    invoke generate(100, "This is every 5th file!") to generate the files

- runner.py
    Test suite for running unit tests
- test_generate.py
    unit tests
    - test_generated_string_is_random
        check if the generated string is random string of printable chars
    - test_generated_string_len_is_valid
        check if the generated string length is within 1 and 65
    - test_generated_only_5th_file_contains_String
        check if only every 5th file has the required string
    - test_generated_7th_file_is_aggregate
        check if the size of 7th file is sum of the sizes of files before it