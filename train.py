import argparse
from trainer import Trainer

import paddle
gpu_available  = paddle.device.is_compiled_with_cuda()
print("GPU available:", gpu_available)

class TrainOptions:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Monodepthv2 options")

        # PATHS
        self.parser.add_argument("--data_path",
                                 type=str,
                                 help="path to the training data",
                                 default="../data")
        self.parser.add_argument("--log_dir",
                                 type=str,
                                 help="log directory",
                                 default="./log_train_1024_320_res50_2")

        # TRAINING options
        self.parser.add_argument("--split",
                                 type=str,
                                 help="which training split to use",
                                 choices=["eigen_full", "eigen_lite"],
                                 default="eigen_full")
        self.parser.add_argument("--num_layers",
                                 type=int,
                                 help="number of resnet layers",
                                 default=18,
                                 choices=[18, 34, 50, 101, 152])
        self.parser.add_argument("--height",
                                 type=int,
                                 help="input image height",
                                 default=320)
        self.parser.add_argument("--width",
                                 type=int,
                                 help="input image width",
                                 default=1024)
        self.parser.add_argument("--disparity_smoothness",
                                 type=float,
                                 help="disparity smoothness weight",
                                 default=0)
        self.parser.add_argument("--scales",
                                 nargs="+",
                                 type=int,
                                 help="scales used in the losses",
                                 default=[0, 1, 2, 3])
        self.parser.add_argument("--min_depth",
                                 type=float,
                                 help="minimum depth",
                                 default=0.1)
        self.parser.add_argument("--max_depth",
                                 type=float,
                                 help="maximum depth",
                                 default=100.0)
        self.parser.add_argument("--use_stereo",
                                 help="if set, uses stereo pair for training",
                                 type=bool,
                                 default=True)
        self.parser.add_argument("--frame_ids",
                                 nargs="+",
                                 type=int,
                                 help="frames to load",
                                 default=[0, -1, 1])
        # DEPTH HINT options
        self.parser.add_argument("--use_depth_hints",
                                 help="if set, apply depth hints during training",
                                 type=bool,
                                 default=True)
                                 #action="store_true")
        self.parser.add_argument("--depth_hint_path",
                                 help="path to load precomputed depth hints from. If not set will"
                                      "be assumed to be data_path/depth_hints",
                                 type=str,
                                 default="../kitti_data/depth_hints")

        # OPTIMIZATION options
        self.parser.add_argument("--batch_size",
                                 type=int,
                                 help="batch size",
                                 default=1)
        self.parser.add_argument("--learning_rate",
                                 type=float,
                                 help="learning rate",
                                 default=1e-5)
        self.parser.add_argument("--start_epoch",
                                 type=int,
                                 help="number of epochs",
                                 default=0)
        self.parser.add_argument("--num_epochs",
                                 type=int,
                                 help="number of epochs",
                                 default=10)
        self.parser.add_argument("--scheduler_step_size",
                                 type=int,
                                 help="step size of the scheduler",
                                 default=2)

        # ABLATION options
        self.parser.add_argument("--weights_init",
                                 type=str,
                                 help="pretrained or scratch",
                                 default="pretrained")

        # SYSTEM options
        self.parser.add_argument("--num_workers",
                                 type=int,
                                 help="number of dataloader workers",
                                 default=0)

        # LOADING options
        self.parser.add_argument("--load_weights_folder",
                                 type=str,
                                 help="name of model to load")
                                 #default='./weight')
        self.parser.add_argument("--models_to_load",
                                 nargs="+",
                                 type=str,
                                 help="models to load",
                                 default=["encoder", "depth", "pose_encoder", "pose"])

        # LOGGING options
        self.parser.add_argument("--log_frequency",
                                 type=int,
                                 help="number of batches between each tensorboard log",
                                 default=250)
        self.parser.add_argument("--save_frequency",
                                 type=int,
                                 help="number of epochs between each save",
                                 default=1)

    def parse(self):
        self.options = self.parser.parse_args()
        return self.options

if __name__ == "__main__":
    options = TrainOptions()
    opts = options.parse()

    trainer = Trainer(opts)
    trainer.train()