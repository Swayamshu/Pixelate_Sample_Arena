from gym.envs.registration import register

register(
    id='pix_sample_arena-v0',
    entry_point='pix_sample_arena.envs:PixSampleArena',
)
