import cv2
import matplotlib.pyplot as plt


def readImg(path):
    return cv2.imread(path, cv2.IMREAD_GRAYSCALE)


class CompareImg:
    def __init__(self, path1, images):
        self.img1 = readImg(path1)
        self.images = [readImg(i) for i in images]
        self.result_img = None
        self.percentage = 0

    def compare(self):
        percentage = []
        all_kp = 0
        for i in self.images:
            orb = cv2.ORB_create()
            kp1, des1 = orb.detectAndCompute(self.img1, None)
            kp2, des2 = orb.detectAndCompute(i, None)
            bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
            matches = bf.match(des1, des2)
            matches = sorted(matches, key=lambda x: x.distance)
            self.result_img = cv2.drawMatches(self.img1, kp1, i, kp2, matches[:10], None, flags=2)
            percentage.append(len(kp1))

            all_kp += len(kp1)

        self.percentage = all_kp / percentage.index(percentage.max()) * 100

        return percentage.index(percentage.max())

    def showResults(self):
        if self.result_img is None:
            return None

        plt.imshow(self.result_img)
        plt.show()

    def getPercent(self):
        return self.percentage

