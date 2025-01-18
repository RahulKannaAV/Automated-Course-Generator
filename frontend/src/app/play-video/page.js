"use client";
import React, { useState } from 'react';
import YouTube from 'react-youtube';
import useAuth from '@/hooks/useAuth';

const YouTubePlayer = (props) => {
  const [startTime] = useState(props.startTime);  // in seconds (0:35)
  const [endTime] = useState(props.endTime);    // in seconds (0:40)

  const { currentUserID } = useAuth();

  const onReady = (event) => {
    const player = event.target;
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


  const opts = {
    height: '390',
    width: '640',
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
    <YouTube
      videoId={props.videoID}
      opts={opts}
      onReady={onReady}
      onStateChange={onStateChange}
    />
  );
};

export default YouTubePlayer;
