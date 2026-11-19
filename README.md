# mlx-uvr-mdx-net

`MLX` 版本的 `UVR5` 人声、伴奏分离工具，将纯净`人声`从各种背景音乐中`分离`出来。

在 `Apple Silicon` 芯片设备上运行（MacBook、Mac mini、iMac）， 

基于 `MLX` 框架， 无需任何 pytorch 及其组件

## Model Download

在 Release 页面， 下载模型文件后保存在 `models` 文件夹下

  * UVR-MDX-NET-Inst_HQ_5.onnx
  
  * UVR-MDX-NET-Inst_HQ_3.onnx


## Usage

1) clone:

```Bash
git clone https://github.com/harryzhu/mlx-uvr-mdx-net.git

cd mlx-uvr-mdx-net

pip install -r requirements.txt

```

2) 将音频源文件放在 `wav/_src` 目录下

3) 在终端中运行：

```Bash
python extract_vocals.py

```

  人声会生成在 `wav/vocal` 目录下

  背景伴奏音乐会生成在 `wav/music` 目录下

## Quality

1) 默认使用快速模式（使用 `models/UVR-MDX-NET-Inst_HQ_5.onnx` 模型）

2) 如果想改用高质量模式（更慢、人声更清晰， 使用 `models/UVR-MDX-NET-Inst_HQ_3.onnx` 模型）
   
   打开 mdxnet/utils.py, 注释掉默认的 predictor:

```Python
   predictor = Predictor(
        model_path=f'{os.path.dirname(__file__)}/../models/UVR-MDX-NET-Inst_HQ_5.onnx',
        dim_f=2560,
        dim_t=8,
        n_fft=6144,
        #denoise=True,
        denoise=False,
        margin=44100,
        chunks=15
    )
```

   将下面注释掉的使用 取消注释即可：

```Python
	# predictor = Predictor(
	#         model_path=f'{os.path.dirname(__file__)}/../models/UVR-MDX-NET-Inst_HQ_3.onnx',
	#         dim_f=3072,
	#         dim_t=8,
	#         n_fft=6144,
	#         denoise=True,
	#         # denoise=False,
	#         margin=44100,
	#         chunks=15
	#     )

```

