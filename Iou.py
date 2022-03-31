import torch

'''一维'''
def iou_1(set_1, set_2):
    x1, x2 = set_1    #(left,right)
    y1, y2 = set_2    #(left,right)
    low = torch.max(x1, y1)
    high = torch.min(x2, y2)
    if high<low:
        inter = 0
    else:
        inter = high - low
    union = x2 - x1 + y2 - y1 - inter
    iou = inter / union
    return iou
s1 = torch.tensor([1,3])
s2 = torch.tensor([2,4])
iou_line = iou_1(s1, s2)
print(iou_line)

def iou_2(box1, box2):
    '''
    两个框的IOU计算
    box = [top, left, bottom, right]
    '''
    high = torch.min(box1[2], box2[2]) - torch.max(box1[0],box2[0])
    width = torch.min(box1[3], box2[3]) - torch.max(box1[1], box2[1])
    if high < 0 or width < 0:
        inter = 0
    else:
        inter = high * width
    union = (box1[2] - box1[0]) * (box1[3] - box1[1]) + (box2[2] - box2[0]) * (box2[3] - box2[1] ) - inter
    iou = inter / union
    return iou
b1 = torch.tensor([0, 0, 2, 2])
b2 = torch.tensor([1, 1, 3, 3])
iou_box = iou_2(b1, b2)
print(iou_box)


# 中心点和宽高
def iou_3(x, y, w, h, l_x, l_y, l_w, l_h):
    '''
    Args:
      x: net predicted x
      y: net predicted y
      w: net predicted width
      h: net predicted height
      l_x: label x
      l_y: label y
      l_w: label width
      l_h: label height

    Returns:
      IoU
    '''
    x_max = x + w / 2
    x_min = x - w / 2
    y_max = y + h / 2
    y_min = y - h / 2
    l_x_max = l_x + l_w / 2
    l_x_min = l_x - l_w / 2
    l_y_max = l_y + l_h / 2
    l_y_min = l_y - l_h / 2
    inter_width = torch.min(x_max, l_x_max) - torch.max(x_min, l_x_min)
    inter_hight = torch.min(y_max, l_y_max) - torch.max(y_min, l_y_min)
    if inter_hight < 0 or inter_width < 0:
        inter = 0
    else:
        inter = inter_hight * inter_width
    union = w * h + l_w * l_h - inter
    iou = inter / union
    return iou
para = torch.tensor([0, 0, 2, 2, 1, 1, 2, 2])
x, y, w, h, l_x, l_y, l_w, l_h = para
iou = iou_3(x, y, w, h, l_x, l_y, l_w, l_h)
print(iou)