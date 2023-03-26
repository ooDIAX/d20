from PIL import Image
import os
import time
import multiprocessing

def chunk_proc(dir):

    pool = multiprocessing.Pool(4)
    pool.starmap(compress_ind, [(k*4, (k+1)*4, dir) for k in range(4)])

    return 


def compress(image_file, i, dir):
    
    filepath = os.path.join(os.getcwd(), image_file)

    image = Image.open(filepath)
    x, y = image.size
    image = image.resize((x//10, y//10))
    image.save(f"{dir}/{i}.jpg", 
                 optimize = True, 
                 quality = 10)
    

    return

def compress_ind(l, r, dir):
    for i in range(l,r):
            compress(f"images/{i}.jpg", i, dir)

if __name__ == "__main__":
    start = time.time()
    compress_ind(0,20,"notmultiprocess")
    end = time.time()
    print("NOT multiprocess: ", end-start)

    start = time.time()
    chunk_proc("multiprocess")
    end = time.time()
    print("multiprocess: ", end-start)

    

    