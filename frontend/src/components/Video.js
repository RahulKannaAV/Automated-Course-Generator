"use client";
import axios from 'axios';
import React, { useState, useEffect, useRef } from 'react';
import YouTube from 'react-youtube';

const CourseVideoPlayer = (props) => {
  const [startTime, setStartTime] = useState(props.startTime);  // in seconds (0:35)
  const [endTime, setEndTime] = useState(props.endTime);    // in seconds (0:40)
  const [audio, setAudio] = useState();
  const [videoID, setVideoID] = useState(props.videoID);
  const audioRef = useRef(null);

  console.log(audioRef)

  useEffect(() => {
    const getAudioData = async() => {
      try {
        const response = await axios.get(`http://localhost:5000/play-translation`, {
          responseType: "blob",
          params: {
            from_seconds: startTime,
            to_seconds: endTime,
            video_id: videoID
          }
        });
        console.log("Obtained from Backend");
        const audioSrc = URL.createObjectURL(response.data);
        setAudio(audioSrc);

          audioRef.current.load();
          audioRef.current.play();
        
      } catch(e) {
        console.error(`Error in fetching audio data: ${e}`)
      }
    }

    setStartTime(props.startTime);
    setEndTime(props.setEndTime);
    // getAudioData();
  }, [props.startTime, props.endTime, props.sectionID]);



  const onReady = (event) => {
    const player = event.target;
    player.setVolume(100);
    player.seekTo(startTime); // Seek to the start time
    player.playVideo();       // Start playing
  };


  const onStateChange = (event) => {
    const player = event.target;
    const currentTime = player.getCurrentTime();
    const playerState = event.data;

    // If the video reaches or exceeds the end time, stop the video
    if (currentTime >= endTime || playerState === window.YT.PlayerState.ENDED) {
      player.pauseVideo();  // Stop video completely when it reaches endTime
      player.seekTo(startTime);
    }
  };

  const onVideoPause = (event) => {
    if(audioRef.current) {
      audioRef.current.pause();
    }
  }


  const opts = {
    height: '576',
    width: '1024',
    playerVars: {
      autoplay: 1,
      controls: 0,  // Allow user control to press play manually
      showinfo: 0,
      loop: 0,      // Disable loop
      autohide: 1,
      modestbranding: 1,
      disablekb: 1,
      fs: 1,
      rel: 0,
      iv_load_policy: 3,
      start: startTime,
      end: endTime
    }
  };

  return (
    
    <div>
      <YouTube
      videoId={props.videoID}
      opts={opts}
      onReady={onReady}
      onStateChange={onStateChange}
      onPause={onVideoPause}
    />
    <audio ref={audioRef} controls hidden>
      <source src={audio} type="audio/mpeg" />
    </audio>
    </div>
  );
};

export default CourseVideoPlayer;
