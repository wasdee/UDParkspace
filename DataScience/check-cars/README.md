#                                                                
# To activate this environment, use
#
#     $ conda activate ud-car
#
# To deactivate an active environment, use
#
#     $ conda deactivate

# WIP, stuck at
```
UDParkspace/DataScience/check-cars on  main [?] via 🐍 v3.10.13 via 🅒 ud-car took 2s 
❯ python -m pip install 'git+https://github.com/facebookresearch/detectron2.git'
Collecting git+https://github.com/facebookresearch/detectron2.git
  Cloning https://github.com/facebookresearch/detectron2.git to /tmp/pip-req-build-206dhf5f
  Running command git clone --filter=blob:none --quiet https://github.com/facebookresearch/detectron2.git /tmp/pip-req-build-206dhf5f
  Resolved https://github.com/facebookresearch/detectron2.git to commit e9f7e2ba15abd7badcb05ef6f5076f06b36a9c5b
  Preparing metadata (setup.py) ... done
Requirement already satisfied: Pillow>=7.1 in /home/nam/.local/share/rtx/installs/python/miniconda3-latest/envs/ud-car/lib/python3.10/site-packages (from detectron2==0.6) (10.0.1)
Collecting matplotlib (from detectron2==0.6)
  Downloading matplotlib-3.8.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (5.8 kB)
Collecting pycocotools>=2.0.2 (from detectron2==0.6)
  Downloading pycocotools-2.0.7-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (1.1 kB)
Requirement already satisfied: termcolor>=1.1 in /home/nam/.local/share/rtx/installs/python/miniconda3-latest/envs/ud-car/lib/python3.10/site-packages (from detectron2==0.6) (2.1.0)
Collecting yacs>=0.1.8 (from detectron2==0.6)
  Downloading yacs-0.1.8-py3-none-any.whl (14 kB)
Collecting tabulate (from detectron2==0.6)
  Using cached tabulate-0.9.0-py3-none-any.whl (35 kB)
Collecting cloudpickle (from detectron2==0.6)
  Downloading cloudpickle-3.0.0-py3-none-any.whl.metadata (7.0 kB)
Collecting tqdm>4.29.0 (from detectron2==0.6)
  Using cached tqdm-4.66.1-py3-none-any.whl.metadata (57 kB)
Requirement already satisfied: tensorboard in /home/nam/.local/share/rtx/installs/python/miniconda3-latest/envs/ud-car/lib/python3.10/site-packages (from detectron2==0.6) (2.11.0)
Collecting fvcore<0.1.6,>=0.1.5 (from detectron2==0.6)
  Downloading fvcore-0.1.5.post20221221.tar.gz (50 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 50.2/50.2 kB 849.2 kB/s eta 0:00:00
  Preparing metadata (setup.py) ... done
Collecting iopath<0.1.10,>=0.1.7 (from detectron2==0.6)
  Downloading iopath-0.1.9-py3-none-any.whl (27 kB)
Collecting omegaconf<2.4,>=2.1 (from detectron2==0.6)
  Downloading omegaconf-2.3.0-py3-none-any.whl (79 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 79.5/79.5 kB 3.6 MB/s eta 0:00:00
Collecting hydra-core>=1.1 (from detectron2==0.6)
  Downloading hydra_core-1.3.2-py3-none-any.whl (154 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 154.5/154.5 kB 6.6 MB/s eta 0:00:00
Collecting black (from detectron2==0.6)
  Using cached black-23.12.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (68 kB)
Requirement already satisfied: packaging in /home/nam/.local/share/rtx/installs/python/miniconda3-latest/envs/ud-car/lib/python3.10/site-packages (from detectron2==0.6) (23.2)
Requirement already satisfied: numpy in /home/nam/.local/share/rtx/installs/python/miniconda3-latest/envs/ud-car/lib/python3.10/site-packages (from fvcore<0.1.6,>=0.1.5->detectron2==0.6) (1.22.3)
Requirement already satisfied: pyyaml>=5.1 in /home/nam/.local/share/rtx/installs/python/miniconda3-latest/envs/ud-car/lib/python3.10/site-packages (from fvcore<0.1.6,>=0.1.5->detectron2==0.6) (6.0.1)
Collecting antlr4-python3-runtime==4.9.* (from hydra-core>=1.1->detectron2==0.6)
  Downloading antlr4-python3-runtime-4.9.3.tar.gz (117 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 117.0/117.0 kB 10.7 MB/s eta 0:00:00
  Preparing metadata (setup.py) ... done
Collecting portalocker (from iopath<0.1.10,>=0.1.7->detectron2==0.6)
  Downloading portalocker-2.8.2-py3-none-any.whl.metadata (8.5 kB)
Collecting contourpy>=1.0.1 (from matplotlib->detectron2==0.6)
  Downloading contourpy-1.2.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (5.8 kB)
Collecting cycler>=0.10 (from matplotlib->detectron2==0.6)
  Downloading cycler-0.12.1-py3-none-any.whl.metadata (3.8 kB)
Collecting fonttools>=4.22.0 (from matplotlib->detectron2==0.6)
  Downloading fonttools-4.47.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (157 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 157.2/157.2 kB 9.6 MB/s eta 0:00:00
Collecting kiwisolver>=1.3.1 (from matplotlib->detectron2==0.6)
  Downloading kiwisolver-1.4.5-cp310-cp310-manylinux_2_12_x86_64.manylinux2010_x86_64.whl.metadata (6.4 kB)
Collecting pyparsing>=2.3.1 (from matplotlib->detectron2==0.6)
  Using cached pyparsing-3.1.1-py3-none-any.whl.metadata (5.1 kB)
Requirement already satisfied: python-dateutil>=2.7 in /home/nam/.local/share/rtx/installs/python/miniconda3-latest/envs/ud-car/lib/python3.10/site-packages (from matplotlib->detectron2==0.6) (2.8.2)
Requirement already satisfied: click>=8.0.0 in /home/nam/.local/share/rtx/installs/python/miniconda3-latest/envs/ud-car/lib/python3.10/site-packages (from black->detectron2==0.6) (8.1.7)
Collecting mypy-extensions>=0.4.3 (from black->detectron2==0.6)
  Using cached mypy_extensions-1.0.0-py3-none-any.whl (4.7 kB)
Collecting pathspec>=0.9.0 (from black->detectron2==0.6)
  Using cached pathspec-0.12.1-py3-none-any.whl.metadata (21 kB)
Requirement already satisfied: platformdirs>=2 in /home/nam/.local/share/rtx/installs/python/miniconda3-latest/envs/ud-car/lib/python3.10/site-packages (from black->detectron2==0.6) (4.1.0)
Requirement already satisfied: tomli>=1.1.0 in /home/nam/.local/share/rtx/installs/python/miniconda3-latest/envs/ud-car/lib/python3.10/site-packages (from black->detectron2==0.6) (2.0.1)
Requirement already satisfied: typing-extensions>=4.0.1 in /home/nam/.local/share/rtx/installs/python/miniconda3-latest/envs/ud-car/lib/python3.10/site-packages (from black->detectron2==0.6) (4.9.0)
Requirement already satisfied: absl-py>=0.4 in /home/nam/.local/share/rtx/installs/python/miniconda3-latest/envs/ud-car/lib/python3.10/site-packages (from tensorboard->detectron2==0.6) (1.4.0)
Requirement already satisfied: grpcio>=1.24.3 in /home/nam/.local/share/rtx/installs/python/miniconda3-latest/envs/ud-car/lib/python3.10/site-packages (from tensorboard->detectron2==0.6) (1.51.1)
Requirement already satisfied: google-auth<3,>=1.6.3 in /home/nam/.local/share/rtx/installs/python/miniconda3-latest/envs/ud-car/lib/python3.10/site-packages (from tensorboard->detectron2==0.6) (2.6.0)
Requirement already satisfied: google-auth-oauthlib<0.5,>=0.4.1 in /home/nam/.local/share/rtx/installs/python/miniconda3-latest/envs/ud-car/lib/python3.10/site-packages (from tensorboard->detectron2==0.6) (0.4.4)
Requirement already satisfied: markdown>=2.6.8 in /home/nam/.local/share/rtx/installs/python/miniconda3-latest/envs/ud-car/lib/python3.10/site-packages (from tensorboard->detectron2==0.6) (3.4.1)
Collecting protobuf<4,>=3.9.2 (from tensorboard->detectron2==0.6)
  Downloading protobuf-3.20.3-cp310-cp310-manylinux_2_12_x86_64.manylinux2010_x86_64.whl (1.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.1/1.1 MB 11.9 MB/s eta 0:00:00
Requirement already satisfied: requests<3,>=2.21.0 in /home/nam/.local/share/rtx/installs/python/miniconda3-latest/envs/ud-car/lib/python3.10/site-packages (from tensorboard->detectron2==0.6) (2.31.0)
Requirement already satisfied: setuptools>=41.0.0 in /home/nam/.local/share/rtx/installs/python/miniconda3-latest/envs/ud-car/lib/python3.10/site-packages (from tensorboard->detectron2==0.6) (68.2.2)
Requirement already satisfied: tensorboard-data-server<0.7.0,>=0.6.0 in /home/nam/.local/share/rtx/installs/python/miniconda3-latest/envs/ud-car/lib/python3.10/site-packages (from tensorboard->detectron2==0.6) (0.6.1)
Requirement already satisfied: tensorboard-plugin-wit>=1.6.0 in /home/nam/.local/share/rtx/installs/python/miniconda3-latest/envs/ud-car/lib/python3.10/site-packages (from tensorboard->detectron2==0.6) (1.8.1)
Requirement already satisfied: werkzeug>=1.0.1 in /home/nam/.local/share/rtx/installs/python/miniconda3-latest/envs/ud-car/lib/python3.10/site-packages (from tensorboard->detectron2==0.6) (2.2.3)
Requirement already satisfied: wheel>=0.26 in /home/nam/.local/share/rtx/installs/python/miniconda3-latest/envs/ud-car/lib/python3.10/site-packages (from tensorboard->detectron2==0.6) (0.41.2)
Requirement already satisfied: cachetools<6.0,>=2.0.0 in /home/nam/.local/share/rtx/installs/python/miniconda3-latest/envs/ud-car/lib/python3.10/site-packages (from google-auth<3,>=1.6.3->tensorboard->detectron2==0.6) (5.3.2)
Requirement already satisfied: pyasn1-modules>=0.2.1 in /home/nam/.local/share/rtx/installs/python/miniconda3-latest/envs/ud-car/lib/python3.10/site-packages (from google-auth<3,>=1.6.3->tensorboard->detectron2==0.6) (0.2.8)
Requirement already satisfied: six>=1.9.0 in /home/nam/.local/share/rtx/installs/python/miniconda3-latest/envs/ud-car/lib/python3.10/site-packages (from google-auth<3,>=1.6.3->tensorboard->detectron2==0.6) (1.16.0)
Requirement already satisfied: rsa<5,>=3.1.4 in /home/nam/.local/share/rtx/installs/python/miniconda3-latest/envs/ud-car/lib/python3.10/site-packages (from google-auth<3,>=1.6.3->tensorboard->detectron2==0.6) (4.7.2)
Requirement already satisfied: requests-oauthlib>=0.7.0 in /home/nam/.local/share/rtx/installs/python/miniconda3-latest/envs/ud-car/lib/python3.10/site-packages (from google-auth-oauthlib<0.5,>=0.4.1->tensorboard->detectron2==0.6) (1.3.0)
Requirement already satisfied: charset-normalizer<4,>=2 in /home/nam/.local/share/rtx/installs/python/miniconda3-latest/envs/ud-car/lib/python3.10/site-packages (from requests<3,>=2.21.0->tensorboard->detectron2==0.6) (3.3.2)
Requirement already satisfied: idna<4,>=2.5 in /home/nam/.local/share/rtx/installs/python/miniconda3-latest/envs/ud-car/lib/python3.10/site-packages (from requests<3,>=2.21.0->tensorboard->detectron2==0.6) (3.6)
Requirement already satisfied: urllib3<3,>=1.21.1 in /home/nam/.local/share/rtx/installs/python/miniconda3-latest/envs/ud-car/lib/python3.10/site-packages (from requests<3,>=2.21.0->tensorboard->detectron2==0.6) (2.1.0)
Requirement already satisfied: certifi>=2017.4.17 in /home/nam/.local/share/rtx/installs/python/miniconda3-latest/envs/ud-car/lib/python3.10/site-packages (from requests<3,>=2.21.0->tensorboard->detectron2==0.6) (2023.11.17)
Requirement already satisfied: MarkupSafe>=2.1.1 in /home/nam/.local/share/rtx/installs/python/miniconda3-latest/envs/ud-car/lib/python3.10/site-packages (from werkzeug>=1.0.1->tensorboard->detectron2==0.6) (2.1.3)
Requirement already satisfied: pyasn1<0.5.0,>=0.4.6 in /home/nam/.local/share/rtx/installs/python/miniconda3-latest/envs/ud-car/lib/python3.10/site-packages (from pyasn1-modules>=0.2.1->google-auth<3,>=1.6.3->tensorboard->detectron2==0.6) (0.4.8)
Requirement already satisfied: oauthlib>=3.0.0 in /home/nam/.local/share/rtx/installs/python/miniconda3-latest/envs/ud-car/lib/python3.10/site-packages (from requests-oauthlib>=0.7.0->google-auth-oauthlib<0.5,>=0.4.1->tensorboard->detectron2==0.6) (3.2.2)
Downloading pycocotools-2.0.7-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (426 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 426.2/426.2 kB 44.2 MB/s eta 0:00:00
Downloading matplotlib-3.8.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (11.6 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 11.6/11.6 MB 67.2 MB/s eta 0:00:00
Using cached tqdm-4.66.1-py3-none-any.whl (78 kB)
Using cached black-23.12.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (1.7 MB)
Downloading cloudpickle-3.0.0-py3-none-any.whl (20 kB)
Downloading contourpy-1.2.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (310 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 310.7/310.7 kB 37.1 MB/s eta 0:00:00
Downloading cycler-0.12.1-py3-none-any.whl (8.3 kB)
Downloading fonttools-4.47.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (4.6 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.6/4.6 MB 71.9 MB/s eta 0:00:00
Downloading kiwisolver-1.4.5-cp310-cp310-manylinux_2_12_x86_64.manylinux2010_x86_64.whl (1.6 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.6/1.6 MB 81.3 MB/s eta 0:00:00
Using cached pathspec-0.12.1-py3-none-any.whl (31 kB)
Using cached pyparsing-3.1.1-py3-none-any.whl (103 kB)
Downloading portalocker-2.8.2-py3-none-any.whl (17 kB)
Building wheels for collected packages: detectron2, fvcore, antlr4-python3-runtime
  Building wheel for detectron2 (setup.py) ... error
  error: subprocess-exited-with-error
  
  × python setup.py bdist_wheel did not run successfully.
  │ exit code: 1
  ╰─> [406 lines of output]
      running bdist_wheel
      running build
      running build_py
      creating build
      creating build/lib.linux-x86_64-cpython-310
      creating build/lib.linux-x86_64-cpython-310/detectron2
      copying detectron2/__init__.py -> build/lib.linux-x86_64-cpython-310/detectron2
      creating build/lib.linux-x86_64-cpython-310/tools
      copying tools/__init__.py -> build/lib.linux-x86_64-cpython-310/tools
      copying tools/analyze_model.py -> build/lib.linux-x86_64-cpython-310/tools
      copying tools/benchmark.py -> build/lib.linux-x86_64-cpython-310/tools
      copying tools/train_net.py -> build/lib.linux-x86_64-cpython-310/tools
      copying tools/lightning_train_net.py -> build/lib.linux-x86_64-cpython-310/tools
      copying tools/convert-torchvision-to-d2.py -> build/lib.linux-x86_64-cpython-310/tools
      copying tools/plain_train_net.py -> build/lib.linux-x86_64-cpython-310/tools
      copying tools/lazyconfig_train_net.py -> build/lib.linux-x86_64-cpython-310/tools
      copying tools/visualize_data.py -> build/lib.linux-x86_64-cpython-310/tools
      copying tools/visualize_json_results.py -> build/lib.linux-x86_64-cpython-310/tools
      creating build/lib.linux-x86_64-cpython-310/detectron2/model_zoo
      copying detectron2/model_zoo/__init__.py -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo
      copying detectron2/model_zoo/model_zoo.py -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo
      creating build/lib.linux-x86_64-cpython-310/detectron2/projects
      copying detectron2/projects/__init__.py -> build/lib.linux-x86_64-cpython-310/detectron2/projects
      creating build/lib.linux-x86_64-cpython-310/detectron2/modeling
      copying detectron2/modeling/__init__.py -> build/lib.linux-x86_64-cpython-310/detectron2/modeling
      copying detectron2/modeling/poolers.py -> build/lib.linux-x86_64-cpython-310/detectron2/modeling
      copying detectron2/modeling/sampling.py -> build/lib.linux-x86_64-cpython-310/detectron2/modeling
      copying detectron2/modeling/mmdet_wrapper.py -> build/lib.linux-x86_64-cpython-310/detectron2/modeling
      copying detectron2/modeling/postprocessing.py -> build/lib.linux-x86_64-cpython-310/detectron2/modeling
      copying detectron2/modeling/box_regression.py -> build/lib.linux-x86_64-cpython-310/detectron2/modeling
      copying detectron2/modeling/test_time_augmentation.py -> build/lib.linux-x86_64-cpython-310/detectron2/modeling
      copying detectron2/modeling/matcher.py -> build/lib.linux-x86_64-cpython-310/detectron2/modeling
      copying detectron2/modeling/anchor_generator.py -> build/lib.linux-x86_64-cpython-310/detectron2/modeling
      creating build/lib.linux-x86_64-cpython-310/detectron2/checkpoint
      copying detectron2/checkpoint/__init__.py -> build/lib.linux-x86_64-cpython-310/detectron2/checkpoint
      copying detectron2/checkpoint/catalog.py -> build/lib.linux-x86_64-cpython-310/detectron2/checkpoint
      copying detectron2/checkpoint/c2_model_loading.py -> build/lib.linux-x86_64-cpython-310/detectron2/checkpoint
      copying detectron2/checkpoint/detection_checkpoint.py -> build/lib.linux-x86_64-cpython-310/detectron2/checkpoint
      creating build/lib.linux-x86_64-cpython-310/detectron2/evaluation
      copying detectron2/evaluation/pascal_voc_evaluation.py -> build/lib.linux-x86_64-cpython-310/detectron2/evaluation
      copying detectron2/evaluation/__init__.py -> build/lib.linux-x86_64-cpython-310/detectron2/evaluation
      copying detectron2/evaluation/lvis_evaluation.py -> build/lib.linux-x86_64-cpython-310/detectron2/evaluation
      copying detectron2/evaluation/evaluator.py -> build/lib.linux-x86_64-cpython-310/detectron2/evaluation
      copying detectron2/evaluation/fast_eval_api.py -> build/lib.linux-x86_64-cpython-310/detectron2/evaluation
      copying detectron2/evaluation/rotated_coco_evaluation.py -> build/lib.linux-x86_64-cpython-310/detectron2/evaluation
      copying detectron2/evaluation/coco_evaluation.py -> build/lib.linux-x86_64-cpython-310/detectron2/evaluation
      copying detectron2/evaluation/cityscapes_evaluation.py -> build/lib.linux-x86_64-cpython-310/detectron2/evaluation
      copying detectron2/evaluation/testing.py -> build/lib.linux-x86_64-cpython-310/detectron2/evaluation
      copying detectron2/evaluation/panoptic_evaluation.py -> build/lib.linux-x86_64-cpython-310/detectron2/evaluation
      copying detectron2/evaluation/sem_seg_evaluation.py -> build/lib.linux-x86_64-cpython-310/detectron2/evaluation
      creating build/lib.linux-x86_64-cpython-310/detectron2/structures
      copying detectron2/structures/__init__.py -> build/lib.linux-x86_64-cpython-310/detectron2/structures
      copying detectron2/structures/boxes.py -> build/lib.linux-x86_64-cpython-310/detectron2/structures
      copying detectron2/structures/masks.py -> build/lib.linux-x86_64-cpython-310/detectron2/structures
      copying detectron2/structures/keypoints.py -> build/lib.linux-x86_64-cpython-310/detectron2/structures
      copying detectron2/structures/image_list.py -> build/lib.linux-x86_64-cpython-310/detectron2/structures
      copying detectron2/structures/instances.py -> build/lib.linux-x86_64-cpython-310/detectron2/structures
      copying detectron2/structures/rotated_boxes.py -> build/lib.linux-x86_64-cpython-310/detectron2/structures
      creating build/lib.linux-x86_64-cpython-310/detectron2/data
      copying detectron2/data/__init__.py -> build/lib.linux-x86_64-cpython-310/detectron2/data
      copying detectron2/data/benchmark.py -> build/lib.linux-x86_64-cpython-310/detectron2/data
      copying detectron2/data/dataset_mapper.py -> build/lib.linux-x86_64-cpython-310/detectron2/data
      copying detectron2/data/detection_utils.py -> build/lib.linux-x86_64-cpython-310/detectron2/data
      copying detectron2/data/catalog.py -> build/lib.linux-x86_64-cpython-310/detectron2/data
      copying detectron2/data/build.py -> build/lib.linux-x86_64-cpython-310/detectron2/data
      copying detectron2/data/common.py -> build/lib.linux-x86_64-cpython-310/detectron2/data
      creating build/lib.linux-x86_64-cpython-310/detectron2/export
      copying detectron2/export/flatten.py -> build/lib.linux-x86_64-cpython-310/detectron2/export
      copying detectron2/export/torchscript.py -> build/lib.linux-x86_64-cpython-310/detectron2/export
      copying detectron2/export/__init__.py -> build/lib.linux-x86_64-cpython-310/detectron2/export
      copying detectron2/export/shared.py -> build/lib.linux-x86_64-cpython-310/detectron2/export
      copying detectron2/export/torchscript_patch.py -> build/lib.linux-x86_64-cpython-310/detectron2/export
      copying detectron2/export/caffe2_modeling.py -> build/lib.linux-x86_64-cpython-310/detectron2/export
      copying detectron2/export/caffe2_inference.py -> build/lib.linux-x86_64-cpython-310/detectron2/export
      copying detectron2/export/c10.py -> build/lib.linux-x86_64-cpython-310/detectron2/export
      copying detectron2/export/caffe2_patch.py -> build/lib.linux-x86_64-cpython-310/detectron2/export
      copying detectron2/export/caffe2_export.py -> build/lib.linux-x86_64-cpython-310/detectron2/export
      copying detectron2/export/api.py -> build/lib.linux-x86_64-cpython-310/detectron2/export
      creating build/lib.linux-x86_64-cpython-310/detectron2/engine
      copying detectron2/engine/__init__.py -> build/lib.linux-x86_64-cpython-310/detectron2/engine
      copying detectron2/engine/launch.py -> build/lib.linux-x86_64-cpython-310/detectron2/engine
      copying detectron2/engine/defaults.py -> build/lib.linux-x86_64-cpython-310/detectron2/engine
      copying detectron2/engine/train_loop.py -> build/lib.linux-x86_64-cpython-310/detectron2/engine
      copying detectron2/engine/hooks.py -> build/lib.linux-x86_64-cpython-310/detectron2/engine
      creating build/lib.linux-x86_64-cpython-310/detectron2/utils
      copying detectron2/utils/comm.py -> build/lib.linux-x86_64-cpython-310/detectron2/utils
      copying detectron2/utils/__init__.py -> build/lib.linux-x86_64-cpython-310/detectron2/utils
      copying detectron2/utils/colormap.py -> build/lib.linux-x86_64-cpython-310/detectron2/utils
      copying detectron2/utils/memory.py -> build/lib.linux-x86_64-cpython-310/detectron2/utils
      copying detectron2/utils/serialize.py -> build/lib.linux-x86_64-cpython-310/detectron2/utils
      copying detectron2/utils/visualizer.py -> build/lib.linux-x86_64-cpython-310/detectron2/utils
      copying detectron2/utils/file_io.py -> build/lib.linux-x86_64-cpython-310/detectron2/utils
      copying detectron2/utils/video_visualizer.py -> build/lib.linux-x86_64-cpython-310/detectron2/utils
      copying detectron2/utils/collect_env.py -> build/lib.linux-x86_64-cpython-310/detectron2/utils
      copying detectron2/utils/events.py -> build/lib.linux-x86_64-cpython-310/detectron2/utils
      copying detectron2/utils/testing.py -> build/lib.linux-x86_64-cpython-310/detectron2/utils
      copying detectron2/utils/analysis.py -> build/lib.linux-x86_64-cpython-310/detectron2/utils
      copying detectron2/utils/env.py -> build/lib.linux-x86_64-cpython-310/detectron2/utils
      copying detectron2/utils/logger.py -> build/lib.linux-x86_64-cpython-310/detectron2/utils
      copying detectron2/utils/develop.py -> build/lib.linux-x86_64-cpython-310/detectron2/utils
      copying detectron2/utils/registry.py -> build/lib.linux-x86_64-cpython-310/detectron2/utils
      copying detectron2/utils/tracing.py -> build/lib.linux-x86_64-cpython-310/detectron2/utils
      creating build/lib.linux-x86_64-cpython-310/detectron2/layers
      copying detectron2/layers/__init__.py -> build/lib.linux-x86_64-cpython-310/detectron2/layers
      copying detectron2/layers/aspp.py -> build/lib.linux-x86_64-cpython-310/detectron2/layers
      copying detectron2/layers/blocks.py -> build/lib.linux-x86_64-cpython-310/detectron2/layers
      copying detectron2/layers/roi_align_rotated.py -> build/lib.linux-x86_64-cpython-310/detectron2/layers
      copying detectron2/layers/mask_ops.py -> build/lib.linux-x86_64-cpython-310/detectron2/layers
      copying detectron2/layers/batch_norm.py -> build/lib.linux-x86_64-cpython-310/detectron2/layers
      copying detectron2/layers/shape_spec.py -> build/lib.linux-x86_64-cpython-310/detectron2/layers
      copying detectron2/layers/losses.py -> build/lib.linux-x86_64-cpython-310/detectron2/layers
      copying detectron2/layers/roi_align.py -> build/lib.linux-x86_64-cpython-310/detectron2/layers
      copying detectron2/layers/nms.py -> build/lib.linux-x86_64-cpython-310/detectron2/layers
      copying detectron2/layers/wrappers.py -> build/lib.linux-x86_64-cpython-310/detectron2/layers
      copying detectron2/layers/deform_conv.py -> build/lib.linux-x86_64-cpython-310/detectron2/layers
      copying detectron2/layers/rotated_boxes.py -> build/lib.linux-x86_64-cpython-310/detectron2/layers
      creating build/lib.linux-x86_64-cpython-310/detectron2/solver
      copying detectron2/solver/__init__.py -> build/lib.linux-x86_64-cpython-310/detectron2/solver
      copying detectron2/solver/lr_scheduler.py -> build/lib.linux-x86_64-cpython-310/detectron2/solver
      copying detectron2/solver/build.py -> build/lib.linux-x86_64-cpython-310/detectron2/solver
      creating build/lib.linux-x86_64-cpython-310/detectron2/config
      copying detectron2/config/__init__.py -> build/lib.linux-x86_64-cpython-310/detectron2/config
      copying detectron2/config/lazy.py -> build/lib.linux-x86_64-cpython-310/detectron2/config
      copying detectron2/config/instantiate.py -> build/lib.linux-x86_64-cpython-310/detectron2/config
      copying detectron2/config/compat.py -> build/lib.linux-x86_64-cpython-310/detectron2/config
      copying detectron2/config/defaults.py -> build/lib.linux-x86_64-cpython-310/detectron2/config
      copying detectron2/config/config.py -> build/lib.linux-x86_64-cpython-310/detectron2/config
      creating build/lib.linux-x86_64-cpython-310/detectron2/tracking
      copying detectron2/tracking/__init__.py -> build/lib.linux-x86_64-cpython-310/detectron2/tracking
      copying detectron2/tracking/iou_weighted_hungarian_bbox_iou_tracker.py -> build/lib.linux-x86_64-cpython-310/detectron2/tracking
      copying detectron2/tracking/hungarian_tracker.py -> build/lib.linux-x86_64-cpython-310/detectron2/tracking
      copying detectron2/tracking/base_tracker.py -> build/lib.linux-x86_64-cpython-310/detectron2/tracking
      copying detectron2/tracking/bbox_iou_tracker.py -> build/lib.linux-x86_64-cpython-310/detectron2/tracking
      copying detectron2/tracking/vanilla_hungarian_bbox_iou_tracker.py -> build/lib.linux-x86_64-cpython-310/detectron2/tracking
      copying detectron2/tracking/utils.py -> build/lib.linux-x86_64-cpython-310/detectron2/tracking
      creating build/lib.linux-x86_64-cpython-310/detectron2/modeling/meta_arch
      copying detectron2/modeling/meta_arch/__init__.py -> build/lib.linux-x86_64-cpython-310/detectron2/modeling/meta_arch
      copying detectron2/modeling/meta_arch/dense_detector.py -> build/lib.linux-x86_64-cpython-310/detectron2/modeling/meta_arch
      copying detectron2/modeling/meta_arch/retinanet.py -> build/lib.linux-x86_64-cpython-310/detectron2/modeling/meta_arch
      copying detectron2/modeling/meta_arch/fcos.py -> build/lib.linux-x86_64-cpython-310/detectron2/modeling/meta_arch
      copying detectron2/modeling/meta_arch/semantic_seg.py -> build/lib.linux-x86_64-cpython-310/detectron2/modeling/meta_arch
      copying detectron2/modeling/meta_arch/panoptic_fpn.py -> build/lib.linux-x86_64-cpython-310/detectron2/modeling/meta_arch
      copying detectron2/modeling/meta_arch/build.py -> build/lib.linux-x86_64-cpython-310/detectron2/modeling/meta_arch
      copying detectron2/modeling/meta_arch/rcnn.py -> build/lib.linux-x86_64-cpython-310/detectron2/modeling/meta_arch
      creating build/lib.linux-x86_64-cpython-310/detectron2/modeling/roi_heads
      copying detectron2/modeling/roi_heads/__init__.py -> build/lib.linux-x86_64-cpython-310/detectron2/modeling/roi_heads
      copying detectron2/modeling/roi_heads/box_head.py -> build/lib.linux-x86_64-cpython-310/detectron2/modeling/roi_heads
      copying detectron2/modeling/roi_heads/rotated_fast_rcnn.py -> build/lib.linux-x86_64-cpython-310/detectron2/modeling/roi_heads
      copying detectron2/modeling/roi_heads/mask_head.py -> build/lib.linux-x86_64-cpython-310/detectron2/modeling/roi_heads
      copying detectron2/modeling/roi_heads/cascade_rcnn.py -> build/lib.linux-x86_64-cpython-310/detectron2/modeling/roi_heads
      copying detectron2/modeling/roi_heads/keypoint_head.py -> build/lib.linux-x86_64-cpython-310/detectron2/modeling/roi_heads
      copying detectron2/modeling/roi_heads/roi_heads.py -> build/lib.linux-x86_64-cpython-310/detectron2/modeling/roi_heads
      copying detectron2/modeling/roi_heads/fast_rcnn.py -> build/lib.linux-x86_64-cpython-310/detectron2/modeling/roi_heads
      creating build/lib.linux-x86_64-cpython-310/detectron2/modeling/backbone
      copying detectron2/modeling/backbone/vit.py -> build/lib.linux-x86_64-cpython-310/detectron2/modeling/backbone
      copying detectron2/modeling/backbone/__init__.py -> build/lib.linux-x86_64-cpython-310/detectron2/modeling/backbone
      copying detectron2/modeling/backbone/backbone.py -> build/lib.linux-x86_64-cpython-310/detectron2/modeling/backbone
      copying detectron2/modeling/backbone/fpn.py -> build/lib.linux-x86_64-cpython-310/detectron2/modeling/backbone
      copying detectron2/modeling/backbone/regnet.py -> build/lib.linux-x86_64-cpython-310/detectron2/modeling/backbone
      copying detectron2/modeling/backbone/swin.py -> build/lib.linux-x86_64-cpython-310/detectron2/modeling/backbone
      copying detectron2/modeling/backbone/utils.py -> build/lib.linux-x86_64-cpython-310/detectron2/modeling/backbone
      copying detectron2/modeling/backbone/mvit.py -> build/lib.linux-x86_64-cpython-310/detectron2/modeling/backbone
      copying detectron2/modeling/backbone/build.py -> build/lib.linux-x86_64-cpython-310/detectron2/modeling/backbone
      copying detectron2/modeling/backbone/resnet.py -> build/lib.linux-x86_64-cpython-310/detectron2/modeling/backbone
      creating build/lib.linux-x86_64-cpython-310/detectron2/modeling/proposal_generator
      copying detectron2/modeling/proposal_generator/__init__.py -> build/lib.linux-x86_64-cpython-310/detectron2/modeling/proposal_generator
      copying detectron2/modeling/proposal_generator/proposal_utils.py -> build/lib.linux-x86_64-cpython-310/detectron2/modeling/proposal_generator
      copying detectron2/modeling/proposal_generator/rrpn.py -> build/lib.linux-x86_64-cpython-310/detectron2/modeling/proposal_generator
      copying detectron2/modeling/proposal_generator/rpn.py -> build/lib.linux-x86_64-cpython-310/detectron2/modeling/proposal_generator
      copying detectron2/modeling/proposal_generator/build.py -> build/lib.linux-x86_64-cpython-310/detectron2/modeling/proposal_generator
      creating build/lib.linux-x86_64-cpython-310/detectron2/data/samplers
      copying detectron2/data/samplers/__init__.py -> build/lib.linux-x86_64-cpython-310/detectron2/data/samplers
      copying detectron2/data/samplers/grouped_batch_sampler.py -> build/lib.linux-x86_64-cpython-310/detectron2/data/samplers
      copying detectron2/data/samplers/distributed_sampler.py -> build/lib.linux-x86_64-cpython-310/detectron2/data/samplers
      creating build/lib.linux-x86_64-cpython-310/detectron2/data/transforms
      copying detectron2/data/transforms/__init__.py -> build/lib.linux-x86_64-cpython-310/detectron2/data/transforms
      copying detectron2/data/transforms/augmentation.py -> build/lib.linux-x86_64-cpython-310/detectron2/data/transforms
      copying detectron2/data/transforms/augmentation_impl.py -> build/lib.linux-x86_64-cpython-310/detectron2/data/transforms
      copying detectron2/data/transforms/transform.py -> build/lib.linux-x86_64-cpython-310/detectron2/data/transforms
      creating build/lib.linux-x86_64-cpython-310/detectron2/data/datasets
      copying detectron2/data/datasets/__init__.py -> build/lib.linux-x86_64-cpython-310/detectron2/data/datasets
      copying detectron2/data/datasets/lvis_v1_category_image_count.py -> build/lib.linux-x86_64-cpython-310/detectron2/data/datasets
      copying detectron2/data/datasets/builtin_meta.py -> build/lib.linux-x86_64-cpython-310/detectron2/data/datasets
      copying detectron2/data/datasets/pascal_voc.py -> build/lib.linux-x86_64-cpython-310/detectron2/data/datasets
      copying detectron2/data/datasets/coco_panoptic.py -> build/lib.linux-x86_64-cpython-310/detectron2/data/datasets
      copying detectron2/data/datasets/lvis_v1_categories.py -> build/lib.linux-x86_64-cpython-310/detectron2/data/datasets
      copying detectron2/data/datasets/register_coco.py -> build/lib.linux-x86_64-cpython-310/detectron2/data/datasets
      copying detectron2/data/datasets/coco.py -> build/lib.linux-x86_64-cpython-310/detectron2/data/datasets
      copying detectron2/data/datasets/cityscapes.py -> build/lib.linux-x86_64-cpython-310/detectron2/data/datasets
      copying detectron2/data/datasets/builtin.py -> build/lib.linux-x86_64-cpython-310/detectron2/data/datasets
      copying detectron2/data/datasets/lvis.py -> build/lib.linux-x86_64-cpython-310/detectron2/data/datasets
      copying detectron2/data/datasets/lvis_v0_5_categories.py -> build/lib.linux-x86_64-cpython-310/detectron2/data/datasets
      copying detectron2/data/datasets/cityscapes_panoptic.py -> build/lib.linux-x86_64-cpython-310/detectron2/data/datasets
      creating build/lib.linux-x86_64-cpython-310/detectron2/projects/point_rend
      copying projects/PointRend/point_rend/point_features.py -> build/lib.linux-x86_64-cpython-310/detectron2/projects/point_rend
      copying projects/PointRend/point_rend/__init__.py -> build/lib.linux-x86_64-cpython-310/detectron2/projects/point_rend
      copying projects/PointRend/point_rend/mask_head.py -> build/lib.linux-x86_64-cpython-310/detectron2/projects/point_rend
      copying projects/PointRend/point_rend/semantic_seg.py -> build/lib.linux-x86_64-cpython-310/detectron2/projects/point_rend
      copying projects/PointRend/point_rend/color_augmentation.py -> build/lib.linux-x86_64-cpython-310/detectron2/projects/point_rend
      copying projects/PointRend/point_rend/point_head.py -> build/lib.linux-x86_64-cpython-310/detectron2/projects/point_rend
      copying projects/PointRend/point_rend/roi_heads.py -> build/lib.linux-x86_64-cpython-310/detectron2/projects/point_rend
      copying projects/PointRend/point_rend/config.py -> build/lib.linux-x86_64-cpython-310/detectron2/projects/point_rend
      creating build/lib.linux-x86_64-cpython-310/detectron2/projects/deeplab
      copying projects/DeepLab/deeplab/__init__.py -> build/lib.linux-x86_64-cpython-310/detectron2/projects/deeplab
      copying projects/DeepLab/deeplab/build_solver.py -> build/lib.linux-x86_64-cpython-310/detectron2/projects/deeplab
      copying projects/DeepLab/deeplab/lr_scheduler.py -> build/lib.linux-x86_64-cpython-310/detectron2/projects/deeplab
      copying projects/DeepLab/deeplab/semantic_seg.py -> build/lib.linux-x86_64-cpython-310/detectron2/projects/deeplab
      copying projects/DeepLab/deeplab/loss.py -> build/lib.linux-x86_64-cpython-310/detectron2/projects/deeplab
      copying projects/DeepLab/deeplab/resnet.py -> build/lib.linux-x86_64-cpython-310/detectron2/projects/deeplab
      copying projects/DeepLab/deeplab/config.py -> build/lib.linux-x86_64-cpython-310/detectron2/projects/deeplab
      creating build/lib.linux-x86_64-cpython-310/detectron2/projects/panoptic_deeplab
      copying projects/Panoptic-DeepLab/panoptic_deeplab/__init__.py -> build/lib.linux-x86_64-cpython-310/detectron2/projects/panoptic_deeplab
      copying projects/Panoptic-DeepLab/panoptic_deeplab/post_processing.py -> build/lib.linux-x86_64-cpython-310/detectron2/projects/panoptic_deeplab
      copying projects/Panoptic-DeepLab/panoptic_deeplab/dataset_mapper.py -> build/lib.linux-x86_64-cpython-310/detectron2/projects/panoptic_deeplab
      copying projects/Panoptic-DeepLab/panoptic_deeplab/panoptic_seg.py -> build/lib.linux-x86_64-cpython-310/detectron2/projects/panoptic_deeplab
      copying projects/Panoptic-DeepLab/panoptic_deeplab/target_generator.py -> build/lib.linux-x86_64-cpython-310/detectron2/projects/panoptic_deeplab
      copying projects/Panoptic-DeepLab/panoptic_deeplab/config.py -> build/lib.linux-x86_64-cpython-310/detectron2/projects/panoptic_deeplab
      creating build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs
      copying detectron2/model_zoo/configs/Base-RCNN-FPN.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs
      copying detectron2/model_zoo/configs/Base-RetinaNet.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs
      copying detectron2/model_zoo/configs/Base-RCNN-DilatedC5.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs
      copying detectron2/model_zoo/configs/Base-RCNN-C4.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs
      creating build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/COCO-InstanceSegmentation
      copying detectron2/model_zoo/configs/COCO-InstanceSegmentation/mask_rcnn_R_50_DC5_3x.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/COCO-InstanceSegmentation
      copying detectron2/model_zoo/configs/COCO-InstanceSegmentation/mask_rcnn_X_101_32x8d_FPN_3x.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/COCO-InstanceSegmentation
      copying detectron2/model_zoo/configs/COCO-InstanceSegmentation/mask_rcnn_R_101_DC5_3x.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/COCO-InstanceSegmentation
      copying detectron2/model_zoo/configs/COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/COCO-InstanceSegmentation
      copying detectron2/model_zoo/configs/COCO-InstanceSegmentation/mask_rcnn_R_101_C4_3x.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/COCO-InstanceSegmentation
      copying detectron2/model_zoo/configs/COCO-InstanceSegmentation/mask_rcnn_R_50_C4_1x.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/COCO-InstanceSegmentation
      copying detectron2/model_zoo/configs/COCO-InstanceSegmentation/mask_rcnn_R_50_C4_3x.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/COCO-InstanceSegmentation
      copying detectron2/model_zoo/configs/COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_1x.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/COCO-InstanceSegmentation
      copying detectron2/model_zoo/configs/COCO-InstanceSegmentation/mask_rcnn_R_50_DC5_1x.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/COCO-InstanceSegmentation
      copying detectron2/model_zoo/configs/COCO-InstanceSegmentation/mask_rcnn_R_101_FPN_3x.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/COCO-InstanceSegmentation
      copying detectron2/model_zoo/configs/COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_1x_giou.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/COCO-InstanceSegmentation
      creating build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/PascalVOC-Detection
      copying detectron2/model_zoo/configs/PascalVOC-Detection/faster_rcnn_R_50_FPN.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/PascalVOC-Detection
      copying detectron2/model_zoo/configs/PascalVOC-Detection/faster_rcnn_R_50_C4.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/PascalVOC-Detection
      creating build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/Detectron1-Comparisons
      copying detectron2/model_zoo/configs/Detectron1-Comparisons/mask_rcnn_R_50_FPN_noaug_1x.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/Detectron1-Comparisons
      copying detectron2/model_zoo/configs/Detectron1-Comparisons/keypoint_rcnn_R_50_FPN_1x.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/Detectron1-Comparisons
      copying detectron2/model_zoo/configs/Detectron1-Comparisons/faster_rcnn_R_50_FPN_noaug_1x.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/Detectron1-Comparisons
      creating build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/quick_schedules
      copying detectron2/model_zoo/configs/quick_schedules/mask_rcnn_R_50_FPN_instant_test.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/quick_schedules
      copying detectron2/model_zoo/configs/quick_schedules/rpn_R_50_FPN_instant_test.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/quick_schedules
      copying detectron2/model_zoo/configs/quick_schedules/mask_rcnn_R_50_C4_instant_test.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/quick_schedules
      copying detectron2/model_zoo/configs/quick_schedules/semantic_R_50_FPN_instant_test.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/quick_schedules
      copying detectron2/model_zoo/configs/quick_schedules/rpn_R_50_FPN_inference_acc_test.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/quick_schedules
      copying detectron2/model_zoo/configs/quick_schedules/semantic_R_50_FPN_training_acc_test.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/quick_schedules
      copying detectron2/model_zoo/configs/quick_schedules/mask_rcnn_R_50_FPN_inference_acc_test.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/quick_schedules
      copying detectron2/model_zoo/configs/quick_schedules/mask_rcnn_R_50_DC5_inference_acc_test.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/quick_schedules
      copying detectron2/model_zoo/configs/quick_schedules/keypoint_rcnn_R_50_FPN_training_acc_test.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/quick_schedules
      copying detectron2/model_zoo/configs/quick_schedules/keypoint_rcnn_R_50_FPN_instant_test.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/quick_schedules
      copying detectron2/model_zoo/configs/quick_schedules/fast_rcnn_R_50_FPN_instant_test.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/quick_schedules
      copying detectron2/model_zoo/configs/quick_schedules/mask_rcnn_R_50_C4_GCV_instant_test.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/quick_schedules
      copying detectron2/model_zoo/configs/quick_schedules/fast_rcnn_R_50_FPN_inference_acc_test.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/quick_schedules
      copying detectron2/model_zoo/configs/quick_schedules/semantic_R_50_FPN_inference_acc_test.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/quick_schedules
      copying detectron2/model_zoo/configs/quick_schedules/retinanet_R_50_FPN_inference_acc_test.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/quick_schedules
      copying detectron2/model_zoo/configs/quick_schedules/cascade_mask_rcnn_R_50_FPN_inference_acc_test.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/quick_schedules
      copying detectron2/model_zoo/configs/quick_schedules/keypoint_rcnn_R_50_FPN_normalized_training_acc_test.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/quick_schedules
      copying detectron2/model_zoo/configs/quick_schedules/panoptic_fpn_R_50_instant_test.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/quick_schedules
      copying detectron2/model_zoo/configs/quick_schedules/cascade_mask_rcnn_R_50_FPN_instant_test.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/quick_schedules
      copying detectron2/model_zoo/configs/quick_schedules/mask_rcnn_R_50_FPN_training_acc_test.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/quick_schedules
      copying detectron2/model_zoo/configs/quick_schedules/mask_rcnn_R_50_C4_training_acc_test.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/quick_schedules
      copying detectron2/model_zoo/configs/quick_schedules/mask_rcnn_R_50_FPN_pred_boxes_training_acc_test.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/quick_schedules
      copying detectron2/model_zoo/configs/quick_schedules/retinanet_R_50_FPN_instant_test.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/quick_schedules
      copying detectron2/model_zoo/configs/quick_schedules/panoptic_fpn_R_50_inference_acc_test.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/quick_schedules
      copying detectron2/model_zoo/configs/quick_schedules/keypoint_rcnn_R_50_FPN_inference_acc_test.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/quick_schedules
      copying detectron2/model_zoo/configs/quick_schedules/mask_rcnn_R_50_C4_inference_acc_test.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/quick_schedules
      copying detectron2/model_zoo/configs/quick_schedules/panoptic_fpn_R_50_training_acc_test.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/quick_schedules
      creating build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/LVISv1-InstanceSegmentation
      copying detectron2/model_zoo/configs/LVISv1-InstanceSegmentation/mask_rcnn_X_101_32x8d_FPN_1x.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/LVISv1-InstanceSegmentation
      copying detectron2/model_zoo/configs/LVISv1-InstanceSegmentation/mask_rcnn_R_50_FPN_1x.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/LVISv1-InstanceSegmentation
      copying detectron2/model_zoo/configs/LVISv1-InstanceSegmentation/mask_rcnn_R_101_FPN_1x.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/LVISv1-InstanceSegmentation
      creating build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/COCO-PanopticSegmentation
      copying detectron2/model_zoo/configs/COCO-PanopticSegmentation/panoptic_fpn_R_101_3x.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/COCO-PanopticSegmentation
      copying detectron2/model_zoo/configs/COCO-PanopticSegmentation/panoptic_fpn_R_50_3x.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/COCO-PanopticSegmentation
      copying detectron2/model_zoo/configs/COCO-PanopticSegmentation/Base-Panoptic-FPN.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/COCO-PanopticSegmentation
      copying detectron2/model_zoo/configs/COCO-PanopticSegmentation/panoptic_fpn_R_50_1x.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/COCO-PanopticSegmentation
      creating build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/LVISv0.5-InstanceSegmentation
      copying detectron2/model_zoo/configs/LVISv0.5-InstanceSegmentation/mask_rcnn_X_101_32x8d_FPN_1x.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/LVISv0.5-InstanceSegmentation
      copying detectron2/model_zoo/configs/LVISv0.5-InstanceSegmentation/mask_rcnn_R_50_FPN_1x.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/LVISv0.5-InstanceSegmentation
      copying detectron2/model_zoo/configs/LVISv0.5-InstanceSegmentation/mask_rcnn_R_101_FPN_1x.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/LVISv0.5-InstanceSegmentation
      creating build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/Cityscapes
      copying detectron2/model_zoo/configs/Cityscapes/mask_rcnn_R_50_FPN.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/Cityscapes
      creating build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/COCO-Keypoints
      copying detectron2/model_zoo/configs/COCO-Keypoints/keypoint_rcnn_X_101_32x8d_FPN_3x.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/COCO-Keypoints
      copying detectron2/model_zoo/configs/COCO-Keypoints/keypoint_rcnn_R_50_FPN_1x.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/COCO-Keypoints
      copying detectron2/model_zoo/configs/COCO-Keypoints/keypoint_rcnn_R_50_FPN_3x.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/COCO-Keypoints
      copying detectron2/model_zoo/configs/COCO-Keypoints/Base-Keypoint-RCNN-FPN.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/COCO-Keypoints
      copying detectron2/model_zoo/configs/COCO-Keypoints/keypoint_rcnn_R_101_FPN_3x.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/COCO-Keypoints
      creating build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/COCO-Detection
      copying detectron2/model_zoo/configs/COCO-Detection/retinanet_R_50_FPN_1x.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/COCO-Detection
      copying detectron2/model_zoo/configs/COCO-Detection/faster_rcnn_R_50_C4_1x.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/COCO-Detection
      copying detectron2/model_zoo/configs/COCO-Detection/faster_rcnn_R_50_FPN_1x.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/COCO-Detection
      copying detectron2/model_zoo/configs/COCO-Detection/faster_rcnn_X_101_32x8d_FPN_3x.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/COCO-Detection
      copying detectron2/model_zoo/configs/COCO-Detection/retinanet_R_101_FPN_3x.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/COCO-Detection
      copying detectron2/model_zoo/configs/COCO-Detection/faster_rcnn_R_50_FPN_3x.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/COCO-Detection
      copying detectron2/model_zoo/configs/COCO-Detection/faster_rcnn_R_50_DC5_3x.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/COCO-Detection
      copying detectron2/model_zoo/configs/COCO-Detection/rpn_R_50_FPN_1x.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/COCO-Detection
      copying detectron2/model_zoo/configs/COCO-Detection/rpn_R_50_C4_1x.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/COCO-Detection
      copying detectron2/model_zoo/configs/COCO-Detection/faster_rcnn_R_50_DC5_1x.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/COCO-Detection
      copying detectron2/model_zoo/configs/COCO-Detection/faster_rcnn_R_101_C4_3x.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/COCO-Detection
      copying detectron2/model_zoo/configs/COCO-Detection/faster_rcnn_R_101_FPN_3x.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/COCO-Detection
      copying detectron2/model_zoo/configs/COCO-Detection/retinanet_R_50_FPN_3x.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/COCO-Detection
      copying detectron2/model_zoo/configs/COCO-Detection/faster_rcnn_R_50_C4_3x.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/COCO-Detection
      copying detectron2/model_zoo/configs/COCO-Detection/fast_rcnn_R_50_FPN_1x.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/COCO-Detection
      copying detectron2/model_zoo/configs/COCO-Detection/faster_rcnn_R_101_DC5_3x.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/COCO-Detection
      creating build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/Misc
      copying detectron2/model_zoo/configs/Misc/scratch_mask_rcnn_R_50_FPN_9x_gn.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/Misc
      copying detectron2/model_zoo/configs/Misc/mask_rcnn_R_50_FPN_3x_dconv_c3-c5.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/Misc
      copying detectron2/model_zoo/configs/Misc/mask_rcnn_R_50_FPN_3x_syncbn.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/Misc
      copying detectron2/model_zoo/configs/Misc/scratch_mask_rcnn_R_50_FPN_3x_gn.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/Misc
      copying detectron2/model_zoo/configs/Misc/mask_rcnn_R_50_FPN_3x_gn.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/Misc
      copying detectron2/model_zoo/configs/Misc/panoptic_fpn_R_101_dconv_cascade_gn_3x.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/Misc
      copying detectron2/model_zoo/configs/Misc/mask_rcnn_R_50_FPN_1x_dconv_c3-c5.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/Misc
      copying detectron2/model_zoo/configs/Misc/mask_rcnn_R_50_FPN_1x_cls_agnostic.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/Misc
      copying detectron2/model_zoo/configs/Misc/scratch_mask_rcnn_R_50_FPN_9x_syncbn.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/Misc
      copying detectron2/model_zoo/configs/Misc/semantic_R_50_FPN_1x.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/Misc
      copying detectron2/model_zoo/configs/Misc/cascade_mask_rcnn_R_50_FPN_1x.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/Misc
      copying detectron2/model_zoo/configs/Misc/cascade_mask_rcnn_R_50_FPN_3x.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/Misc
      copying detectron2/model_zoo/configs/Misc/cascade_mask_rcnn_X_152_32x8d_FPN_IN5k_gn_dconv.yaml -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/Misc
      copying detectron2/model_zoo/configs/COCO-InstanceSegmentation/mask_rcnn_regnetx_4gf_dds_fpn_1x.py -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/COCO-InstanceSegmentation
      copying detectron2/model_zoo/configs/COCO-InstanceSegmentation/mask_rcnn_R_50_C4_1x.py -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/COCO-InstanceSegmentation
      copying detectron2/model_zoo/configs/COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_1x.py -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/COCO-InstanceSegmentation
      copying detectron2/model_zoo/configs/COCO-InstanceSegmentation/mask_rcnn_regnety_4gf_dds_fpn_1x.py -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/COCO-InstanceSegmentation
      creating build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/new_baselines
      copying detectron2/model_zoo/configs/new_baselines/mask_rcnn_R_50_FPN_400ep_LSJ.py -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/new_baselines
      copying detectron2/model_zoo/configs/new_baselines/mask_rcnn_R_50_FPN_200ep_LSJ.py -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/new_baselines
      copying detectron2/model_zoo/configs/new_baselines/mask_rcnn_regnetx_4gf_dds_FPN_200ep_LSJ.py -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/new_baselines
      copying detectron2/model_zoo/configs/new_baselines/mask_rcnn_R_101_FPN_100ep_LSJ.py -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/new_baselines
      copying detectron2/model_zoo/configs/new_baselines/mask_rcnn_R_50_FPN_100ep_LSJ.py -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/new_baselines
      copying detectron2/model_zoo/configs/new_baselines/mask_rcnn_regnety_4gf_dds_FPN_200ep_LSJ.py -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/new_baselines
      copying detectron2/model_zoo/configs/new_baselines/mask_rcnn_regnetx_4gf_dds_FPN_400ep_LSJ.py -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/new_baselines
      copying detectron2/model_zoo/configs/new_baselines/mask_rcnn_regnetx_4gf_dds_FPN_100ep_LSJ.py -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/new_baselines
      copying detectron2/model_zoo/configs/new_baselines/mask_rcnn_regnety_4gf_dds_FPN_100ep_LSJ.py -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/new_baselines
      copying detectron2/model_zoo/configs/new_baselines/mask_rcnn_R_101_FPN_200ep_LSJ.py -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/new_baselines
      copying detectron2/model_zoo/configs/new_baselines/mask_rcnn_R_50_FPN_50ep_LSJ.py -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/new_baselines
      copying detectron2/model_zoo/configs/new_baselines/mask_rcnn_regnety_4gf_dds_FPN_400ep_LSJ.py -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/new_baselines
      copying detectron2/model_zoo/configs/new_baselines/mask_rcnn_R_101_FPN_400ep_LSJ.py -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/new_baselines
      creating build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/common
      copying detectron2/model_zoo/configs/common/train.py -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/common
      copying detectron2/model_zoo/configs/common/optim.py -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/common
      copying detectron2/model_zoo/configs/common/coco_schedule.py -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/common
      creating build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/common/models
      copying detectron2/model_zoo/configs/common/models/cascade_rcnn.py -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/common/models
      copying detectron2/model_zoo/configs/common/models/retinanet.py -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/common/models
      copying detectron2/model_zoo/configs/common/models/mask_rcnn_vitdet.py -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/common/models
      copying detectron2/model_zoo/configs/common/models/mask_rcnn_c4.py -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/common/models
      copying detectron2/model_zoo/configs/common/models/fcos.py -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/common/models
      copying detectron2/model_zoo/configs/common/models/keypoint_rcnn_fpn.py -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/common/models
      copying detectron2/model_zoo/configs/common/models/mask_rcnn_fpn.py -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/common/models
      copying detectron2/model_zoo/configs/common/models/panoptic_fpn.py -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/common/models
      creating build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/common/data
      copying detectron2/model_zoo/configs/common/data/coco_keypoint.py -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/common/data
      copying detectron2/model_zoo/configs/common/data/constants.py -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/common/data
      copying detectron2/model_zoo/configs/common/data/coco_panoptic_separated.py -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/common/data
      copying detectron2/model_zoo/configs/common/data/coco.py -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/common/data
      copying detectron2/model_zoo/configs/COCO-PanopticSegmentation/panoptic_fpn_R_50_1x.py -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/COCO-PanopticSegmentation
      copying detectron2/model_zoo/configs/COCO-Keypoints/keypoint_rcnn_R_50_FPN_1x.py -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/COCO-Keypoints
      copying detectron2/model_zoo/configs/COCO-Detection/fcos_R_50_FPN_1x.py -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/COCO-Detection
      copying detectron2/model_zoo/configs/COCO-Detection/retinanet_R_50_FPN_1x.py -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/COCO-Detection
      copying detectron2/model_zoo/configs/Misc/mmdet_mask_rcnn_R_50_FPN_1x.py -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/Misc
      copying detectron2/model_zoo/configs/Misc/torchvision_imagenet_R_50.py -> build/lib.linux-x86_64-cpython-310/detectron2/model_zoo/configs/Misc
      running build_ext
      Traceback (most recent call last):
        File "<string>", line 2, in <module>
        File "<pip-setuptools-caller>", line 34, in <module>
        File "/tmp/pip-req-build-206dhf5f/setup.py", line 151, in <module>
          setup(
        File "/home/nam/.local/share/rtx/installs/python/miniconda3-latest/envs/ud-car/lib/python3.10/site-packages/setuptools/__init__.py", line 103, in setup
          return distutils.core.setup(**attrs)
        File "/home/nam/.local/share/rtx/installs/python/miniconda3-latest/envs/ud-car/lib/python3.10/site-packages/setuptools/_distutils/core.py", line 185, in setup
          return run_commands(dist)
        File "/home/nam/.local/share/rtx/installs/python/miniconda3-latest/envs/ud-car/lib/python3.10/site-packages/setuptools/_distutils/core.py", line 201, in run_commands
          dist.run_commands()
        File "/home/nam/.local/share/rtx/installs/python/miniconda3-latest/envs/ud-car/lib/python3.10/site-packages/setuptools/_distutils/dist.py", line 969, in run_commands
          self.run_command(cmd)
        File "/home/nam/.local/share/rtx/installs/python/miniconda3-latest/envs/ud-car/lib/python3.10/site-packages/setuptools/dist.py", line 989, in run_command
          super().run_command(command)
        File "/home/nam/.local/share/rtx/installs/python/miniconda3-latest/envs/ud-car/lib/python3.10/site-packages/setuptools/_distutils/dist.py", line 988, in run_command
          cmd_obj.run()
        File "/home/nam/.local/share/rtx/installs/python/miniconda3-latest/envs/ud-car/lib/python3.10/site-packages/wheel/bdist_wheel.py", line 364, in run
          self.run_command("build")
        File "/home/nam/.local/share/rtx/installs/python/miniconda3-latest/envs/ud-car/lib/python3.10/site-packages/setuptools/_distutils/cmd.py", line 318, in run_command
          self.distribution.run_command(command)
        File "/home/nam/.local/share/rtx/installs/python/miniconda3-latest/envs/ud-car/lib/python3.10/site-packages/setuptools/dist.py", line 989, in run_command
          super().run_command(command)
        File "/home/nam/.local/share/rtx/installs/python/miniconda3-latest/envs/ud-car/lib/python3.10/site-packages/setuptools/_distutils/dist.py", line 988, in run_command
          cmd_obj.run()
        File "/home/nam/.local/share/rtx/installs/python/miniconda3-latest/envs/ud-car/lib/python3.10/site-packages/setuptools/_distutils/command/build.py", line 131, in run
          self.run_command(cmd_name)
        File "/home/nam/.local/share/rtx/installs/python/miniconda3-latest/envs/ud-car/lib/python3.10/site-packages/setuptools/_distutils/cmd.py", line 318, in run_command
          self.distribution.run_command(command)
        File "/home/nam/.local/share/rtx/installs/python/miniconda3-latest/envs/ud-car/lib/python3.10/site-packages/setuptools/dist.py", line 989, in run_command
          super().run_command(command)
        File "/home/nam/.local/share/rtx/installs/python/miniconda3-latest/envs/ud-car/lib/python3.10/site-packages/setuptools/_distutils/dist.py", line 988, in run_command
          cmd_obj.run()
        File "/home/nam/.local/share/rtx/installs/python/miniconda3-latest/envs/ud-car/lib/python3.10/site-packages/setuptools/command/build_ext.py", line 88, in run
          _build_ext.run(self)
        File "/home/nam/.local/share/rtx/installs/python/miniconda3-latest/envs/ud-car/lib/python3.10/site-packages/setuptools/_distutils/command/build_ext.py", line 345, in run
          self.build_extensions()
        File "/home/nam/.local/share/rtx/installs/python/miniconda3-latest/envs/ud-car/lib/python3.10/site-packages/torch/utils/cpp_extension.py", line 511, in build_extensions
          compiler_name, compiler_version = self._check_abi()
        File "/home/nam/.local/share/rtx/installs/python/miniconda3-latest/envs/ud-car/lib/python3.10/site-packages/torch/utils/cpp_extension.py", line 894, in _check_abi
          compiler = self.compiler.compiler_cxx[0]
      IndexError: list index out of range
      [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for detectron2
  Running setup.py clean for detectron2
  Building wheel for fvcore (setup.py) ... done
  Created wheel for fvcore: filename=fvcore-0.1.5.post20221221-py3-none-any.whl size=61400 sha256=2a74ecd4977de0c31088ab040b994d42c8814447452884627c00cfa1bf22493e
  Stored in directory: /home/nam/.cache/pip/wheels/01/c0/af/77c1cf53a1be9e42a52b48e5af2169d40ec2e89f7362489dd0
  Building wheel for antlr4-python3-runtime (setup.py) ... done
  Created wheel for antlr4-python3-runtime: filename=antlr4_python3_runtime-4.9.3-py3-none-any.whl size=144554 sha256=575c589e376efa3cdacbd4d6b352107555179984691b785f9bd46032b9d3a671
  Stored in directory: /home/nam/.cache/pip/wheels/12/93/dd/1f6a127edc45659556564c5730f6d4e300888f4bca2d4c5a88
Successfully built fvcore antlr4-python3-runtime
Failed to build detectron2
ERROR: Could not build wheels for detectron2, which is required to install pyproject.toml-based projects
```