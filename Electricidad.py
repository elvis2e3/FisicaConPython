# -*- coding: utf-8 -*-
class Electricidad():
    def __init__(self):
        global K
        K = 9000000000
    def fuerza(self, q1, q2, d):
        return K * ((q1 * q2) / float(pow(d, 2)))
