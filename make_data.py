import numpy as np
import random
from argparse import ArgumentParser
import pdb
def main(num, centers, max_range, std):
    if num % centers != 0:
        raise AssertionError("The number of data points must be divisible by the number of centers")
    data = []
    for i in range(centers):
        loc_x = 2 * max_range * (random.random() - 0.5) # random center location in range [-max_range, max_range]
        loc_y = 2 * max_range * (random.random() - 0.5) # random center location in range [-max_range, max_range]
        std_x = std * random.random() + 1e-4 # random std in range [0, std]
        std_y = std * random.random() + 1e-4 # random std in range [0, std]

        x = np.random.normal(loc = loc_x, scale=std_x, size=int(num/centers))
        x = x.reshape((-1 ,1))
        y = np.random.normal(loc = loc_y, scale=std_y, size=int(num/centers))
        y = y.reshape((-1 ,1))
        points = np.concatenate([x,y], axis=1)
        data.append(points)
    data = np.concatenate(data, axis=0)
    file = open('./tests/data_N_%d_C_%d_R_%d_S_%d.txt' % (num,centers,max_range,std),'w')
    for i in range(data.shape[0]):
        file.write(str(data[i][0]) + ', ' + str(data[i][1]) + '\n')
    file.close()

if __name__ == "__main__":
    # Generate 2D points with multi-modal gaussian distribution
    # Save a txt file to ./tests
    # N denotes Number of data to generate
    # C denotes Number of cluster centers
    # R denotes center range
    # S denotes std range
    parser = ArgumentParser()
    parser.add_argument("--num_data", type=int,dest="num", 
                        default='1e5',
                        help="Number of data to generate")

    parser.add_argument("--num_centers", type=int,dest="centers", 
                        default='5',
                        help="Number of cluster centers")

    parser.add_argument("--max_range", type=int,dest="max_range", 
                        default='5',
                        help="Cluster centers will be randomly located between [-max_range, max_range]")
    
    parser.add_argument("--max_std", type=float,
                        dest="std", default='5' ,
                        help="the std of each cluster will be randomly assigned between 0 and max_std")

    args = parser.parse_args()
    main(**vars(args))
