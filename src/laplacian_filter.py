import cv2
import numpy as np
from matplotlib import pyplot as plt


def set_kernel(type_temp):
    laplacian_kernel = 0
    if type_temp == 3:
        laplacian_kernel = np.array([[1, 1, 1],
                                     [1, -8, 1],
                                     [1, 1, 1]])
    elif type_temp == 5:
        laplacian_kernel = np.array([[-1, -1, -1, -1, -1],
                                     [-1, -1, -1, -1, -1],
                                     [-1, -1, 24, -1, -1],
                                     [-1, -1, -1, -1, -1],
                                     [-1, -1, -1, -1, -1]])
    return laplacian_kernel


def get_laplacian_filter(image, matrix_type):
    borders = int(matrix_type / 2)
    laplacian_kernel = set_kernel(matrix_type)
    laplacian_image = np.zeros(image.shape, dtype=np.int16)
    for i in range(borders, image.shape[0] - borders):
        for j in range(borders, image.shape[1] - borders):
            kernel = image[i - borders:i + borders + 1, j - borders:j + borders + 1] * laplacian_kernel
            laplacian_image[i, j] = np.sum(kernel)
    return laplacian_image


if __name__ == '__main__':
    img = cv2.imread('../samples/lena.jpg')
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    images = []
    images.append(gray_img)

    laplacian_filter_3x3 = get_laplacian_filter(gray_img, 3)
    images.append(laplacian_filter_3x3)

    laplacian_filter_5x5 = get_laplacian_filter(gray_img, 5)
    images.append(laplacian_filter_5x5)

    fig = plt.figure(0)
    titles = ['Gray Image', '3x3 mask', '5x5 mask']
    for x in range(len(images)):
        plt.subplot(1, 3, x + 1), plt.imshow(images[x], 'gray')
        plt.title(titles[x])
        plt.axis('off')
        cv2.imwrite("../results/laplacian_filter_image_mask_{}.jpg".format(int(x + 1)), images[x])

    fig.savefig("../results/laplacian_filter_figure.jpg")
    plt.show()
    plt.close()
