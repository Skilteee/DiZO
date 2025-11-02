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

* ```--lr_projection```: learning rate for projection.

* ```--clip_range```: $\tau$ for projection clipping.


We provide example scripts below for reproducing our experiments.

```bash
# do not involve $\gamma$ (original MeZO)
MODEL=facebook/opt-2.7b TASK=SST2 MODE=ft LR=1e-6 EPS=1e-3 STEPS=4000 bash dizo.sh
# use zeroth-order optimization for $\gamma$ projection searching
MODEL=facebook/opt-2.7b TASK=SST2 MODE=ft LR=1e-6 EPS=1e-3 STEPS=4000 ENHANCED=zo bash dizo.sh
# use first-order optimization for $\gamma$ projection searching
MODEL=facebook/opt-2.7b TASK=SST2 MODE=ft LR=1e-6 EPS=1e-3 STEPS=4000 ENHANCED=fo bash dizo.sh
```
