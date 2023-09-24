import os

if os.path.exists('/content/MellowPyre'):
    os.chdir('/content/MellowPyre')
    commandline_args = "--share --no-half-vae --listen --xformers --enable-insecure-extension-access --gradio-queue --remotemoe"
    os.system(f"COMMANDLINE_ARGS='{commandline_args}' python launch.py")
    
    if os.path.exists('/content/drive'):
        os.makedirs('/content/drive/MyDrive/Colab Notebooks/MellowPyre/Configs/', exist_ok=True)
        os.system("cp -v '/content/MellowPyre/config.json' '/content/drive/MyDrive/Colab Notebooks/MellowPyre/Configs/'")
        os.system("cp -v '/content/MellowPyre/ui-config.json' '/content/drive/MyDrive/Colab Notebooks/MellowPyre/Configs/'")
        os.system("cp -v '/content/MellowPyre/styles.csv' '/content/drive/MyDrive/Colab Notebooks/MellowPyre/Configs/'")
    
    os.chdir('/content/')
else:
    print("Missing MellowPyre, run from step1 to download again.")
