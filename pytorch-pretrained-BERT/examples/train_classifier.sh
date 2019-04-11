#!/usr/bin/env bash

base_path=/home/v-yinguo/Amcute/repos/semEvalTask4
train_file=train.json
test_file=test.json
ans_file=$base_path/test-data/$subtask/relations.txt
predict_file=$base_path/bert_prediction_result/$subtask 

 python3 $base_path/pytorch-pretrained-BERT/examples/run_classifier.py \
--data_dir $base_path/bert_data/\
--output_dir $base_path/bert_prediction_result/model \
--task_name mnli \
--do_train \
--do_eval \
--bert_model bert-base-uncased \
--verbose_logging \
--num_train_epochs 30 \
--train_batch_size 128 \
--gradient_accumulation_steps 32 \
--do_lower_case \
> $predict_file


