# cloud_computing_mrjob
sandbox for cloud computing map reduce jobs

***Run only mapper in command line***
```
python3 mr_word_count.py -r local < data/pg27827.txt --mapper
```

***Run in command line and output to a file***
```
python3 mr_count_freq_words.py data/pg27827.txt --output-dir=freq_word_count_out --no-output
```

***Run in jupyter with output dir***
```
!python3 ipynb_map_reduce_cc1_top10.py -r local ./data/shortjokes.csv --output-dir=ipynb_map_reduce_cc1_top10_out --no-output
```