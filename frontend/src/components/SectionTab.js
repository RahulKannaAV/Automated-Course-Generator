"use client";
import * as React from 'react';
import PropTypes from 'prop-types';
import Tabs from '@mui/material/Tabs';
import Tab from '@mui/material/Tab';
import Box from '@mui/material/Box';
import { TypeAnimation } from 'react-type-animation';
import axios from 'axios';

function CustomTabPanel(props) {
  const { children, value, index, ...other } = props;

  return (
    <div
      role="tabpanel"
      hidden={value !== index}
      id={`simple-tabpanel-${index}`}
      aria-labelledby={`simple-tab-${index}`}
      {...other}
    >
      {value === index && <Box sx={{ p: 3 }}>{children}</Box>}
    </div>
  );
}

CustomTabPanel.propTypes = {
  children: PropTypes.node,
  index: PropTypes.number.isRequired,
  value: PropTypes.number.isRequired,
};

function a11yProps(index) {
  return {
    id: `simple-tab-${index}`,
    'aria-controls': `simple-tabpanel-${index}`,
  };
}

const SectionTab = (props) => {
  const [value, setValue] = React.useState(0);
  const [sequence, setSequence] = React.useState([]);


  React.useEffect(() => {
    const getTranscriptSequence = async() => {
      try {
        console.log(props.courseID, props.videoID);
        if(props.courseID.length > 0 && props.videoID.length > 0) {
        const sequenceResponse = await axios.get("http://localhost:5000/get-transcript-sequences", {
          params: {
            course_id: props.courseID,
            from_seconds: props.startTime,
            to_seconds: props.endTime,
            video_id: props.videoID
          }
        });

        setSequence(sequenceResponse.data);
      }
      } catch(e) {
        console.error(`Error in fetching Transcript Sequence: ${e}`)
      }
    } 

    getTranscriptSequence();
  }, [props.sectionID]); 

  const [currentSubtitles, setCurrentSubtitles] = React.useState([]);
  const [time, setTime] = React.useState(0);


  React.useEffect(() => {
    // Timer to simulate time progression
    const interval = setInterval(() => {
      setTime((prevTime) => prevTime + 1);
    }, 1000);

    return () => clearInterval(interval); // Cleanup interval on unmount
  }, []);

  React.useEffect(() => {
    // Find all subtitles matching the current time (allowing overlaps)
    const activeSubtitles = sequence.filter(
      (s) => time >= s.start && time <= s.end
    );
    setCurrentSubtitles(activeSubtitles);
  }, [time]);

  const handleChange = (event, newValue) => {
    setValue(newValue);
  };

  console.log(sequence, currentSubtitles);
  return (
    <Box sx={{ width: '100%' }}>
      <Box sx={{ borderBottom: 1, borderColor: 'divider' }}>
        <Tabs value={value} onChange={handleChange} aria-label="basic tabs example">
          <Tab label="References" {...a11yProps(0)} />
          <Tab label="Summary" {...a11yProps(1)} />
          <Tab label="Test your Knowledge" {...a11yProps(2)} />
        </Tabs>
      </Box>
      <CustomTabPanel value={value} index={0}>
        References
      </CustomTabPanel>
      <CustomTabPanel value={value} index={1}>
        Summary
      </CustomTabPanel>
      <CustomTabPanel value={value} index={2}>
        Test your Knowledge
      </CustomTabPanel>
    </Box>
  );
}

export default SectionTab;