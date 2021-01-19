# kitti_leftDisp2rightDisp
in the KITTI dataset, there is left2rightDisparity but no right2leftDisparity

so I calculated right2leftDisparity from left2rightDisparity

you may can calculate from velodyne also. but I'm not sure how to make dense disparity on the vehicle.
probably bilinear interpolation on the object mask


anyway you can get [ground truth right disparity](https://drive.google.com/file/d/1CmL-BymlOT_Z92tbseKBQnZhUG4ZSsSy/view?usp=sharing)
