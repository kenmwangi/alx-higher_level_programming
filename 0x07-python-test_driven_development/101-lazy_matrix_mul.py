#!/usr/bin/python3
"""Module lazy_matrix_mul
Matrix multiplication using NumPy.
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """ Multiples m_a and m_b to give mat_mul results"""
    return numpy.matmul(m_a, m_b)
