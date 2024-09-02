# MediaPlayer
A media player that plays audiovisual recordings while displaying a survey on a second monitor. Synchronization between the survey and media player is achieved using codes named receiver, sender, and mqttclient. This allows for conducting perception studies on audio-visual stimuli and saving results to a text file.

Features

    • MQTT Communication: Utilizes the paho-mqtt library for efficient message transfer between the sender and receiver.
    • Audio-Visual Playback: Integrates the vlc library for playing video files.
    • User Interface: Provides a user-friendly interface using tkinter for displaying the test and gathering responses.
    • Survey Module: Implements a customizable survey to gather user feedback on perceived synchronization between audio and video streams.
    • Threaded Execution: Uses Python's threading to handle the asynchronous sending and receiving of media files.

Components

    1. demo_rec.py - This script acts as the receiver, listening for incoming MQTT messages that trigger video playback.
    2. demo_send.py - The sender script, which sends video files over MQTT and initiates playback on the receiver's side.
    3. mqttclient.py - A custom MQTT client wrapper, handling the connection, message publishing, and subscription to topics.
    4. main.py - The main entry point for the application, initializing the user interface and managing the overall experiment flow.

Setup and Installation

  1.  Prerequisites:
     
       • Python 3.x
       • Required libraries: paho-mqtt, vlc, tkinter, PIL, cv2, screeninfo

  3.  Installation:
    
     pip install paho-mqtt python-vlc pillow opencv-python screeninfo

 3.  Running the Application:

   • Start the receiver by executing demo_rec.py.
   • Start the sender by executing demo_send.py.
   • Run main.py to launch the user interface and begin the experiment.


Usage

   1. Launch the application via main.py.
   2. Follow the instructions displayed on the user interface to conduct the synchronization test.
   3. Respond to each survey question as prompted after each video sequence.
   4. Results are saved locally for further analysis.
