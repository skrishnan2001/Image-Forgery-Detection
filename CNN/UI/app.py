import streamlit as st

# File Processing Pkgs
import pandas as pd
from PIL import Image


import os

try:
    os.chdir('./MantraNet')
except:
    pass

import matplotlib.pyplot as plt
import gc
from mantranet import *
from pytorch_lightning import Trainer


@st.cache
def load_image(image_file):
    img = Image.open(image_file)
    return img


def check_forgery(model, img_path='./example.jpg', device=device):

    model.to(device)
    model.eval()

    im = load_image(img_path)
    im = np.array(im)
    original_image = im.copy()

    im = torch.Tensor(im)
    im = im.unsqueeze(0)
    im = im.transpose(2, 3).transpose(1, 2)
    im = im.to(device)

    with torch.no_grad():
        final_output = model(im)

    #st.write('Original image')
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(20, 20))
    ax1.imshow(original_image)
    ax1.set_title('Original image')
    ax1.set_yticklabels([])
    ax1.set_xticklabels([])


    #st.write('Predicted forgery mask')
    ax2.imshow((final_output[0][0]).cpu().detach(), cmap='gray')
    ax2.set_title('Predicted forgery mask')
    ax2.set_yticklabels([])
    ax2.set_xticklabels([])

    #st.write('Suspicious regions detected')
    ax3.imshow((final_output[0][0].cpu().detach().unsqueeze(
        2) > 0.2)*torch.tensor(original_image))
    ax3.set_title('Suspicious regions detected')
    ax3.set_yticklabels([])
    ax3.set_xticklabels([])
    st.pyplot(fig)
    #plt.title('Suspicious regions detected')


def main():
    st.title("Image Forgery Detection")

    menu = ["Home", "CSV"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
        image_file = st.file_uploader(
            "Upload Image", type=['png', 'jpeg', 'jpg'])
        if image_file is not None:

            # To See Details
            # st.write(type(image_file))
            # st.write(dir(image_file))

            file_details = {"Filename": image_file.name,
                            "FileType": image_file.type, "FileSize": image_file.size}
            st.write(file_details)

            img = load_image(image_file)
            # st.image(img)

            # to change if you have a GPU with at least 12Go RAM (it will save you a lot of time !)
            device = 'cpu'
            model = pre_trained_model(
                weight_path='./MantraNetv4.pt', device=device)

            model.eval()

            path = "../Images"
            isExist = os.path.exists(path)
            if not isExist:
                os.makedirs(path)

            img = img.save(f"{path}/{image_file.name}")

            # plt.figure(figsize=(20,20))
            check_forgery(
                model, img_path=f"{path}/{image_file.name}", device=device)

    elif choice == "CSV":
        st.subheader("CSV")
        data_file = st.file_uploader("Upload CSV", type=['csv'])
        if st.button("Process"):
            if data_file is not None:
                file_details = {"Filename": data_file.name,
                                "FileType": data_file.type, "FileSize": data_file.size}
                st.write(file_details)

                df = pd.read_csv(data_file)
                st.dataframe(df)


if __name__ == '__main__':
    main()
