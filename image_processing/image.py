import cv2
import streamlit as st


def show(img):
    cv2.imshow('openCV', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


img1 = cv2.imread('download.jpg', 1)
img2 = cv2.imread('road.jpg', 1)
img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
img = cv2.add(img1, img2)
show(img)


page_bg_img = '''
<style>
body {
background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)


def welcome():
    st.title("Welcome To The World Of Image Processing")
    ''' Image processing is a method to perform some operations on an image, in order to get an enhanced image or to extract some useful information from it. It is a type of signal processing in which input is an image and output may be image or characteristics/features associated with that image. Nowadays, image processing is among rapidly growing technologies. It forms core research area within engineering and computer science disciplines too.'''
    st.write(
        " READ MORE [link](%s)""https://sisu.ut.ee/imageprocessing/book/1")


# def Merge():
#     st.title("Merging Two Images")
#     img1 = st.file_uploader("Upload Image 1", type=["png", "jpg"])
#     img2 = st.file_uploader("Upload Image 2", type=["png", "jpg"])
#     img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
#     img = cv2.add(img1, img2)
#     st.image(img)


def main():

    selected_box = st.sidebar.selectbox(
        'Choose one of the following',
        ('Welcome', 'Merge', 'Video', 'Face Detection',
         'Feature Detection', 'Object Detection')
    )

    if selected_box == 'Welcome':
        welcome()
    if selected_box == 'Merge':
        Merge()
    if selected_box == 'Video':
        video()
    if selected_box == 'Face Detection':
        face_detection()
    if selected_box == 'Feature Detection':
        feature_detection()
    if selected_box == 'Object Detection':
        object_detection()


if __name__ == "__main__":
    main()
