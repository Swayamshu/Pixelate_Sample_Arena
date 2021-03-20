import gym
import pix_sample_arena
import time
import pybullet as p
import pybullet_data
import cv2

if __name__=="__main__":
    env = gym.make("pix_sample_arena-v0")
    x=0
    while True:
        p.stepSimulation()
    time.sleep(100)
