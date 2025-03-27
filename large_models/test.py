import torch
import matplotlib.pyplot as plt

include_list = ['model.decoder.layers.0.self_attn.k_proj.weight', 'model.decoder.layers.0.self_attn.v_proj.weight', 'model.decoder.layers.0.self_attn.q_proj.weight', 'model.decoder.layers.0.self_attn.out_proj.weight', 'model.decoder.layers.1.self_attn.k_proj.weight', 'model.decoder.layers.1.self_attn.v_proj.weight', 'model.decoder.layers.1.self_attn.q_proj.weight', 'model.decoder.layers.1.self_attn.out_proj.weight', 'model.decoder.layers.2.self_attn.k_proj.weight', 'model.decoder.layers.2.self_attn.v_proj.weight', 'model.decoder.layers.2.self_attn.q_proj.weight', 'model.decoder.layers.2.self_attn.out_proj.weight', 'model.decoder.layers.3.self_attn.k_proj.weight', 'model.decoder.layers.3.self_attn.v_proj.weight', 'model.decoder.layers.3.self_attn.q_proj.weight', 'model.decoder.layers.3.self_attn.out_proj.weight', 'model.decoder.layers.4.self_attn.k_proj.weight', 'model.decoder.layers.4.self_attn.v_proj.weight', 'model.decoder.layers.4.self_attn.q_proj.weight', 'model.decoder.layers.4.self_attn.out_proj.weight', 'model.decoder.layers.5.self_attn.k_proj.weight', 'model.decoder.layers.5.self_attn.v_proj.weight', 'model.decoder.layers.5.self_attn.q_proj.weight', 'model.decoder.layers.5.self_attn.out_proj.weight', 'model.decoder.layers.6.self_attn.k_proj.weight', 'model.decoder.layers.6.self_attn.v_proj.weight', 'model.decoder.layers.6.self_attn.q_proj.weight', 'model.decoder.layers.6.self_attn.out_proj.weight', 'model.decoder.layers.7.self_attn.k_proj.weight', 'model.decoder.layers.7.self_attn.v_proj.weight', 'model.decoder.layers.7.self_attn.q_proj.weight', 'model.decoder.layers.7.self_attn.out_proj.weight', 'model.decoder.layers.8.self_attn.k_proj.weight', 'model.decoder.layers.8.self_attn.v_proj.weight', 'model.decoder.layers.8.self_attn.q_proj.weight', 'model.decoder.layers.8.self_attn.out_proj.weight', 'model.decoder.layers.9.self_attn.k_proj.weight', 'model.decoder.layers.9.self_attn.v_proj.weight', 'model.decoder.layers.9.self_attn.q_proj.weight', 'model.decoder.layers.9.self_attn.out_proj.weight', 'model.decoder.layers.10.self_attn.k_proj.weight', 'model.decoder.layers.10.self_attn.v_proj.weight', 'model.decoder.layers.10.self_attn.q_proj.weight', 'model.decoder.layers.10.self_attn.out_proj.weight', 'model.decoder.layers.11.self_attn.k_proj.weight', 'model.decoder.layers.11.self_attn.v_proj.weight', 'model.decoder.layers.11.self_attn.q_proj.weight', 'model.decoder.layers.11.self_attn.out_proj.weight', 'model.decoder.layers.12.self_attn.k_proj.weight', 'model.decoder.layers.12.self_attn.v_proj.weight', 'model.decoder.layers.12.self_attn.q_proj.weight', 'model.decoder.layers.12.self_attn.out_proj.weight', 'model.decoder.layers.13.self_attn.k_proj.weight', 'model.decoder.layers.13.self_attn.v_proj.weight', 'model.decoder.layers.13.self_attn.q_proj.weight', 'model.decoder.layers.13.self_attn.out_proj.weight', 'model.decoder.layers.14.self_attn.k_proj.weight', 'model.decoder.layers.14.self_attn.v_proj.weight', 'model.decoder.layers.14.self_attn.q_proj.weight', 'model.decoder.layers.14.self_attn.out_proj.weight', 'model.decoder.layers.15.self_attn.k_proj.weight', 'model.decoder.layers.15.self_attn.v_proj.weight', 'model.decoder.layers.15.self_attn.q_proj.weight', 'model.decoder.layers.15.self_attn.out_proj.weight', 'model.decoder.layers.16.self_attn.k_proj.weight', 'model.decoder.layers.16.self_attn.v_proj.weight', 'model.decoder.layers.16.self_attn.q_proj.weight', 'model.decoder.layers.16.self_attn.out_proj.weight', 'model.decoder.layers.17.self_attn.k_proj.weight', 'model.decoder.layers.17.self_attn.v_proj.weight', 'model.decoder.layers.17.self_attn.q_proj.weight', 'model.decoder.layers.17.self_attn.out_proj.weight', 'model.decoder.layers.18.self_attn.k_proj.weight', 'model.decoder.layers.18.self_attn.v_proj.weight', 'model.decoder.layers.18.self_attn.q_proj.weight', 'model.decoder.layers.18.self_attn.out_proj.weight', 'model.decoder.layers.19.self_attn.k_proj.weight', 'model.decoder.layers.19.self_attn.v_proj.weight', 'model.decoder.layers.19.self_attn.q_proj.weight', 'model.decoder.layers.19.self_attn.out_proj.weight', 'model.decoder.layers.20.self_attn.k_proj.weight', 'model.decoder.layers.20.self_attn.v_proj.weight', 'model.decoder.layers.20.self_attn.q_proj.weight', 'model.decoder.layers.20.self_attn.out_proj.weight', 'model.decoder.layers.21.self_attn.k_proj.weight', 'model.decoder.layers.21.self_attn.v_proj.weight', 'model.decoder.layers.21.self_attn.q_proj.weight', 'model.decoder.layers.21.self_attn.out_proj.weight', 'model.decoder.layers.22.self_attn.k_proj.weight', 'model.decoder.layers.22.self_attn.v_proj.weight', 'model.decoder.layers.22.self_attn.q_proj.weight', 'model.decoder.layers.22.self_attn.out_proj.weight', 'model.decoder.layers.23.self_attn.k_proj.weight', 'model.decoder.layers.23.self_attn.v_proj.weight', 'model.decoder.layers.23.self_attn.q_proj.weight', 'model.decoder.layers.23.self_attn.out_proj.weight']
idx = 0
models = [torch.load('model{}.pth'.format(i)) for i in range(10)]
alphas = [torch.load('alpha{}.pth'.format(i)) for i in range(10)]

for i in range(len(models[0].keys())):
    key_i = 'constraints.{}'.format(i)

    values = []
    alpha = []
    for j in range(10):
        values.append(models[j][key_i].item())
    for j in range(1, 10):
        alpha.append(alphas[j][key_i].item())

    plt.plot(values, label='gamma')
    plt.plot(alpha, label='alpha')
    plt.title(include_list[idx])
    idx += 1
    plt.show()

