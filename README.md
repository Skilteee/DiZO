Please cd ./large_models first.

## Installation

```
pip install -r requirements.txt
```

## Usage

Use `run.py` for all functions (zero-shot/ICL/fine-tuning/MeZO):

```bash
python run.py {ARGUMENTS}
```

Please read run.py for a complete list of arguments. We introduce some of the most important ones below. 

The first part is also used in [MeZO](https://github.com/princeton-nlp/MeZO).

* ```--num_train``` : Number of training examples. For ICL, this is the number of demonstrations.

* ```--num_dev``` : Number of validation examples.

* ```--num_test``` : Number of testing examples.

* ```--model_name``` : HuggingFace model name or path.

* ```--task_name``` : Task name.

* ```--trainer``` : can be none (zero-shot/ICL), regular (fine-tuning), or zo (MeZO).

* ```--zo_eps``` : ZO hyperparameter epsilon for weight update.

* ```--prefix_tuning``` : use prefix-tuning.

* ```--lora``` : use LoRA.

------------------------------------------------------

The second part is the new introduced arguments in DiZO.

* ```--enhanced ```: wheather involving projection (DiZO) into ZO training, need to set ```--trainer=zo```

* ```--interval```: training step interval to update the projection ($\kappa$).

* ```--zo_eps_projection```: ZO hyperparameter epsilon for projection update.

* ```--step_size_projection```: step size for projection.

* ```--clip_range```: $\tau$ for projection clipping.


We provide example scripts below for reproducing our experiments.

```bash
# do not involve $\gamma$ (original MeZO)
MODEL=facebook/opt-2.7b TASK=SST2 MODE=ft LR=1e-6 EPS=1e-3 STEPS=4000 bash dizo.sh

# use zeroth-order optimization for $\gamma$ projection searching
CUDA_VISIBLE_DEVICES=1 MODEL=facebook/opt-2.7b TASK=SST2 MODE=ft LR=1e-6 EPS=1e-3 STEPS=4000 ENHANCED=zo ZO_EPS_PROJECTION=0.1 STEP_SIZE_PROJECTION=2.0 CLIP_RANGE=0.2 bash dizo.sh

# use first-order optimization for $\gamma$ projection searching
MODEL=facebook/opt-2.7b TASK=SST2 MODE=ft LR=1e-6 EPS=1e-3 STEPS=4000 ENHANCED=fo INTERVAL=50 bash dizo.sh
```

Zeroth-order optimization is sensitive to the choice of hyperparameters. Our recommended newly introduced hyperparameter search range are as follows. Empirically, more aggresive projection is better for smaller model and easier tasks, and vise versa.

| DiZO methods     | Suggested Value         |
|------------------|------------|
| interval   | 50/100/200/400  |
| zo_eps_projection    | 0.1/0.05  |
| step_size_projection             | 2.0/1.0  |
| clip_range             | 0.1/0.2/0.3  |

We have provided two additional log files ([DiZO](https://github.com/Skilteee/DiZO/blob/main/output-DiZO-SST2.log) and [MeZO](https://github.com/Skilteee/DiZO/blob/main/output-MeZO-SST2.log) on SST2) to verify that your code is running correctly. The exact numbers may vary slightly depending on the specific devices.

## How to incorporate MeZO or DiZO

Please refer to ```trainer.py``` for details. The ```_inner_training_loop``` function is edited, please replace the original training loop with MeZO. For DiZO, to see where we edited, search ```DiZO added```.

## Citation

```text
@article{tan2025harmony,
  title={Harmony in divergence: Towards fast, accurate, and memory-efficient zeroth-order llm fine-tuning},
  author={Tan, Qitao and Liu, Jun and Zhan, Zheng and Ding, Caiwei and Wang, Yanzhi and Ma, Xiaolong and Lee, Jaewoo and Lu, Jin and Yuan, Geng},
  journal={arXiv preprint arXiv:2502.03304},
  year={2025}
}
```
