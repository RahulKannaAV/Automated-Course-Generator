"use client"
import { useState, useEffect } from "react";
import styles from "./page.module.css";
import axios from 'axios';
import LoadingModal from "@/components/Modal";
import { TextField, Typography, Button } from "@mui/material";

const CourseCreation = () => {

    const [openModal, setModal] = useState(false);


    const [status, setStatus] = useState("Sit back and relax. We got this for you.");
    useEffect(() => {
        // Create EventSource instance for listening to events
        const eventSource = new EventSource('http://localhost:5000/events');
    
        // EventSource on message handler
        eventSource.onmessage = (event) => {
          const parsedData = JSON.parse(event.data);
          console.log("Received event:", parsedData);  // Log to track event sequence
          setStatus(parsedData.data);  // Update status based on event data
        };
    
        // EventSource error handler
        eventSource.onerror = () => {
          console.error("EventSource connection error.");
          eventSource.close();
        };
    
        // Reconnect on close or error
        eventSource.onclose = () => {
          console.log("EventSource connection closed. Reconnecting...");
          setTimeout(() => {
            const eventSource = new EventSource('http://localhost:5000/events');
          }, 5000); // Retry every 5 seconds
        };
    
        // Cleanup: Close the connection when the component unmounts
        return () => {
          eventSource.close();
        };
      }, []);

    const handleStartTask = async () => {        
        try {
            setModal(!openModal);

            // Start the task on the server
            const result = await axios.get('http://localhost:5000/create-course');
            console.log(result);
            // Begin listening for events if not already listening
            if(result.status == 200) {
                setModal(false);
            }
            
        } catch (error) {
            console.error("Error starting task:", error);
            setStatus("Failed to start task.");
        }
    };

    return (
        <div id={styles.page}>
            {openModal && <LoadingModal 
                            key={status}
                            message={"Preparing the plan"} 
                            desc={status}  />}
            <div id={styles.course_form}>
                <div id={styles.message}>
                    <Typography variant="h3" sx={{
                        marginTop: "7%",
                        marginLeft: "10%"
                    }}>
                        ACP
                    </Typography>
                    <div id={styles.text}>
                        <Typography variant="h2" sx={{
                            marginBottom: "20px"
                        }}>
                            Learn for the Future
                        </Typography>
                        <Typography variant="h5">
                            Create course plans with no hassle
                        </Typography>
                    </div>
                </div>
                <div id={styles.course_input}>
                    <Typography variant="h3" sx={{
                        textAlign: "center",
                        marginTop: "5%"
                    }}>
                        Create a Course
                    </Typography>
                    <div className={styles.course_field}>
                        <Typography variant="h4">
                            Video URL
                        </Typography>
                        <TextField 
                            fullWidth
                            placeholder="Enter Video URL"
                        />
                    </div>
                    <div className={styles.course_field}>
                        <Typography variant="h4">
                            Title
                        </Typography>
                        <TextField 
                            fullWidth
                            placeholder="Enter Course Title"
                        />
                    </div>
                    <div className={styles.course_submit}>
                        <Button variant="contained" onClick={handleStartTask}>
                            Create Course
                        </Button>

                    </div>
                </div>
            </div>
        </div>
    )
}

export default CourseCreation;