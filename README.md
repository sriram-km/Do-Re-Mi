# Do-Re-Mi
A next level music assistant


## Inspiration 💡
I love Doraemon so much. I always wanted an assistant like him to assist with things. I was always curious about AI too. I wanted to do something kind of AI but I wasn't sure can I do it. So this time I did an AI to do the tasks we need to do by getting music as an input.
## What it does ⚙️
We have to say the hotword "Do-re-mi" to wake her up. She will make a sound to indicate that she is listening to us. Then have to do any of the below commands.
<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **Start**
<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; After the hotword. If we said "Start". she will start listening to us. We have to play some music by humming or through a musical instrument or just play it by using our phone. Then will identify the song and execute the command that has been configured for the song.
<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **New command**
<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; You can add actions for your favorite song by using the command "New command". Once you said this command, she will listen to your song identify it, and then ask you for the terminal command to be executed and the comment needs to be printed once your actions are done. For example, We have configured **Photograph by Ed Sheeran** to take a screenshot.
<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **Stop**
<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; When you don't want her to keep listening to you just say "Stop"

## How we built it ⚒️
We used **Snowball** to identify the hotword. We created the custom hotword "Do-re-mi" using snowball. Then we identify the command that needs to be run with the [Speech Recognition](https://github.com/Uberi/speech_recognition) Then we use **sounddevice** to record audio then save the file with **scipy** in a temp folder. Then we use **ARC cloud** to identify the song through their SDK. Then process the output from ARC, then we run through the JSON file where all commands will be stored to find the command configured for the song and then execute it.

## Challenges we ran into 👍
Training custom hotword "Do-re-mi" with Snowball because it needs to be short. Maintaining a JSON file as a DB. Recording and saving audio files with python. I haven't worked with this before.

## Accomplishments that we're proud of 😁
I am proud of building a hotword detection. I haven't done it before. I made an AI assistant with python. I am more into backend development. I use JAVA most of the time. This time I went with Python to try new technology and get out of my comfort zone.
## What we learned 📖
I learned many things in Python that I haven't used before. I got to know snowball which would be really helpful. I got to know many python libraries which I haven't used before.

## What's next for Do-Re-Mi ⏭️
Planning to add much more custom commands to Do-Re-Mi. I want to add play music when I hum songs I want Doremi to find and play the song I hummed.
