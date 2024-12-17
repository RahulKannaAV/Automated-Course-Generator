"use client"
import * as React from 'react';
import PropTypes from 'prop-types';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import CssBaseline from '@mui/material/CssBaseline';
import Divider from '@mui/material/Divider';
import Drawer from '@mui/material/Drawer';
import IconButton from '@mui/material/IconButton';
import InboxIcon from '@mui/icons-material/MoveToInbox';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import MailIcon from '@mui/icons-material/Mail';
import MenuIcon from '@mui/icons-material/Menu';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import CourseVideoPlayer from '@/components/Video';
import { useParams } from 'next/navigation';
import { useState, useEffect } from 'react';
import axios from 'axios';

const drawerWidth = 450;

function CoursePage(props) {

  const params = useParams();
  const [mobileOpen, setMobileOpen] = React.useState(false);
  const [isClosing, setIsClosing] = React.useState(false);
  const [sections, setSections] = useState([]);
  const [course_ID, setCourseID] = useState(params.course_id);
  const [sectionData, setSectionData] = useState({
    section_ID: undefined,
    video_ID: "",
    course_ID: params.course_id,
    section_start: 0,
    section_end: 0,
    section_name: "Course"
  });
  
  console.log(sectionData);
  useEffect(() => {
    const getAllSectionIDandTitle = async() => {
      const sectionData = await axios.get(`http://localhost:5000/sections/${course_ID}`);
      setSections(sectionData.data);
    }

    // Getting Video ID of the course
    const getVideoID = async() => {
      const videoData = await axios.get(`http://localhost:5000/get-video-id`, {
        params: {
          courseID: sectionData.course_ID
        }
      });

      setSectionData({...sectionData, video_ID: videoData.data});
    }


    getAllSectionIDandTitle();
    getVideoID();
    if(sectionData.sectionID !== undefined) {
      fetchNewSection();
    }
  }, [])

  const handleDrawerClose = () => {
    setIsClosing(true);
    setMobileOpen(false);
  };

  const handleDrawerTransitionEnd = () => {
    setIsClosing(false);
  };

  const handleDrawerToggle = () => {
    if (!isClosing) {
      setMobileOpen(!mobileOpen);
    }
  };

      // Get section content
      const fetchNewSection = async(content) => {
        const [sectionID, title] = content;

        const newSectionResponse = await axios.get(`http://localhost:5000/get-section-content`, {
          params: {
            sectionID: sectionID
          }
        });
    
        const newSectionData = newSectionResponse.data;
        setSectionData((prevSectionData) => ({
          ...prevSectionData,
          section_start: newSectionData.section_start,
          section_end: newSectionData.section_end,
          section_name: title,
          section_ID: sectionID,
        }));
      }


  const drawer = (
    <div>
      <Toolbar />
      <Divider />
      <List>
        {sections.length > 0 && sections.map((cand_key, index) => (
          <ListItem key={cand_key[1]} disablePadding>
            <ListItemButton onClick={async() => {await fetchNewSection(cand_key);}}>
              <ListItemIcon>
                {index % 2 === 0 ? <InboxIcon /> : <MailIcon />}
              </ListItemIcon>
              <ListItemText primary={`${index+1}) ${cand_key[1]}`} />
            </ListItemButton>
          </ListItem>
        ))}
      </List>
      <Divider />
      <List>
        {['All mail', 'Trash', 'Spam'].map((text, index) => (
          <ListItem key={text} disablePadding>
            <ListItemButton>
              <ListItemIcon>
                {index % 2 === 0 ? <InboxIcon /> : <MailIcon />}
              </ListItemIcon>
              <ListItemText primary={text} />
            </ListItemButton>
          </ListItem>
        ))}
      </List>
    </div>
  );


  return (
    <Box sx={{ display: 'flex' }}>
      <CssBaseline />
      <AppBar
        position="fixed"
        sx={{
          width: { sm: `calc(100% - ${drawerWidth}px)` },
          ml: { sm: `${drawerWidth}px` },
        }}
      >
        <Toolbar>
          <IconButton
            color="inherit"
            aria-label="open drawer"
            edge="start"
            onClick={handleDrawerToggle}
            sx={{ mr: 2, display: { sm: 'none' } }}
          >
            <MenuIcon />
          </IconButton>
          <Typography variant="h6" noWrap component="div">
            Generative AI Course
          </Typography>
        </Toolbar>
      </AppBar>
      <Box
        component="nav"
        sx={{ width: { sm: drawerWidth }, flexShrink: { sm: 0 } }}
        aria-label="mailbox folders"
      >
        {/* The implementation can be swapped with js to avoid SEO duplication of links. */}
        <Drawer
          variant="temporary"
          open={mobileOpen}
          onTransitionEnd={handleDrawerTransitionEnd}
          onClose={handleDrawerClose}
          ModalProps={{
            keepMounted: true, // Better open performance on mobile.
          }}
          sx={{
            display: { xs: 'block', sm: 'none' },
            '& .MuiDrawer-paper': { boxSizing: 'border-box', width: drawerWidth },
          }}
        >
          {drawer}
        </Drawer>
        <Drawer
          variant="permanent"
          sx={{
            display: { xs: 'none', sm: 'block' },
            '& .MuiDrawer-paper': { boxSizing: 'border-box', width: drawerWidth },
          }}
          open
        >
          {drawer}
        </Drawer>
      </Box>
      <Box
        component="main"
        sx={{ flexGrow: 1, p: 3, width: { sm: `calc(100% - ${drawerWidth}px)` } }}
      >
        <Toolbar />
        <Typography sx={{ marginBottom: 2 }}>
          {sectionData.section_name}
        </Typography>
        <CourseVideoPlayer 

            startTime={sectionData.section_start}
            endTime={sectionData.section_end}
            key={sectionData.section_ID}
            videoID={sectionData.video_ID}/>
      </Box>
    </Box>
  );
}

export default CoursePage;
