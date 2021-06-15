import time

from gym_stag_hunt.envs import ClassicStagHunt, MarkovStagHunt
from gym_stag_hunt.envs.staghunt_escalation import EscalationStagHunt
from gym_stag_hunt.envs.staghunt_harvest import HarvestStagHunt

ENVS = {
    'CLASSIC': ClassicStagHunt,
    'MARKOV': MarkovStagHunt,
    'HARVEST': HarvestStagHunt,
    'ESCALATION': EscalationStagHunt
}
ENV = 'ESCALATION'

if __name__ == "__main__":
    env = ENVS[ENV](obs_type='image')

    env.reset()
    for i in range(10000):
        obs, rewards, done, info = env.step([env.action_space.sample(), env.action_space.sample()])
        time.sleep(.6)
        if ENV == 'CLASSIC':
            env.render(rewards=rewards)
        else:
            env.render()
    env.close()
    quit()