import cv2
import numpy as np
import time

from numpy.lib.stride_tricks import sliding_window_view


def cosine_similarity(x, y):
    numerator = np.einsum('ijk,ijk->ij', x, y)
    denominator = np.linalg.norm(x, axis=-1) * np.linalg.norm(y, axis=-1)
    return numerator / denominator


def window_based_matching(left_img_path, right_img_path, disparity_range, kernel_size=5):
    left = cv2.imread(left_img_path, 0)
    right = cv2.imread(right_img_path, 0)

    left = left.astype(np.float32)
    left_w = sliding_window_view(left, (kernel_size, kernel_size))
    left_w = left_w.reshape(left_w.shape[0], left_w.shape[1], -1)

    right = right.astype(np.float32)
    right_w = sliding_window_view(right, (kernel_size, kernel_size))
    right_w = right_w.reshape(right_w.shape[0], right_w.shape[1], -1)

    height, width = left.shape[:2]
    _, width_w = left_w.shape[:2]

    kernel_half = int((kernel_size - 1) / 2)
    scale = 3

    costs = np.full(
        (height, width, disparity_range), -1, dtype=np.float32)
    for j in range(disparity_range):
        wp = left_w[:, j:width_w]
        wqd = right_w[:, 0:width_w-j]

        costs[kernel_half:height-kernel_half,
              kernel_half+j:width-kernel_half, j] = cosine_similarity(wp, wqd)

    min_cost_indices = np.argmax(costs, axis=2)
    depth = min_cost_indices * scale
    depth = depth.astype(np.uint8)

    cv2.imwrite('Depth_Image_Estimation/win_cs_result.png', depth)
    cv2.imwrite('Depth_Image_Estimation/win_cs_color_result.png',
                cv2.applyColorMap(depth, cv2.COLORMAP_JET))

    return depth


def main():
    left_img_path = 'Depth_Image_Estimation/Aloe/Aloe_left_1.png'
    right_img_path = 'Depth_Image_Estimation/Aloe/Aloe_right_1.png'
    disparity_range = 64
    kernel_size = 5

    _ = window_based_matching(
        left_img_path=left_img_path,
        right_img_path=right_img_path,
        disparity_range=disparity_range,
        kernel_size=kernel_size,
    )


if __name__ == "__main__":
    start_time = time.time()
    main()
    print(f"Runtime: {(time.time()-start_time):.5f}s\n")
