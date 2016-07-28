echo "start at `date`"
wc -l /notebooks/wise_title_desc_bigflow.all.0724.head
/usr/bin/python gen_word2vec.py
echo "end at `date`"
