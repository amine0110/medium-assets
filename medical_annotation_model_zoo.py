import streamlit as st

def main():
    st.title("Medical Imaging Annotation Models")

    st.markdown('''
| Model        | N. Training Data | Data Modality | N. Epochs | mAP  (%) | Ckpts | Download Dataset |
|--------------|------------------|-----------|-------|-------|-------|-------|
| Lungs | 400  | CT | 22  | 95 | [Ckpt](https://drive.google.com/file/d/1NirjDsF_QhqfsB2ZtJO8bpH-PQ7YSGnk/view?usp=sharing) | Soon |
| Heart | 400  | CT | 120  | 89 | [Ckpt](https://drive.google.com/file/d/1DPY59bKAFZLvz7B5L00NeYBOJLRt6e7e/view?usp=sharing) | [Available](https://drive.google.com/file/d/1aqRAdbo70gngaQwuVsK9qi3cYjodiKmz/view?usp=sharing) |
| Liver | 400  | CT | 150  | 93 | [Ckpt](https://drive.google.com/file/d/1FOqPd9bIqXRynbDScBSoDFlDFm56SPsM/view?usp=sharing) | [Available](https://drive.google.com/file/d/15G11RYvOXoIF5rm-ya5rC4394-0hVxA6/view?usp=sharing) |
| Spleen | 400  | CT | 120  | 90 | [Ckpt](https://drive.google.com/file/d/1aNDXzbxIRHqMbpEDYa5VaIO4jRWzVg4b/view?usp=sharing) | [Available](https://drive.google.com/file/d/1cuPzACQH4l_VN5NZOyCCy9ElAu4SQ1-Q/view?usp=sharing) |
| Hips | 400  | CT | 145  | 99 | [Ckpt](https://drive.google.com/file/d/13_otIfYXWZWy477qTF2RniLXl1nS1Ui6/view?usp=sharing) | [Left](https://drive.google.com/file/d/1QwiMnlrwieT_Q0aatLb-Mh0wOLsbW4cq/view?usp=sharing), [Right](https://drive.google.com/file/d/1JBm_h6jKUvi0XAnyXusenZriQdG8lHLZ/view?usp=sharing) |
| Spine | 400  | CT | 74  | 92 | [Ckpt](https://drive.google.com/file/d/1YAZ6pAW6Q2Mh0rs0w0ivUpezdU1tZZNn/view?usp=sharing) | Soon |
''')

if __name__ == "__main__":
    main()
