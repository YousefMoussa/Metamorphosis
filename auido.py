import ffmpeg

input_file = 'AnswerRecording1.mp4'
output_file = 'temp_audio1.mp3'

(
    ffmpeg
    .input(input_file)
    .output(output_file, format='mp3')
    .run()
)
