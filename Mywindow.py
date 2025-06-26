from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect, Slot, Signal, QModelIndex,
    QSize, QTime, QUrl)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon, QResizeEvent,
    QImage, QKeySequence, QLinearGradient, QStandardItemModel, QStandardItem,
    QPalette, QPixmap, QRadialGradient, QTransform, Qt)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTextBrowser, QVBoxLayout,
    QWidget, QFileDialog)
from ui_window import Ui_MainWindow
from TLabel import TLabel
import pandas
import cv2
import os
import numpy as np
import multiprocessing as mp
import threading


class Mywindow(QMainWindow):
    pd_label_color = pandas.read_csv('./class_dict.csv', sep=',')  # CSV路径
    name_value = pd_label_color['name'].values
    num_class = len(name_value)
    colormap = []
    for i in range(len(pd_label_color.index)):
        tmp = pd_label_color.iloc[i]  # 通过行号索引行数据
        color = []
        color.append(tmp['r'])
        color.append(tmp['g'])
        color.append(tmp['b'])
        colormap.append(color)
    cm = np.array(colormap).astype('uint8')

    def __init__(self):
        super().__init__()
        self.mat = np.zeros((576, 832))  # 初始化一个矩阵，用来存放模型识别后最大值的索引
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.labels = (TLabel(), TLabel())
        self.ui.verticalLayout_2.insertWidget(1, self.labels[0])
        self.ui.verticalLayout_2.addWidget(self.labels[1])
        self.__path: str  # 文件路径
        self.folder_path: str  # 文件夹路径
        self.folderSavePath = './output'  # 批处理后图片保存路径,默认程序当前目录
        self.originalImage = QPixmap("original.png")
        self.resultImage = QPixmap("result.png")
        self.labels[0].setPixmap(self.originalImage)
        self.labels[1].setPixmap(self.resultImage)
        info = ["File: ", "78-60煤岩镜质体占比: ", "78-64煤岩镜质体占比: ", "78-67煤岩镜质体占比: ", "78-70煤岩镜质体占比: ", "78-72煤岩镜质体占比: ",
                "78-106煤岩镜质体占比: ", "78-107煤岩镜质体占比: ", "78-108煤岩镜质体占比: ", "78-111煤岩镜质体占比: ", "78-143煤岩镜质体占比: ", 
                "78-153煤岩镜质体占比: ", "78-227煤岩镜质体占比: ", "78-231煤岩镜质体占比: ", "78-251煤岩镜质体占比: ", "78-1116煤岩镜质体占比: ", "杂质占比: "]
        self.__model = QStandardItemModel()
        self.__model.appendColumn([QStandardItem(txt) for txt in info])
        self.__model.appendColumn([QStandardItem() for _ in range(17)])
        self.ui.tableView.setModel(self.__model)
        self.ui.tableView.setColumnWidth(0, 186)
        self.ui.tableView.setColumnWidth(1, 80)

    @staticmethod
    def coal_onnx_demo(path):
        print(path)
        img = cv2.imread(path)
        net = cv2.dnn.readNetFromONNX("./coal_semantic.onnx")  # 导入模型
        blob = cv2.dnn.blobFromImage(img, 0.00392, (832, 576), (0, 0, 0))  # 归一化到0到1之间之间
        blob[:, 0, :, :] = (blob[:, 0, :, :] - 0.458) / 0.229
        blob[:, 1, :, :] = (blob[:, 1, :, :] - 0.456) / 0.224
        blob[:, 2, :, :] = (blob[:, 2, :, :] - 0.406) / 0.225
        net.setInput(blob)  # 将预处理之后的数组输入模型
        out = net.forward()  # 得到模型输出
        out = (out - np.min(out)) / (np.max(out) - np.min(out))
        #print(np.min(out))
        pre_label = np.argmax(out, axis=1)  # 获得最大值对应的索引
        pre_label_value = np.max(out, axis=1)  # 获得最大值
        pre_label = np.squeeze(pre_label)  # 降维
        pre_label_value = np.squeeze(pre_label_value)  # 降维
        pre = Mywindow.cm[pre_label]  # 三通道顺序为RGB
        # pre1 = Image.fromarray(pre)
        return pre_label

    #  计算图片中镜质体所占的比例
    @staticmethod
    def cal_pro(mat) -> list:
        ans = [0] * 16
        for row in mat:
            for i in row:
                ans[i] = ans[i] + 1
        return ans

    @Slot()
    def detect_single(self) -> None:
        dialog = QFileDialog()
        dialog.setModal(True)
        self.__path = dialog.getOpenFileName()
        if self.__model.columnCount() > 2:
            self.__model.removeColumns(2, self.__model.columnCount() - 2)
        if len(self.__path[0]) > 0:
            self.labels[0].setPixmap(self.__path[0])
            self.mat = self.coal_onnx_demo(self.__path[0])
            ans = Mywindow.cal_pro(self.mat)
            ans[0], ans[-1] = ans[-1], ans[-1]
            self.__model.setData(self.__model.index(0,1), os.path.split(self.__path[0])[1])
            for i in range(1, 17):
                self.__model.setData(self.__model.index(i,1), f"{ans[i - 1] / 479232:.2%}")
            img = Mywindow.cm[self.mat]
            self.resultImage = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
            self.labels[1].setPixmap(QImage(self.resultImage.data, self.resultImage.shape[1], self.resultImage.shape[0], QImage.Format.Format_BGR888))
            
    @Slot()
    def result_save(self) -> None:
        dialog4 = QFileDialog()
        dialog4.setModal(True)
        single_path = dialog4.getExistingDirectory()
        if len(single_path) > 0:
            self.__model.clear()
            self.__model.setRowCount(30)
            self.__model.setColumnCount(30)
            cv2.imwrite(single_path + '/' + os.path.splitext(os.path.split(self.__path[0])[1])[0] + "_result.png", self.resultImage)
            self.__model.setData(self.__model.index(0, 0), "检测后的图片已经保存")
            self.ui.tableView.setColumnWidth(0, 586)

    @Slot()
    def detect_folder(self) -> None:
        global pre_image
        dialog2 = QFileDialog()
        dialog2.setModal(True)
        self.__path = dialog2.getExistingDirectory()
        if len(self.__path) > 0:
            pre_image = [file for file in os.listdir(self.__path) if os.path.splitext(file)[1] in (".png", ".jpg")]  # 返回指定路径下所有图片的名字，并存放于一个列表中
            t = threading.Thread(target=self.__detect_subfunc_1, args=(self.__path, pre_image, self.folderSavePath))
            t.start()
            # for image in pre_image:
            #     mat_folder = Mywindow.coal_onnx_demo(self.folder_path + '/' + image)
            #     img_folder = Mywindow.cm[mat_folder]
            #     img_folder = cv2.cvtColor(img_folder, cv2.COLOR_RGB2BGR)
            #     cv2.imwrite(self.folderSavePath + '/' + os.path.splitext(image)[0] + "_result.png", img_folder)
        self.labels[0].clear()
        self.labels[1].clear()
        self.__model.clear()
        self.__model.setRowCount(30)
        self.__model.setColumnCount(30)
        self.__model.setData(self.__model.index(0, 0), "共"+str(len(pre_image))+"张图片待处理，请等待")
        self.__model.setData(self.__model.index(1, 0), "检测后的图片保存的路径为：")
        self.__model.setData(self.__model.index(2, 0), str(self.folderSavePath))
        self.ui.tableView.setColumnWidth(0, 586)
    @staticmethod
    def detect_subfunc_0(folder_path:str, images:list, save_path:str):
        ans = list()
        for image in images:
            mat = Mywindow.coal_onnx_demo(folder_path + '/' + image)
            img = Mywindow.cm[mat]
            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
            cv2.imwrite(save_path + '/' + os.path.splitext(image)[0] + "_result.png", img)
            temp = Mywindow.cal_pro(mat)
            temp[0], temp[-1] = temp[-1], temp[0]
            temp.append(image)
            ans.append(temp)
        return ans
    
    def __detect_subfunc_1(self, folder_path:str, images:list, save_path:str) -> None:
        step: int = len(images) // mp.cpu_count()  # 获取步长
        pool = mp.Pool(mp.cpu_count())  # 创建进程池
        results = list()  # 存放进程的返回值
        # 分配任务，创建进程
        for i in range(mp.cpu_count() - 1):
            results.append(pool.apply_async(func=Mywindow.detect_subfunc_0, args=(folder_path, images[step *i: step + step * i], save_path)))
        results.append(pool.apply_async(func=Mywindow.detect_subfunc_0, args=(folder_path, images[mp.cpu_count()*step-step :], save_path)))
        pool.close()
        pool.join()

        self.__model.removeColumns(1, self.__model.columnCount() - 1)
        for result in results:
            temps:list = result.get()
            for temp in temps:
                if len(temp) == 0:
                    continue
                self.__model.appendColumn([QStandardItem() for _ in range(17)])
                index:int = self.__model.columnCount() - 1
                self.ui.tableView.setColumnWidth(index, 80)
                self.__model.setData(self.__model.index(0, index), temp.pop())
                for i in range(1, 17):
                    self.__model.setData(self.__model.index(i, index), f"{temp[i - 1] / 479232:.2%}")


    @Slot()
    def modify_path(self) -> None:
        dialog3 = QFileDialog()
        dialog3.setModal(True)
        self.folderSavePath = dialog3.getExistingDirectory()

    @Slot()
    def show_result(self, index:QModelIndex):
        if index.column() == 0:
            return
        file = str(self.__model.index(0, index.column()).data())
        self.labels[0].setPixmap(self.__path + '/' + file)
        self.labels[1].setPixmap(self.folderSavePath + '/' + os.path.splitext(file)[0] + "_result.png")