You can reproduce the results in the paper by running the following.
```bash
# do not involve $\gamma$
MODEL=facebook/opt-2.7b TASK=SST2 MODE=ft LR=1e-6 EPS=1e-3 STEPS=4000 bash dizo.sh
# use zo for $\gamma$ searching
MODEL=facebook/opt-2.7b TASK=SST2 MODE=ft LR=1e-6 EPS=1e-3 STEPS=4000 ENHANCED=zo bash dizo.sh
# use fo for $\gamma$ searching
MODEL=facebook/opt-2.7b TASK=SST2 MODE=ft LR=1e-6 EPS=1e-3 STEPS=4000 ENHANCED=fo bash dizo.sh
```
