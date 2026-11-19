import os 
import soundfile as sf
from .predictor import *


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
def separate_audio(file_path, output_dir):
    #print(ort.get_available_providers())
    if not os.path.isdir(f"{output_dir}/music"):
        os.makedirs(f"{output_dir}/music", exist_ok=True)
    if not os.path.isdir(f"{output_dir}/vocal"):
        os.makedirs(f"{output_dir}/vocal", exist_ok=True)
    vocals, no_vocals, sampling_rate = predictor.predict(file_path)
    filename = os.path.splitext(os.path.split(file_path)[-1])[0]
    f_music = f"{output_dir}/music/{filename}.wav"
    f_vocal = f"{output_dir}/vocal/{filename}.wav"
    sf.write(f_music, no_vocals, sampling_rate)
    sf.write(f_vocal, vocals, sampling_rate)

    return f_music, f_vocal


   