# import os
# from PIL import Image

# # 假设所有PNG文件都在当前文件夹下
# folder_path = "/data/liuqing/MLDA-Net-repo/data/lite_data/10_03/1"
# for file_name in os.listdir(folder_path):
#     if file_name.endswith(".png"):
#         png_image = Image.open(os.path.join(folder_path, file_name))
#         if png_image.mode == "RGBA":
#             png_image = png_image.convert("RGB")
#         jpg_file_name = file_name[:-4]+".jpg"
#         png_image.save(os.path.join(folder_path, jpg_file_name), "JPEG")

import os
from PIL import Image

# 假设所有JPG文件都在当前文件夹下，这里替换为实际的文件夹路径
folder_path = "/data/liuqing/MLDA-Net-repo/data/2011_10_03/2011_10_03_drive_0027_sync/image_00/data"
for file_name in os.listdir(folder_path):
    if file_name.endswith(".jpg"):
        # 打开JPG图像文件
        jpg_file_path = os.path.join(folder_path, file_name)
        jpg_image = Image.open(os.path.join(folder_path, file_name))
        # 如果图像是RGBA模式（有透明度通道），转换为RGB模式（PNG存储要求）
        if jpg_image.mode == "RGBA":
            jpg_image = jpg_image.convert("RGB")
        # 生成对应的PNG文件名，将.jpg后缀替换为.png
        png_file_name = file_name[:-4] + ".png"
        # 构建PNG文件在原文件夹下的完整保存路径
        png_file_path = os.path.join(folder_path, png_file_name)
        os.remove(jpg_file_path)
        try:
            # 保存为PNG文件，覆盖原位置同名文件（实现转换）
            jpg_image.save(png_file_path, "PNG")
        except Exception as e:
            print(f"转换文件 {os.path.join(folder_path, file_name)} 时出错: {e}")

print("完成！")

# import paddle
# model_params = paddle.load("/data/liuqing/MLDA-Net-repo/data/pretrain_weights/encoder.pdparams")
# for param_name, param_value in model_params.items():
#     print("参数名称:", param_name)
#     print("参数形状:", param_value.shape)

# print("完成！")