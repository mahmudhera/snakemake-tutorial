import argparse
from matplotlib import pyplot as plt
import pandas as pd
import math

def parse_args():
    parser = argparse.ArgumentParser(
                    prog = 'plotter',
                    description = 'Plots a kmer spectrum (histogram)',
                    epilog = 'Usage: python plotter.py <k-spectrum-filename> <img-filename>')
    parser.add_argument('input_filename')
    parser.add_argument('output_filename')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_args()
    input_filename = args.input_filename
    output_filename = args.output_filename

    df = pd.read_csv(input_filename, delimiter=' ', header=None)
    df.columns = ['A', 'B']

    plt.plot( df['A'].tolist(), [math.log(c) for c in df['B'].tolist()], marker='s', color='r' )
    plt.xlabel('count')
    plt.ylabel('Log of #kmers with this count')
    plt.savefig(output_filename)
