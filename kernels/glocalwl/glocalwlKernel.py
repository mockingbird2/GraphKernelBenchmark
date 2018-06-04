import subprocess
import os
import numpy as np
from .. import kernel
from scipy import sparse as sps


class GlocalWLKernel(kernel.Kernel):

    #1: -l to use labels, "-nl" if not
    #2: number of iterations
    #3: -i to use iso type
    #parameter_combinations = [["-l", "1", "-i"],["-l", "2", "-i"]]
    #kernel_name = "WL3L", "WL2L", "WL3G", "WL2G", "Graphlet", "ShortestPath", "ColorRefinement"
    #all kernels use first parameter argument #1, WL and CR use #2, WL use #3

    def __init__(self, dataset_name, output_path, dataset_path, parameter_combinations, kernel_name):
        super().__init__(dataset_name, output_path, dataset_path)
        self.parameter_combinations = parameter_combinations
        self.kernel_name = kernel_name

    def compile(self):
        pass
        #p = subprocess.Popen(['sh', 'compile.sh'])
        #p.wait()

    def load_data(self):
        #is being done once kernel computes
        pass

    def compute_kernel_matrices(self):
        output_paths = []
        for para_combination in self.parameter_combinations:
            output_path = os.path.join(self.output_path, "glocalwl_"+self.kernel_name+"_"+para_combination[0]+"_"+para_combination[1]+"_"+para_combination[2])
            output_paths.append(output_path)
            exec_path = os.path.join('kernels','glocalwl','globalwl')
            p = subprocess.Popen([exec_path, self.datasetname, self.kernel_name, para_combination[0], para_combination[1], para_combination[2], output_path])
            p.wait()
        return output_paths