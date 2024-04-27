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
throughs in video and image interpretation tasks [ 11 ][5]. This field
has expanded into a large set of tasks including recognition, cap-
tioning, description, and question answering [ 6]. In a similar vein,
text to speech systems have been around for decades and there
are publicly available tools that allow for easy use [ 1]. Our group
plans to train a Vid-LLM model to produce textual commentary
for a video game using publicly available videos. This text will be
converted to audio using a TTS (Text-to-Speech) model to generate
audio commentary.

### 1.3 Major Objectives


# Final Result
<video width="1280" height="720" controls>
  <source src="assets/output_with_commentary.mp4" type="video/mp4">
</video>