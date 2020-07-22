print('start to prewiit...')
result = np.ones(img.shape) * 255 # new array for prewiit 
for i in range(1, h-1):
    for j in range(1, w-1):
        ##TODO
        result[i, j] = np.array([G, G, G])
