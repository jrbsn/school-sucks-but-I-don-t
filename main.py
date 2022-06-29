import numpy as np
import math

cD = 0.53 #axial drag coefficient
cSF = -6.0 #side force coefficient with side slip angle
cL = 6.3 #lift coefficient with angle of attack
mR_damping = -6.6 #roll moment coefficient with roll rate (damping)
mP = -5.6 #pitch moment coefficient with angle of attack
mP_damping = -250 #pitch moment coefficient with pitch rate (damping)
mY = 5.6 #yaw moment coefficient with side slip angle
mY_damping = -250 #yaw moment coefficient with yaw rate (damping)

def sin(angle):
    angle = math.radians(angle)
    angle = math.sin(angle)
    return math.degrees(angle)
def cos(angle):
    angle = math.radians(angle)
    angle = math.cos(angle)
    return math.degrees(angle)
def tan(angle):
    angle = math.radians(angle)
    angle = math.tan(angle)
    return math.degrees(angle)

def find_t_roll(roll):
    t_roll = np.array([
        [1, 0, 0],
        [0, cos(roll), sin(roll)],
        [0, (-1 * sin(roll)), cos(roll)]
    ])
def find_t_pitch(pitch):
    t_pitch = np.array([
        [cos(pitch), 0, (-1 * sin(pitch))],
        [0, 1, 0],
        [sin(pitch), 0, cos(pitch)]
    ])
    return t_pitch
def find_t_yaw(yaw):
    t_yaw = np.array([
        [cos(yaw), sin(yaw), 0],
        [(-1 * sin(yaw)), cos(yaw), 0],
        [0, 0, 1]
    ])
    return t_yaw

def find_cBLL(roll, pitch, yaw):
    t_roll = find_t_roll(roll)
    t_pitch = find_t_pitch(pitch)
    t_yaw = find_t_yaw(yaw)

    cBLL = np.matmul(t_roll, t_pitch)
    return np.matmul(cBLL, t_yaw)
def find_cLLB(roll, pitch, yaw):
    t_roll = find_t_roll(roll).T()
    t_pitch = find_t_pitch(pitch).T()
    t_yaw = find_t_yaw(yaw).T()

    cBLL = np.matmul(t_roll, t_pitch)
    return np.matmul(cBLL, t_yaw)