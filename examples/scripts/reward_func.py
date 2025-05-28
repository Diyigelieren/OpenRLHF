import torch


def reward_func(queries, prompts, labels):
    # queries is prompts + responses
    # labels is answers

    reward = torch.randn(len(queries))
    print(f"====================<func_rewards>====================")
    print(reward)
    print("reward_size: ", reward.shape)
    print("reward_type: ", type(reward))
    return reward 
