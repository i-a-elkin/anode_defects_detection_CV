def compression(array, coef):

    new_list = [0] * (array.shape[1] // coef)
    for i in range(array.shape[0] // coef):
        new_list[i] = []
        for j in range(array.shape[1] // coef):
            compression = round(array[i*coef:i*coef+coef, j*coef:j*coef+coef].mean())
            new_list[i].append(int(compression))
    return np.array(new_list)