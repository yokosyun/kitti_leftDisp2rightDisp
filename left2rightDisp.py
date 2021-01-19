import torch
import torch.nn as nn

def left2right(disp,ind):
    disp = disp.cpu()
    focal = 7.070493000000e+02
    baseline = 0.54
    eps = 0.00000001
    depth = focal * baseline /(disp+eps)

    

    thresh = torch.nn.Threshold(threshold = -100.0,value= 0.0 , inplace = False)
    thresh_ind = torch.nn.Threshold(threshold = -disp.shape[2],value= 0.0 , inplace = False)    
    depth =thresh(-depth)
    depth = depth*(-1)

    disp_r = torch.zeros([1,disp.shape[1],disp.shape[2]])

    num = "%.6d" %(ind)
    
    filename = str(num)
 
    filename += "_10.png" 

    print(filename)

    print('result/disp_r/'+filename)


    cx= depth.shape[2]/2
    for u in range (depth.shape[2]):
        for v in range (depth.shape[1]):    
            depth_z = depth[:,v,u]
            Y_l = -(u -cx) * depth_z / focal
            Y_r = Y_l + baseline
            x =  -1 * Y_r * focal / (depth_z+eps) + cx
            x = int(x)
            if x >= depth.shape[2] or x <0:
                x = 0
            
            if disp_r[:,v,x] == 0.0:
                disp_r[:,v,x] = disp[:,v,u]
            else:
                if disp[:,v,u] >disp_r[:,v,x]:
                    disp_r[:,v,x] = disp[:,v,u]              

                
    save_image(disp_r/torch.max(disp), 'result/disp_r/tmp.png')
    disp_r = torch.squeeze(disp_r)
    disp_r = disp_r.data.cpu().numpy()
    img = disp_r
    img = (img*256).astype('uint16')
    img = Image.fromarray(img)
    img.save('result/disp_r/'+filename)
