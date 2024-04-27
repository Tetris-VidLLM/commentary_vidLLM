# Commentary Using Vid-LLMs

### Calvin Kranig, Unmesh Raskar, Gurudatta Patil, Ram Goutham Gunasekaran

## 1 Introduction

### 1.1 Problem Statement
While there has been broad research in the field, there has not been
a universal video to commentary system that has been developed.
Our group plans to show that we can develop a commentary system
for professional Tetris with the hopes that it can be generalized in
the future.

### 1.2 Significance
Commentary in both real sports and video games serves to deepen
the emotional bond between fans and their favorite activities. Whether
watching a live match or playing a virtual game, commentary
enriches the viewing and playing experience, strengthening the
connection between the audience and the sport or game they en-
joy. Despite the ubiquity of this commentary, there exists many
games/sports that do not have any commentary limiting their ap-
peal and accessibility. Commentary plays a crucial role in enhancing
the experience of viewing various games and sports, aiding view-
ers in comprehending the unfolding action and enabling visually
impaired individuals to partake in events they might otherwise
miss out on. Beyond major professional events in sports and games,
the majority of recorded games and sports often lack any form
of commentary. Our group seeks to remedy this by developing a
commentary system that will be able to take in video clips and
produce commentary for the given sport/game.
Over the past couple of years there have been major break-
throughs in video and image interpretation tasks [[11]](#references)[[5]](#references). This field
has expanded into a large set of tasks including recognition, cap-
tioning, description, and question answering [[6]](#references). In a similar vein,
text to speech systems have been around for decades and there
are publicly available tools that allow for easy use [[1]](#references). Our group
plans to train a Vid-LLM model to produce textual commentary
for a video game using publicly available videos. This text will be
converted to audio using a TTS (Text-to-Speech) model to generate
audio commentary.

### 1.3 Major Objectives


## Final Result
<video width="640" height="360" controls>
  <source src="assets/output_with_commentary.mp4" type="video/mp4">
</video>

## [GitHub Page](https://github.com/Tetris-VidLLM/commentary_vidLLM)

## References
[1] 2023. What is Text-to-Speech? - Hugging Face — huggingface.co. https:
//huggingface.co/tasks/text-to-speech. (2023). [Accessed 20-02-2024].

[2] Sihan Chen, Handong Li, Qunbo Wang, Zijia Zhao, Mingzhen Sun, Xinxin Zhu,
and Jing Liu. 2023. VAST: A Vision-Audio-Subtitle-Text Omni-Modality Founda-
tion Model and Dataset. (2023). arXiv:cs.CV/2305.18500

[3] Sanyuan Chen, Yu Wu, Chengyi Wang, Shujie Liu, Daniel Tompkins, Zhuo Chen,
and Furu Wei. 2022. BEATs: Audio Pre-Training with Acoustic Tokenizers. (2022).
arXiv:eess.AS/2212.09058

[4] Sushant Gautam, Cise Midoglu, Saeed Shafiee Sabet, Dinesh Baniya Kshatri, and
Pål Halvorsen. 2022. Soccer Game Summarization using Audio Commentary,
Metadata, and Captions. In Proceedings of the 1st Workshop on User-Centric Nar-
rative Summarization of Long Videos (NarSUM ’22). Association for Computing
Machinery, New York, NY, USA, 13–22. https://doi.org/10.1145/3552463.3557019

[5] Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh,
Sandhini Agarwal, Girish Sastry, Amanda Askell, Pamela Mishkin, Jack Clark,
Gretchen Krueger, and Ilya Sutskever. 2021. Learning Transferable Visual Models
From Natural Language Supervision. (2021). arXiv:cs.CV/2103.00020

[6] Yunlong Tang, Jing Bi, Siting Xu, Luchuan Song, Susan Liang, Teng Wang, Daoan
Zhang, Jie An, Jingyang Lin, Rongyi Zhu, Ali Vosoughi, Chao Huang, Zeliang
Zhang, Feng Zheng, Jianguo Zhang, Ping Luo, Jiebo Luo, and Chenliang Xu.
2024. Video Understanding with Large Language Models: A Survey. (2024).
arXiv:cs.CV/2312.17432

[7] Classic Tetris. 2018. 2018 Classic Tetris World Championship. (Dec. 2018). https:
//www.youtube.com/playlist?list=PLA3elidp12Uu_aTr7X0cWnZ7bkB2YK_jQ

[8] Zhanyu Wang, Longyue Wang, Zhen Zhao, Minghao Wu, Chenyang Lyu,
Huayang Li, Deng Cai, Luping Zhou, Shuming Shi, and Zhaopeng Tu.
2023. GPT4Video: A Unified Multimodal Large Language Model for
lnstruction-Followed Understanding and Safety-Aware Generation. (2023).
arXiv:cs.CV/2311.16511

[9] Antoine Yang, Arsha Nagrani, Paul Hongsuck Seo, Antoine Miech, Jordi Pont-
Tuset, Ivan Laptev, Josef Sivic, and Cordelia Schmid. 2023. Vid2Seq: Large-Scale
Pretraining of a Visual Language Model for Dense Video Captioning. (2023).
arXiv:cs.CV/2302.14115

[10] Bang Yang, Tong Zhang, and Yuexian Zou. 2022. CLIP Meets Video
Captioning: Concept-Aware Representation Learning Does Matter. (2022).
arXiv:cs.CV/2111.15162

[11] Rowan Zellers, Ximing Lu, Jack Hessel, Youngjae Yu, Jae Sung Park, Jize Cao, Ali
Farhadi, and Yejin Choi. 2021. MERLOT: Multimodal Neural Script Knowledge
Models. (2021). arXiv:cs.CV/2106.02636
