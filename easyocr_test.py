import easyocr

image = 'path'
reader = easyocr.Reader(['ch_sim','en']) # 只需要运行一次就可以将模型加载到内存中
result = reader.readtext(image)
result


'''
https://github.com/JaidedAI/EasyOCR
'''